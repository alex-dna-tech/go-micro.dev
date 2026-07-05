#!/usr/bin/env python3
"""Migrate Jekyll docs content into Hugo Docsy site using navigation.yml structure."""

import re
import os
import shutil
import sys

import yaml

NAV_FILE = 'tmp/_data/navigation.yml'
JEKYLL_DOCS_DIR = 'tmp/docs'
HUGO_DOCS_DIR = 'content/en/docs'

SECTION_DIR_MAP = {
    'core': 'overview',
    'interfaces': 'interfaces',
    'examples': 'examples',
    'guides': 'guides',
    'project': 'project',
}

CROSS_SECTION_URLS = {
    '/docs/guides/no-secret-first-agent.html',
    '/docs/guides/your-first-agent.html',
    '/docs/guides/zero-to-hero.html',
}

CROSS_SECTION_WEIGHTS = {
    '/docs/guides/no-secret-first-agent.html': 5,
    '/docs/guides/your-first-agent.html': 10,
    '/docs/guides/zero-to-hero.html': 20,
}

INDEX_URLS = {
    '/docs/',
    '/docs/examples/',
    '/docs/examples/realworld/',
    '/docs/guides/migration/',
    '/docs/architecture/',
}


def strip_jekyll_frontmatter(content):
    m = re.match(r'^---\s*\n.*?\n(---|\.\.\.)\s*\n', content, re.DOTALL)
    if m:
        return content[m.end():]
    return content


def rewrite_html_links(content):
    def _replace_link(m):
        pre = m.group(1)
        url = m.group(2)
        post = m.group(3)
        if url.endswith('.html') and not url.startswith(('http://', 'https://', '#')):
            url = url[:-5]
        return f'{pre}{url}{post}'

    return re.sub(r'(\]\()([^)]+\.html)(\))', _replace_link, content)


def rewrite_img_tags(content, target_dir):
    images_to_copy = []
    def _replace_img(m):
        src = m.group(1)
        alt = m.group(2)
        filename = src.rsplit('/', 1)[-1]
        src_path = os.path.join('tmp', 'images', 'generated', filename)
        dst_path = os.path.join(target_dir, filename)
        images_to_copy.append((src_path, dst_path))
        return f'![{alt}]({filename})'
    body = re.sub(
        r'<img\s+src="(/images/generated/[^"]+)"\s+alt="([^"]*)"[^>]*/?>',
        _replace_img,
        content,
    )
    return body, images_to_copy


def strip_duplicate_header_and_description(body, title):
    lines = body.split('\n')
    stripped = []
    found_h1 = False
    for line in lines:
        if not found_h1 and line.startswith('# ') and line[2:].strip() == title:
            found_h1 = True
            continue
        if found_h1 and not stripped and not line.strip():
            continue
        found_h1 = True
        stripped.append(line)
    return '\n'.join(stripped).strip() + '\n'


def get_description(body, title):
    for line in body.strip().split('\n'):
        line = line.strip()
        if not line or line.startswith('#') or line.startswith('![') \
                or line.startswith('```') or line.startswith('<img') \
                or line.startswith('<'):
            continue
        text = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', line)
        text = re.sub(r'[*_~`]', '', text).strip()
        if len(text) > 20:
            return text[:200]
    return f'Documentation for {title}'


def url_to_jekyll_source(url):
    path = url.lstrip('/')
    if path.endswith('.html'):
        path = path[:-5]
    if path.startswith('docs/'):
        path = path[5:]
    if path.startswith('badge'):
        return os.path.join('tmp', path + '.html')
    return os.path.join(JEKYLL_DOCS_DIR, path + '.md')


INDEX_PATH_MAP = {
    '/docs/': ('', '_index.md'),
    '/docs/examples/': ('examples', '_index.md'),
    '/docs/examples/realworld/': ('examples', 'realworld', '_index.md'),
    '/docs/guides/migration/': ('guides', 'migration', '_index.md'),
    '/docs/architecture/': ('project', 'architecture', '_index.md'),
}

def url_to_target_info(url, section):
    if url in INDEX_PATH_MAP:
        parts = INDEX_PATH_MAP[url]
        return os.path.join(HUGO_DOCS_DIR, *parts), None

    target_dir = SECTION_DIR_MAP.get(section, 'overview')
    if url in CROSS_SECTION_URLS:
        target_dir = 'guides'
    elif url.startswith('/badge'):
        target_dir = 'project'

    filename = url.rstrip('/').split('/')[-1]
    if filename.endswith('.html'):
        filename = filename[:-5]
    return os.path.join(HUGO_DOCS_DIR, target_dir, f'{filename}.md'), target_dir


