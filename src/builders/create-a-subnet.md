# Create a Subnet

<div class="warning">
Pre requirements 

You need to have `jucli` (Jungo-CLI) on your system. 
You can install it from [here](../tools/jungo-cli.md#Installation).
</div>

Run command below to create a new Subnet:

```bash
jucli subnet create --wallet.name <your-coldkey> --chain_endpoint wss://devnet-rpc.jungoai.xyz
```

You will see something like this:

```
>> Your balance is: 200.000000000
>> Do you want to register a subnet for 1000.000000000? [y/n]: 
>> Enter password to unlock key: <YOUR_PASSWORD>
>> ✅ Registered subnetwork with netuid: 1002
```

After that you will be the owner of the Subnet.

<div class="warning">
Note 

User Subnet's netuid is an incremental id start from 1001, 
netuids from 1 to 1000 are reserved for base layer apps and netuid 0 is root subnet.
</div>
