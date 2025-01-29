# Create a Wallet (Coldkey)

<div class="warning">
Pre requirements 

You need to have `jucli` (Jungo-CLI) on your system. 
You can install it from [here](../tools/jungo-cli.md#Installation).
</div>

Coldkey is a synonym for Wallet in JungoAI.

Create a new wallet:

```bash
jucli wallet new_coldkey
```

You will see the following prompts:

- `Enter the path to the wallets directory (~/.jungoai/wallets/):`<br>
Default is `~/.jungoai/wallets/`, press enter or write another path as you want.

- `Enter the wallet name (default): alan`<br>
Enter your desire name for your coldkey (wallet name). In this example we used `alan`.

- `Choose the number of words [12/15/18/21/24]:`<br>
Write number of words for secret phrase.

- `Enter your password:`<br>
Write a password for your wallet.

- `The mnemonic to the new coldkey is: ...`<br>
Save your mnemonic in a safe place, it will used to recover the coldkey.

Now check your wallet:

```bash
jucli wallet list
```