def resolve_bundle_path(target_path):
    base_no_ext = target_path.rsplit('.', 1)[0]
    if os.path.isdir(base_no_ext):
        return os.path.join(base_no_ext, 'index.md')
    return target_path


def generate_frontmatter(title, weight, description, link_title=None, draft=False):
    lines = ['---']
    lines.append(f'title: "{title}"')
    if link_title:
        lines.append(f'linkTitle: "{link_title}"')
    lines.append(f'weight: {weight}')
    if draft:
        lines.append('draft: true')
    desc = description.replace('"', '\\"').replace('\n', ' ')
    lines.append(f'description: "{desc}"')
    lines.append('---')
    return '\n'.join(lines)


def kebab_to_title(s):
    s = s.replace('-', ' ').replace('_', ' ')
    parts = s.split()
    return ' '.join(p.capitalize() for p in parts)


def collect_nav_urls(nav):
    urls = set()
    for section in nav:
        items = nav[section]
        if isinstance(items, list):
            for item in items:
                if isinstance(item, dict) and 'url' in item:
                    urls.add(item['url'])
    return urls


def jekyll_path_to_orphan_target(rel_path):
    rel_no_ext = rel_path.rsplit('.', 1)[0]
    return os.path.join(HUGO_DOCS_DIR, rel_no_ext + '.md')


def process_orphan(jekyll_abs_path, target_path, nav_urls, nav_generated_paths, generated, errors):
    if target_path in nav_generated_paths:
        generated.append(f'{target_path} (skipped, nav-generated)')
        return

    with open(jekyll_abs_path) as f:
        content = f.read()

    body = strip_jekyll_frontmatter(content)
    body = rewrite_html_links(body)

    filename = os.path.basename(jekyll_abs_path)
    title = kebab_to_title(filename.rsplit('.', 1)[0])

    description = get_description(body, title)
    frontmatter = generate_frontmatter(title, 1, description, draft=True)

    body = strip_duplicate_header_and_description(body, title)

    target_file_dir = os.path.dirname(target_path)
    body, images_to_copy = rewrite_img_tags(body, target_file_dir)
    for src_img, dst_img in images_to_copy:
        if os.path.exists(src_img):
            shutil.copy2(src_img, dst_img)
            generated.append(f'  img: {dst_img}')

    os.makedirs(os.path.dirname(target_path), exist_ok=True)
    with open(target_path, 'w') as f:
        f.write(frontmatter + '\n' + body)

    generated.append(f'{target_path} (orphan, draft=true, weight=1)')


def process_orphans(nav, nav_generated_paths, generated, errors):
    nav_urls = collect_nav_urls(nav)

    for root, dirs, files in os.walk(JEKYLL_DOCS_DIR):
        rel_root = os.path.relpath(root, JEKYLL_DOCS_DIR)
        for f in files:
            if not f.endswith('.md'):
                continue

            if f in ('index.md', '_index.md'):
                continue

            jekyll_abs = os.path.join(root, f)
            rel_path = os.path.join(rel_root, f) if rel_root != '.' else f

            is_nav = False
            for url in nav_urls:
                jek_path = url_to_jekyll_source(url)
                if os.path.exists(jek_path) and os.path.samefile(jek_path, jekyll_abs):
                    is_nav = True
                    break

            if is_nav:
                continue

            target = jekyll_path_to_orphan_target(rel_path)
            process_orphan(jekyll_abs, target, nav_urls, nav_generated_paths, generated, errors)


def cleanup_stale_files():
    cleaned = []
    for root, dirs, files in os.walk(HUGO_DOCS_DIR):
        for f in files:
            file_path = os.path.join(root, f)
            base_no_ext = file_path.rsplit('.', 1)[0]

            if f.endswith('.md') and not f.startswith('_index'):
                if os.path.isdir(base_no_ext):
                    os.remove(file_path)
                    cleaned.append(file_path)

            if f.endswith('.jpg'):
                parent = os.path.dirname(file_path)
                bundle_dir = parent
                if os.path.basename(bundle_dir) != 'images':
                    jpg_base = file_path.rsplit('.', 1)[0]
                    if os.path.isdir(jpg_base):
                        os.remove(file_path)
                        cleaned.append(file_path)

    for root, dirs, files in os.walk(HUGO_DOCS_DIR):
        for f in files:
            if f.endswith('.jpg') and os.path.basename(root) != os.path.basename(f).rsplit('.', 1)[0]:
                parent_no_ext = os.path.join(os.path.dirname(root), os.path.basename(f).rsplit('.', 1)[0])
                if os.path.isdir(parent_no_ext):
                    file_path = os.path.join(root, f)
                    os.remove(file_path)
                    cleaned.append(file_path)

    return cleaned


