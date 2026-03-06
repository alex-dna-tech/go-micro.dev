---
title: Go Micro
description: Go Micro - A Go microservices framework
params:
  body_class: td-navbar-links-all-active bg-pattern
---

{{% blocks/hero
  height="full bg-pattern td-below-navbar"
  color="dark-blue"
%}}

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
  <a {{% _param btn-lg primary %}} href="docs/">
    Learn more
  </a>
  <a {{% _param btn-lg secondary %}}
    href="{{% param github_project_repo %}}"
    target="_blank" rel="noopener noreferrer">
    Get the code
    {{% _param FA brands github "" %}}
  </a>
</div>

{{% blocks/link-down color="info" %}}
{{% /blocks/hero %}}

{{% blocks/section color="dark-blue bg-pattern py-5" type="row" %}}
<div class="row g-4 justify-content-center">
<div class="col-lg-4 col-md-6">
{{% elements/variant-card 
    title="Pluggable" 
    subtitle="Swap components without changing code" 
%}}
<div class="p-3 display-6">🔌</div>
{{% /elements/variant-card %}}
</div>

<div class="col-lg-4 col-md-6">
{{% elements/variant-card 
    title="Zero Config" 
    subtitle="Works out of the box with sensible defaults" 
%}}
<div class="p-3 display-6">⚡</div>
{{% /elements/variant-card %}}
</div>

<div class="col-lg-4 col-md-6">
{{% elements/variant-card 
    title="RPC First" 
    subtitle="Swap components without changing code" 
%}}
<div class="p-3 display-6">🎯</div>
{{% /elements/variant-card %}}
</div>

<div class="col-lg-4 col-md-6">
{{% elements/variant-card 
    color="light"
    title="Pub/Sub" 
    subtitle="Swap components without changing code" 
%}}
<div class="p-3 display-6">📡</div>
{{% /elements/variant-card %}}
</div>

<div class="col-lg-4 col-md-6">
{{% elements/variant-card 
    title="State Management" 
    subtitle="Unified store interface for persistence" 
%}}
<div class="p-3 display-6">🗄️</div>
{{% /elements/variant-card %}}
</div>

<div class="col-lg-4 col-md-6">
{{% elements/variant-card 
    title="Multi-Transport" 
    subtitle="HTTP, gRPC, NATS, and more" 
%}}
<div class="p-3 display-6">🌐</div>
{{% /elements/variant-card %}}
</div>
</div>
{{% /blocks/section %}}

