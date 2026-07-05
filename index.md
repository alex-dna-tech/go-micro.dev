# Go Micro

> Go Micro - A Go microservices framework

---

LLMS index: [llms.txt](/llms.txt)

---

<section id="td-cover-block-0" class="row td-hero-block td-cover-block--height-full bg-pattern td-below-navbar js-td-cover -bg-dark-blue" >
  <div class="col-12">
    <div class="container td-overlay__inner">
      <div class="text-center">
        <div class="pt-3 lead">
          

<div class="d-flex justify-content-center align-items-center mb-5">
<div class="logo-container position-relative text-center" role="button">

<!-- Glow -->
<div class="logo-glow position-absolute top-0 start-0 w-100 h-100 rounded-circle"></div>

<svg width="300" height="300" viewBox="0 0 200 200" class="hexagon relative z-10">
<!-- Defs for gradients -->
<defs>
<linearGradient id="hexGradient" x1="0%" y1="0%" x2="100%" y2="100%">
<stop offset="0%" style="stop-color:#00ADD8;stop-opacity:1"></stop>
<stop offset="100%" style="stop-color:#5DC9E2;stop-opacity:1"></stop>
</linearGradient>
<linearGradient id="lineGradient" x1="0%" y1="0%" x2="100%" y2="100%">
<stop offset="0%" style="stop-color:#00ADD8;stop-opacity:0.8"></stop>
<stop offset="100%" style="stop-color:#00ADD8;stop-opacity:0.3"></stop>
</linearGradient>
</defs>
<!-- Outer Hexagon -->
<polygon points="100,10 185,55 185,145 100,190 15,145 15,55" fill="none" stroke="url(#hexGradient)" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"></polygon>
<!-- Inner Network Lines -->
<line x1="100" y1="100" x2="100" y2="55" stroke="url(#lineGradient)" stroke-width="2" class="network-line"></line>
<line x1="100" y1="100" x2="142.5" y2="77.5" stroke="url(#lineGradient)" stroke-width="2" class="network-line" style="animation-delay: 0.2s"></line>
<line x1="100" y1="100" x2="142.5" y2="122.5" stroke="url(#lineGradient)" stroke-width="2" class="network-line" style="animation-delay: 0.4s"></line>
<line x1="100" y1="100" x2="100" y2="145" stroke="url(#lineGradient)" stroke-width="2" class="network-line" style="animation-delay: 0.6s"></line>
<line x1="100" y1="100" x2="57.5" y2="122.5" stroke="url(#lineGradient)" stroke-width="2" class="network-line" style="animation-delay: 0.8s"></line>
<line x1="100" y1="100" x2="57.5" y2="77.5" stroke="url(#lineGradient)" stroke-width="2" class="network-line" style="animation-delay: 1s"></line>
<!-- Cross connections for distributed system look -->
<line x1="100" y1="55" x2="142.5" y2="77.5" stroke="rgba(0,173,216,0.2)" stroke-width="1" class="network-line" style="animation-delay: 1.2s"></line>
<line x1="142.5" y1="77.5" x2="142.5" y2="122.5" stroke="rgba(0,173,216,0.2)" stroke-width="1" class="network-line" style="animation-delay: 1.3s"></line>
<line x1="142.5" y1="122.5" x2="100" y2="145" stroke="rgba(0,173,216,0.2)" stroke-width="1" class="network-line" style="animation-delay: 1.4s"></line>
<line x1="100" y1="145" x2="57.5" y2="122.5" stroke="rgba(0,173,216,0.2)" stroke-width="1" class="network-line" style="animation-delay: 1.5s"></line>
<line x1="57.5" y1="122.5" x2="57.5" y2="77.5" stroke="rgba(0,173,216,0.2)" stroke-width="1" class="network-line" style="animation-delay: 1.6s"></line>
<line x1="57.5" y1="77.5" x2="100" y2="55" stroke="rgba(0,173,216,0.2)" stroke-width="1" class="network-line" style="animation-delay: 1.7s"></line>
<!-- Central Node (Core) -->
<circle cx="100" cy="100" r="12" fill="#0D1117" stroke="#00ADD8" stroke-width="3" class="network-node"></circle>
<circle cx="100" cy="100" r="6" fill="#00ADD8" class="network-node pulse"></circle>
<!-- Outer Nodes (Microservices) -->
<circle cx="100" cy="55" r="6" fill="#0D1117" stroke="#00ADD8" stroke-width="2" class="network-node node-1"></circle>
<circle cx="142.5" cy="77.5" r="6" fill="#0D1117" stroke="#00ADD8" stroke-width="2" class="network-node node-2"></circle>
<circle cx="142.5" cy="122.5" r="6" fill="#0D1117" stroke="#00ADD8" stroke-width="2" class="network-node node-3"></circle>
<circle cx="100" cy="145" r="6" fill="#0D1117" stroke="#00ADD8" stroke-width="2" class="network-node node-4"></circle>
<circle cx="57.5" cy="122.5" r="6" fill="#0D1117" stroke="#00ADD8" stroke-width="2" class="network-node node-5"></circle>
<circle cx="57.5" cy="77.5" r="6" fill="#0D1117" stroke="#00ADD8" stroke-width="2" class="network-node node-6"></circle>
<!-- Data packets animation -->
<circle cx="100" cy="77.5" r="2" fill="#5DC9E2" opacity="0">
<animate attributeName="opacity" values="0;1;0" dur="2s" repeatCount="indefinite" begin="0s"></animate>
<animate attributeName="cy" values="100;55" dur="2s" repeatCount="indefinite" begin="0s"></animate>
</circle>
<circle cx="121.25" cy="88.75" r="2" fill="#5DC9E2" opacity="0">
<animate attributeName="opacity" values="0;1;0" dur="2s" repeatCount="indefinite" begin="0.3s"></animate>
<animate attributeName="cx" values="100;142.5" dur="2s" repeatCount="indefinite" begin="0.3s"></animate>
<animate attributeName="cy" values="100;77.5" dur="2s" repeatCount="indefinite" begin="0.3s"></animate>
</circle>
</svg>

