# Create a Hotkey

<div class="warning">
Pre requirements 

You need to have `jucli` (Jungo-CLI) on your system. 
You can install it from [here](../tools/jungo-cli.md#Installation).

</div>

A hotkey is another address that placed under a coldkey. The coldkey is used to hold and transfer tokens. 
A hotkey (alongside coldkey) is used to register node (worker or monitor).
Stake and reward distribution also done in the hotkeys.
The purpose of hotkey is to provide more security, coldkey to be used for transfer tokens, 
and hotkey to be used in JungoAI ecosystem e.g stake.

```bash
jucli wallet new_hotkey
```

Fill the prompts. For example:

```
Enter the wallet name (default): alan
Enter the name of the new hotkey (default): alan-hotkey1
Enter the wallet path (Hint: You can set this with `jucli config set --wallet-path`) (~/.jungoai/wallets/):
Choose the number of words [12/15/18/21/24]: 12
```

Now check your wallet:

```bash
jucli wallet list
```
