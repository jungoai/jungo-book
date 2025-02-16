# Jungo CLI

Jungo-CLI is JungoAI command line tool, for managing wallets, making transactions, 
creating subnets and so on... .

## Installation

Install Rye:
```bash
curl -sSf https://rye.astral.sh/get | bash
```

Install Jungo-CLI via Rye:
```bash
rye tools install jungo-cli --git https://github.com/jungoai/jungo-cli.git
```

Verify installation:
```bash
jucli --version
```

See the `help` for more information:
```bash
jucli --help
```

Also you can get `help` for subcomamnds:
```bash
jucli <subcommand> --help
```

## Update Package

Update to last version:
```bash
rye tools install -f jungo-cli --git https://github.com/jungoai/jungo-cli.git
```

Install/Update a specific version (e.g version 0.1.0):
```bash
rye tools install -f jungo-cli --git https://github.com/jungoai/jungo-cli.git@v0.1.0
```
