# Register UID

<div class="warning">
Pre requirements 

You need to have `jucli` (Jungo-CLI) on your system. 
You can install it from [here](../tools/jungo-cli.md#Installation).

You should have a coldkey. Follow [here](create-a-wallet.md) to create one.

You should have hotkey. Follow [here](create-a-hotkey.md) to create one.
</div>

## Get Token

Currently you can get token by DM Mr.Bakhshandeh at Telegram ([@rbakhshandeh](https://t.me/rbakhshandeh)).

## Register UID

We are showing registering UID on subnet 1001 (echo subnet) on devnet (you can do it on any subnet you want):

```bash
jucli subnet register --name <your-coldkey> --hotkey <your-hotkey> --netuid 1001 --chain devnet
```
