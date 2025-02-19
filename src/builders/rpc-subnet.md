# RPC Subnet

It is the RPC provider subnet of JungoAI and functions as a decentralized, free and 
open-source solution. It could serve as a replacement for centralized solutions such as 
Infura, Alchemy, and others.

Key features:
- **Permissionless**: Anyone can run an RPC node and receive rewards in JUNGO.
- **Trustless**: Requests propagate to all nodes, and the result follows the majority. 
  Thus, the results from minority nodes are considered invalid in the presence of malicious nodes.
- **Efficient**: Nodes are ranked based on performance, latency, and trust, ensuring that 
  clients receive responses from the node with the lowest latency and highest trust.

Note: Currently just Ethereum RPC supported.

## How it works?

Worker nodes are RPC providers that anyone can run. On the other hand, 
monitor nodes measure the performance of worker nodes. Workers with 
higher uptime and accuracy gain more trust. On the client side, they can 
see the ranking of workers based on performance and trust. Additionally, 
the client receives responses from the geographically closest node with 
the lowest latency.

In the end, the client can choose to receive results in two ways:
- **Optimistic**: The client receives the result and processes it immediately. After a short delay, it receives validation.
  This method is more efficient and can be used on nodes with high trust.
- **Pessimistic**: The client receives a validated result, ensuring it follows the majority of nodes.