def main():
    with open(NAV_FILE) as f:
        nav = yaml.safe_load(f)

    generated = []
    skipped = []
    errors = []
    nav_generated_paths = set()

    section_order = ['core', 'interfaces', 'examples', 'guides', 'project']
    guides_page_count = 0

    for section in section_order:
        items = nav.get(section, [])
        if not items:
            continue

        for pos, item in enumerate(items):
            url = item['url']
            title = item['title']

            if url in INDEX_URLS:
                for parts in INDEX_PATH_MAP.values():
                    nav_generated_paths.add(os.path.join(HUGO_DOCS_DIR, *parts))
                skipped.append(f'{title} → _index.md (preserved)')
                continue

            target_path_flat, target_dir = url_to_target_info(url, section)
            target_path = resolve_bundle_path(target_path_flat)
            nav_generated_paths.add(target_path)
            jekyll_source = url_to_jekyll_source(url)

            if url in CROSS_SECTION_WEIGHTS:
                weight = CROSS_SECTION_WEIGHTS[url]
            elif section == 'core':
                weight = pos * 10
            elif section == 'guides':
                weight = 30 + guides_page_count * 10
                guides_page_count += 1
            else:
                weight = (pos + 1) * 10

            if url == '/badge.html':
                _write_stub(target_path, title, weight)
                generated.append(f'{title} → {target_path} (stub, weight={weight})')
                continue

            if not os.path.exists(jekyll_source):
                errors.append(f'{title}: source not found: {jekyll_source}')
                continue

            with open(jekyll_source) as f:
                source_content = f.read()

            body = strip_jekyll_frontmatter(source_content)
            body = rewrite_html_links(body)
            target_file_dir = os.path.dirname(target_path)
            body, images_to_copy = rewrite_img_tags(body, target_file_dir)
            for src_img, dst_img in images_to_copy:
                if os.path.exists(src_img):
                    shutil.copy2(src_img, dst_img)
                    generated.append(f'  img: {dst_img}')
            description = get_description(body, title)
            body = strip_duplicate_header_and_description(body, title)

            link_title = None
            if title == 'MCP & AI Agents':
                link_title = 'MCP & AI Agents'

            frontmatter = generate_frontmatter(title, weight, description, link_title)

            os.makedirs(os.path.dirname(target_path), exist_ok=True)
            with open(target_path, 'w') as f:
                f.write(frontmatter + '\n' + body)

            generated.append(f'{target_path} (weight={weight})')

    print(f'Generated nav pages: {len(generated)}')
    for g in generated:
        print(f'  + {g}')
    if skipped:
        print(f'Skipped (_index preserved): {len(skipped)}')
        for s in skipped:
            print(f'  - {s}')

    print('\n--- Orphan content ---')
    orphan_generated = []
    process_orphans(nav, nav_generated_paths, orphan_generated, errors)
    print(f'Orphan pages: {len(orphan_generated)}')
    for g in orphan_generated:
        print(f'  + {g}')

    print('\n--- Cleanup stale files ---')
    cleaned = cleanup_stale_files()
    if cleaned:
        print(f'Removed {len(cleaned)} stale files:')
        for c in cleaned:
            print(f'  - {c}')
    else:
        print('No stale files to clean up.')

    if errors:
        print(f'\nErrors: {len(errors)}', file=sys.stderr)
        for e in errors:
            print(f'  ! {e}', file=sys.stderr)

    return len(errors) == 0


def _write_stub(target_path, title, weight):
    description = f'Documentation for {title}'
    frontmatter = generate_frontmatter(title, weight, description)
    os.makedirs(os.path.dirname(target_path), exist_ok=True)
    with open(target_path, 'w') as f:
        f.write(frontmatter + f'\n\n# {title}\n\n{description}\n')


if __name__ == '__main__':
    sys.exit(0 if main() else 1)
