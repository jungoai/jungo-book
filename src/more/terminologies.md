# Terminologies

### JUNGO

The native token with decimal of 9.

### Wallet

Both of ECDSA (Ethereum wallet) and Sr25519 (Polkadot wallet) supported.

### Netuid

Each subnet has a unique Netuid in Jungochain.

### UID

Each node (Worker/Monitor) has a unique UID in that Subnet.
Before you run a node, you need to register UID on corresponding Subnet by your Coldkey and Hotkey,
that means a couple of Coldkey/Hotkey map to a UID on a Subnet.

### Root Subnet (or Subnet 0)

Is a specific Subnet that other Subnets are defined here.
In other word Subnet 0 contains Monitors and Subnets (instead of Workers),
emission will distribute here between subnets first,
then Subnets will distribute them between their nodes.
You can read more about emissions [here]().

### Tempo

Period of time reward distribute.

### Coldkey

### Hotkey
