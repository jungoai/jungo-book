# Run RPC Worker/Monitor

<div class="warning">
Pre requirements 

Before continuing make sure you have met [Registering UID](register-uid.md).
</div>

Clone rpc-subnet:
```bash
git clone https://github.com/jungoai/rpc-subnet.git
```
```bash
cd rpc-subnet
```

## Configuration

Create `.env` file
```bash
cp .env.example .env
```

Customize the parameters in the .env file. Some of these parameters are for Workers, 
others are for Monitors, and some are needed for both.

Create `.providers.json`
```bash
cp ./.providers.json ~/.providers.json
```

Open `.providers.json` in your favorite editor and add your RPC endpoints under `providers` field.
```bash
code ~/.providers.json
```

E.g: 
```json
{
  "providers": [
    "https://eth-mainnet.public.blastapi.io",
    "https://eth.llamarpc.com",
  ]
}
```

## Run with Docker

Run Worker:
```bash
. ./scripts/run_rpc_worker_docker.sh
```

Run Monitor:
```bash
. ./scripts/run_rpc_monitor_docker.sh
```

**Note**:
If you are connecting to a local jungochain node with `fast-blocks` enabled, you should pass 
`--fast_blocks` into `./scripts/run_rpc_monitor_docker.sh`

Also you can customize scripts.

## Development

See [here](https://github.com/jungoai/rpc-subnet?tab=readme-ov-file#rpc-subnet).
