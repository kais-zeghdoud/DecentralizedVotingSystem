import json
from web3 import Web3

ganache_url = "http://127.0.0.1:8545"
web3 = Web3(Web3.HTTPProvider(ganache_url))
ganache_cli_command = "ganache-cli --accounts=100 ---account_keys_path /Flask/App/keys.json"

def get_accounts():
    if web3.isConnected():
        with open('Flask/App/keys.json', 'r') as file:
            keys = json.load(file)
        return keys["private_keys"]
    else:
        return False