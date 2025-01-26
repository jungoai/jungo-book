# Run Jungochain RPC node

## Hardware Requirements

<style>
table {
  width: 100%;
}

th, td {
  width: 33%;
}
table th:nth-child(1), table td:nth-child(1) {
  width: 20%;
}
</style>

<!-- System Requirements: -->

| System Requirements |    |
|:--------------|----------|
| RAM           | ~286 MiB |
| Architectures | Linux x86_64: `Linux kernel 2.6.32+` `glibc 2.11+` <br> MacOS x86_64: `MacOS 10.7+` `(Lion+)` |

| Network Requirements             |  |
|:---------------------------------|--|
| Access to the public internet    |  |
| Jungochain runs on ipv4          |  |
| Port 9944  | Websocket. This port is used by jungo-sdk and jungo-cli.It only accepts connections from localhost.Make sure this port is firewalled off from the public domain unless you wanted to run a RPC node.|
| Port 9939  | RPC. This port is opened, but not used. |
| Port 30333 | p2p socket. This port accepts connections from other jungochain nodes.Make sure your firewall(s) allow incoming traffic to this port.|

- It is assumed your default outgoing traffic policy is ACCEPT. If not, make sure outbound traffic to port 30333 is allowed.

The easiest way to run a node is via docker:

## Run via Docker

### Login to ghcr.io

- Generate a PAT:
  - Go to [GitHub Developer Settings](https://github.com/settings/tokens).
  - Click *Generate new token* (classic).
  - Select scopes: read:packages (to pull images).
- Login to ghcr.io
```bash
echo "<your_personal_access_token>" | docker login ghcr.io -u <your_github_username> --password-stdin
```

### Pull docker image:

```bash
docker pull ghcr.io/jungoai/jungochain:0.1.0-devnet
```

### Run image

Simply run:

```bash
. ./scripts/bootstrap/run_by_docker.sh
```

It will not expose RPC to external request by default, you need to pass `--rpc` for that. Also there are other options:

```bash
. ./scripts/bootstrap/run_by_docker.sh \
  --name myNodeName \
  --telemetry-url "wss://telemetry.polkadot.io/submit/ 0" \
  --rpc \
  --archive 
```
```
# --name <NAME>           # (optional) show your node name in telemetry
# --telemetry-url <ADDR>  # (optional) telemetry address
# --rpc                   # (optional) expose rpc to external requests
# --archive               # (optional) if you want to run archive node (it needs about 1.5 TB storage)
```

Note: chain data would be store on `"$HOME/.jungochain/"` directory

### Ensure running image

Check running container:
```bash
docker ps
```

It should show something like:
```bash
CONTAINER ID   IMAGE                                     COMMAND  CREATED          STATUS          PORTS     NAMES
ae61c5ea3863   ghcr.io/jungoai/jungochain:0.1.0-devnet   ...      13 seconds ago   Up 12 seconds             angry_perlma
```

Check the logs (use your container id instead of `ae61c5ea3863`):
```bash
docker logs ae61c5ea3863
```

You should see a line like:
```bash
🔍 Discovered new external address for our node: ...
```

You can stop the service whenever you want with:
```bash
docker stop <CONTAINER_ID>
```

If you are looking for building from source code, see [here](https://github.com/jungoai/jungochain?tab=readme-ov-file#for-jungochain-development)
