# Terminologies

### JUNGO

The JungoAI native token with decimal of 9.

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

### Wallet

A Wallet is an address hold funds of JUNGO.
Both ECDSA (Ethereum wallet) and Sr25519 (Polkadot wallet) addresses are supported.

### Coldkey

Synonym for Wallet.

### Hotkey

A hotkey is another address that placed under a coldkey. The coldkey is used to hold and transfer tokens. 
A hotkey (alongside coldkey) is used to register node (worker or monitor).
Stake and reward distribution also done in the hotkeys.
The purpose of hotkey is to provide more security, coldkey to be used for transfer tokens
and hotkey to be used in JungoAI ecosystem e.g stake.
