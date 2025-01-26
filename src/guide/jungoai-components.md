# JungoAI Componenets

Main Componenet of JungoAI ecosystem would be:
- Jungochain
- Subnet
  - Worker node
  - Monitor node

## Jungochain

Jungochain is the blockchain layer of JungoAI.

It handle transactions and serve Subnets, store information and metadata of 
Subnet itself and each nodes (worker or monitor), And incentivize them utilizing JUNGO token. 
You can find out how emission will distribute [here]().

Here is the Summarize of Jungochain:

- **JUNGO**: The native token with decimal of 9.
- **Wallet**: Both of ECDSA (Ethereum wallet) and Sr25519 (Polkadot wallet) supported.
- **Netuid**: Each subnet has a unique Netuid in Jungochain.
- **UID**: Each node (Worker/Monitor) has a unique UID in that Subnet.
- **Root Subnet (or Subnet 0)**: Is a specific Subnet that other Subnets are defined here. 
  In other word Subnet 0 contains Monitors and Subnets (instead of Workers), emission will distribute here
  between subnets first, then Subnet will distribute it between it's nodes. 
  You can read more about emissions [here]().
- **Tempo**: Period of time reward distribute.

## Subnet

A Subnet is a subnetwork under Jungochain, running an AI or Big Data service. How Subnet works:

Subnet is made of Worker nodes and Monitor nodes.

### Worker

The Worker is the node that AI/Big-data service run on.

### Monitor

The Monitor is the node that analyze Workers for distributing reward fair.

A Monitor also gets reward according to the average of Monitors result.
See [emission] section for more details.

Here is a diagram of a Subnet:

![figure subnet](../assets/subnet.png)
