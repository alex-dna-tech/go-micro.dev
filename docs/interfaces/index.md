# Interfaces

LLMS index: [llms.txt](/llms.txt)

---

Section pages:

- [Client/Server](/docs/interfaces/client-server/): Go Micro uses a client/server model for RPC communication between services.
- [Registry](/docs/interfaces/registry/): The registry is responsible for service discovery in Go Micro. It allows services to register themselves and discover other services.
- [Broker](/docs/interfaces/broker/): The broker provides pub/sub messaging for Go Micro services.
- [Transport](/docs/interfaces/transport/): The transport layer is responsible for communication between services.
- [Store](/docs/interfaces/store/): The store provides a pluggable interface for data storage in Go Micro.
- [Plugins](/docs/interfaces/plugins/): Plugins are scoped under each interface directory within this repository. To use a plugin, import it directly from the corresponding interface subpackage and pass it to your service via options.
