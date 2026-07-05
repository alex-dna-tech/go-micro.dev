#!/usr/bin/env python3
"""Migrate Jekyll docs content into Hugo Docsy site using navigation.yml structure."""

import re
import os
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


def get_description(body, title):
    for line in body.strip().split('\n'):
        line = line.strip()
        if not line or line.startswith('#') or line.startswith('![') \
                or line.startswith('```') or line.startswith('<img') \
                or line.startswith('<'):
            continue
        text = re.sub(r'[\[\]\(\)]', '', line)
        text = re.sub(r'[*_~`]', '', text).strip()
        if len(text) > 20:
            return text[:200]
    return f'Documentation for {title}'


def url_to_jekyll_source(url):
    # Remove leading / and strip .html
    path = url.lstrip('/')
    if path.endswith('.html'):
        path = path[:-5]
    # Remove /docs/ prefix to get relative path in tmp/docs/
    if path.startswith('docs/'):
        path = path[5:]
    # Handle special badge URL (/badge.html)
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


def generate_frontmatter(title, weight, description, link_title=None):
    lines = ['---']
    lines.append(f'title: "{title}"')
    if link_title:
        lines.append(f'linkTitle: "{link_title}"')
    lines.append(f'weight: {weight}')
    desc = description.replace('"', '\\"').replace('\n', ' ')
    lines.append(f'description: "{desc}"')
    lines.append('---')
    return '\n'.join(lines)


def main():
    with open(NAV_FILE) as f:
        nav = yaml.safe_load(f)

    generated = []
    skipped = []
    errors = []

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
                skipped.append(f'{title} → _index.md (preserved)')
                continue

            target_path, target_dir = url_to_target_info(url, section)
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
            description = get_description(body, title)

            link_title = None
            if title == 'MCP & AI Agents':
                link_title = 'MCP & AI Agents'

            frontmatter = generate_frontmatter(title, weight, description, link_title)

            os.makedirs(os.path.dirname(target_path), exist_ok=True)
            with open(target_path, 'w') as f:
                f.write(frontmatter + '\n' + body)

            generated.append(f'{target_path} (weight={weight})')

    print(f'Generated: {len(generated)}')
    for g in generated:
        print(f'  + {g}')
    if skipped:
        print(f'Skipped (_index preserved): {len(skipped)}')
        for s in skipped:
            print(f'  - {s}')
    if errors:
        print(f'Errors: {len(errors)}', file=sys.stderr)
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
