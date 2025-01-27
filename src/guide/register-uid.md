# Register UID

- First of all you need to install [Jungo-CLI](https://github.com/jungoai/jungo-cli) (JungoAI command line tool).
- Create a Coldkey (Wallet)
- Create a Hotkey

## Install Jungo-CLI

1- Install Rye:
```bash
curl -sSf https://rye.astral.sh/get | bash
```

2- Install Jungo-CLI via Rye:
```bash
rye install jungo-cli --git https://github.com/jungoai/jungo-cli.git
```

Verify installation:
```bash
jucli --version
```

## Create a Coldkey
```bash
jucli wallet new_coldkey
```
`Enter the path to the wallets directory (~/.jungoai/wallets/):`, 
Default is ~/.jungoai/wallets/, press enter or write another path as you want

`Enter the wallet name (default): alan`, 
Enter your desire name for your coldkey (wallet name). In this example we use `alan`.

`Choose the number of words [12/15/18/21/24]:`,
Write number of words for secret phrase.

`Enter your password:`
Write a password for your wallet.

`The mnemonic to the new coldkey is: ...`,
Save your mnemonic in a safe place, it will used to recover the coldkey.

```bash
jucli wallet list
```

## Create a Hotkey
A hotkey is another address that placed under a coldkey. The coldkey is used to hold and transfer tokens. 
A hotkey (alongside coldkey) is used to register node (worker or monitor) and get staked to get reward 
in JungoAI ecosystem. The purpose of hotkey is to provide more security, 
coldkey for causal use like transfer tokens, and hotkey to be used in JungoAI ecosystem.

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

Now check your wallet.
```bash
jucli wallet list
```

## Get Token

Currently to get token you can DM Mr.Bakhshandeh at Telegram ([@rbakhshandeh](https://t.me/rbakhshandeh)).

## Register UID

We are showing registering UID on subnet 1001 (echo subnet) on devnet (you can do it on any subnet you want):

```bash
jucli subnet register --name <your-coldkey> --hotkey <your-hotkey> --netuid 1001 --chain devnet
```
