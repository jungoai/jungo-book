# Protocol

JungoAI Protocol consisted of 3 layer:

- Blockchain layer (Jungochain)
- Base Layer
- Apps Layer

## Jungochain

Jungochain is the blockchain layer of JungoAI.

It handles transactions and serve Subnets, store information and metadata of 
Subnet itself and each nodes (worker or monitor), And incentivize them utilizing JUNGO token. 
You can find out how emission will distribute [here]().

To get more details checkout [terminologies](../more/terminologies.md)

## Base Layer

The base layer is a list of **Subnets** running infrastructure services have optimized for 
serving other Subnets, e.g: De Storage, De Message Queue and etc... .

## Apps Layer

Apps Layer is a list of **Subnets** that give service to end-users.


## Subnet

A Subnet is a subnetwork under Jungochain, running an AI or Big Data service. 
It could be in Base Layer or Apps Layer. 

Everyone can run a Subnet on Jungochain by staking amount of JUNGO token, 
set configuration parameters and define the service API (to be used by the end-user).
After than other persons can run Worker and Monitor nodes that follow 
the rules (service API and configuration) on the subnet and get emission too.

*How Subnet works:*

Subnet is made of Worker nodes and Monitor nodes.

### Worker

Is actual node that run Big Data or AI service and serve end-user.

### Monitor

A Monitor analyze performance of Workers and send result (scores of Workers) back to the Jungochain. 
Then Jungochain distribute reward among Workers according to it.
A Monitor also gets reward according to the average of Monitor results.
See [emission](../more/emissions.md) section for more details.

Here is a diagram of a Subnet:

<center>
  <img src="../assets/subnet.png" alt="figure subnet" width="60%">
</center>

And Here is an overview of JungoAI ecosystem:

<center>
  <img src="../assets/protocol.png" alt="figure 1" width="60%">
</center>

For running a Subnet node see [here](guide/run-a-subnet-node.md).

Or if you want to create a new Subnet see [here]().
