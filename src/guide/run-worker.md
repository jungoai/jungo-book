# Run Worker node

Before continuing make sure you have met [Registering UID](register-uid.md).

To demonstrate how to run a monitor node, we are going to do it on subnet 1001 (echo subnet) on
devnet as an example.

Install echo-subnet:

```
rye install echo-subnet --git https://github.com/jungoai/jungo-echo-subnet.git
```

*Note: you can install `rye` by `curl -sSf https://rye.astral.sh/get | bash`*

Run echo-monitor:

```
echo-worker \
  --ip            <your-public-host-ip> \
  --port          <your-host-port>      \
  --wallet.name   <your-coldkey>        \
  --wallet.hotkey <your-hotkey>         \
  --netuid        1001                  \
  --chain_endpoint wss://devnet-rpc.jungoai.xyz \
  --logging.debug
```

The above command will run echo-worker on the UID that registered by coldkey and hotkey.

Add stake to your hotkey (replace 100 with amount you want in JUNGO):

```
jucli stake add --amount 100 --name <your-coldkey> --hotkey <your-hotkey> --chain devnet
```

Check your node after a while:

```
jucli wallet overview --name <your-coldkey> --chain devnet
```
