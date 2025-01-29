# Create a Hotkey

<div class="warning">
Pre requirements 

You need to have `jucli` (Jungo-CLI) on your system. 
You can install it from [here](../tools/jungo-cli.md#Installation).

</div>

See [here](../more/terminologies.md#hotkey) for Hotkey definition.

Create a new hotkey:

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
