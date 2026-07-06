# Architecture Decision Records

> Documentation of architectural decisions made in Go Micro, following the ADR pattern.

---

LLMS index: [llms.txt](/llms.txt)

---

## What are ADRs?

Architecture Decision Records (ADRs) capture important architectural decisions along with their context and consequences. They help understand why certain design choices were made.

### Planned

**Core Design**
- ADR-002: Interface-First Design
- ADR-003: Default Implementations

**Service Discovery**
- ADR-005: Registry Plugin Scope

**Communication**
- ADR-006: HTTP as Default Transport
- ADR-007: Content-Type Based Codecs

**Configuration**
- ADR-008: Environment Variable Support

## Status Values

- **Proposed**: Under consideration
- **Accepted**: Decision approved
- **Deprecated**: No longer recommended
- **Superseded**: Replaced by another ADR

## Contributing

To propose a new ADR:

1. Number it sequentially (check existing ADRs)
2. Follow the structure of existing ADRs
3. Include: Status, Context, Decision, Consequences, Alternatives
4. Submit a PR for discussion
5. Update status based on review

ADRs are immutable once accepted. To change a decision, create a new ADR that supersedes the old one.

---

Section pages:

- [Adr 001 Plugin Architecture](/docs/project/architecture/adr-001-plugin-architecture/): Microservices frameworks need to support multiple infrastructure backends (registries, brokers, transports, stores). Different teams have different preferences and existing infrastructure.
- [Adr 004 Mdns Default Registry](/docs/project/architecture/adr-004-mdns-default-registry/): Service discovery is critical for microservices. Common approaches:
- [Adr 009 Progressive Configuration](/docs/project/architecture/adr-009-progressive-configuration/): Microservices frameworks face a paradox:
- [Adr 010 Unified Gateway](/docs/project/architecture/adr-010-unified-gateway/): Authors: Go Micro Team