<!-- Text -->
<div class="text-center mb-5">
    <h1 class="display-3 fw-bold mb-4">
        <span class="gradient-text">GoMicro</span>
    </h1>
    <p class="lead text-gray-custom mb-5 mx-auto">
        A Go microservices framework
    </p>
</div>

</div>
</div>

<!-- prettier-ignore -->
<div class="td-cta-buttons my-5">
<a class="download-btn btn btn-go btn-lg d-inline-flex align-items-center gap-2" href="docs/">
Learn more
<i class="fa-solid fa-book-open-reader"></i>
</a>
<a class="btn btn-outline-go btn-lg d-inline-flex align-items-center gap-2"
href="https://github.com/alex-dna-tech/go-micro"
target="_blank" rel="noopener noreferrer">
Get the code
<i class="fa-brands fa-github"></i>
</a>
</div>




<a class="btn btn-link text-info" href="#td-block-1" aria-label="Read more"><i class="fa-solid fa-circle-chevron-down" style="font-size: 400%"></i></a>

</div>
      </div>
    </div>
  </div>
  
</section>


<div><a id="td-block-1" class="td-anchor-no-extra-offset"></a></div>
<section class="row td-box td-box--dark-blue bg-pattern py-5 td-box--height-auto">
  <div class="col container">
    <div class="row">
      
      
<div class="row g-4 justify-content-center">
<div class="col-lg-4 col-md-6">
<div class="variant-card variant-card--gradient rounded-4 p-4 border border-secondary">
<div class="variant-preview d-flex align-items-center justify-content-center rounded-3 mb-3">

<div class="pt-3 lead">
<div class="p-3 display-6">🔌</div>
</div>

</div>
<h3 class="fw-semibold fs-5 mb-1">Pluggable</h3>
<p class="small text-secondary mb-0">Swap components without changing code</p>

</div>


</div>

<div class="col-lg-4 col-md-6">
<div class="variant-card variant-card--gradient rounded-4 p-4 border border-secondary">
<div class="variant-preview d-flex align-items-center justify-content-center rounded-3 mb-3">

<div class="pt-3 lead">
<div class="p-3 display-6">⚡</div>
</div>

</div>
<h3 class="fw-semibold fs-5 mb-1">Zero Config</h3>
<p class="small text-secondary mb-0">Works out of the box with sensible defaults</p>

</div>


</div>

<div class="col-lg-4 col-md-6">
<div class="variant-card variant-card--gradient rounded-4 p-4 border border-secondary">
<div class="variant-preview d-flex align-items-center justify-content-center rounded-3 mb-3">

<div class="pt-3 lead">
<div class="p-3 display-6">🎯</div>
</div>

</div>
<h3 class="fw-semibold fs-5 mb-1">RPC First</h3>
<p class="small text-secondary mb-0">Swap components without changing code</p>

</div>


</div>

<div class="col-lg-4 col-md-6">
<div class="variant-card variant-card--gradient rounded-4 p-4 border border-secondary">
<div class="variant-preview d-flex align-items-center justify-content-center rounded-3 mb-3">

<div class="pt-3 lead">
<div class="p-3 display-6">📡</div>
</div>

</div>
<h3 class="fw-semibold fs-5 mb-1">Pub/Sub</h3>
<p class="small text-secondary mb-0">Swap components without changing code</p>

</div>


</div>

<div class="col-lg-4 col-md-6">
<div class="variant-card variant-card--gradient rounded-4 p-4 border border-secondary">
<div class="variant-preview d-flex align-items-center justify-content-center rounded-3 mb-3">

<div class="pt-3 lead">
<div class="p-3 display-6">🗄️</div>
</div>

</div>
<h3 class="fw-semibold fs-5 mb-1">State Management</h3>
<p class="small text-secondary mb-0">Unified store interface for persistence</p>

</div>


</div>

<div class="col-lg-4 col-md-6">
<div class="variant-card variant-card--gradient rounded-4 p-4 border border-secondary">
<div class="variant-preview d-flex align-items-center justify-content-center rounded-3 mb-3">

<div class="pt-3 lead">
<div class="p-3 display-6">🌐</div>
</div>

</div>
<h3 class="fw-semibold fs-5 mb-1">Multi-Transport</h3>
<p class="small text-secondary mb-0">HTTP, gRPC, NATS, and more</p>

</div>


</div>
</div>
</div>
  </div>
</section>

---

Section pages:

- [](/v5/)
- [](/v6/)
- [About Goldydocs](/about/): A sample site using the Docsy Hugo theme.
- [Blog](/blog/)
- [Documentation](/docs/)
- [Search Results](/search/)
- [Website information](/site/): Information about the website.
