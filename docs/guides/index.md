# Guides

LLMS index: [llms.txt](/llms.txt)

---

Section pages:

- [Migration Guides](/docs/guides/migration/): Step-by-step guides for migrating to Go Micro from other frameworks.
- [No-secret First Agent](/docs/guides/no-secret-first-agent/): This is the fastest first-agent success path when you do not have a provider key
- [Your First Agent](/docs/guides/your-first-agent/): This walkthrough builds the smallest useful Go Micro agent path: one service
- [0→hero Reference](/docs/guides/zero-to-hero/): The 0→hero path is the maintained, no-secret reference for the Go Micro services → agents → workflows lifecycle. It ties the CLI inner loop and the runtime harness together so a contributor can prove the framework still works as one system, not as separate demos.
- [Debugging your agent](/docs/guides/debugging-agents/): Use this guide when an agent surprises you: it answered without using a service,
- [Plan & Delegate](/docs/guides/plan-delegate/): Every Go Micro agent has two built-in capabilities, on top of the service tools it discovers:
- [Agent Guardrails](/docs/guides/agent-guardrails/): An autonomous agent decides its own actions at runtime, which is what makes it useful — and what makes it risky. The common failure modes are mundane: it loops, repeating the same call without making
- [Agents and Workflows](/docs/guides/agents-and-workflows/): Go Micro's AI primitives map directly onto the taxonomy in Anthropic's Building Effective Agents. That post draws one distinction that matters:
- [Agent Integration Patterns](/docs/guides/agent-patterns/): This guide covers common patterns for integrating AI agents with Go Micro services, from single-agent workflows to multi-agent architectures.
- [The Agent Harness](/docs/guides/agent-harness/): The first wave of agent frameworks solved one problem: put a model in a loop with
- [Agent Loops](/docs/guides/agent-loops/): Most agent work is one-shot: a prompt goes in, an answer comes out. The next
- [Agent2Agent (A2A)](/docs/guides/a2a-protocol/): Go Micro speaks the Agent2Agent (A2A) protocol — the open standard for agents on different frameworks to discover and call each other over HTTP. The A2A gateway is the agent-side analogue of the MCP g
- [AI Provider Guide](/docs/guides/ai-provider-guide/): This guide walks you through implementing a new AI model provider for
- [Provider Conformance](/docs/guides/provider-conformance/): Go Micro treats model providers as interchangeable pieces of the same agent
- [Atlas Cloud Integration](/docs/guides/atlascloud-integration/): Atlas Cloud is an enterprise AI infrastructure platform offering 300+ models across text, image, and video through a unified, OpenAI-compatible API. It is an official Go Micro sponsor and a first-clas
- [Payments (x402)](/docs/guides/x402-payments/): Go Micro can require a payment before a tool runs, using x402 — the open HTTP 402 Payment Required standard for stablecoin payments, designed for AI agents and onchain APIs. It lets every Go Micro end
- [Comparison](/docs/guides/comparison/): How Go Micro compares to other Go microservices frameworks.
- [Contributing](/docs/guides/contributing/): This is a rendered copy of the repository `CONTRIBUTING.md` for convenient access via the documentation site.
- [Quick Start](/docs/guides/quickstart/): Get up and running with go-micro in under 5 minutes.
