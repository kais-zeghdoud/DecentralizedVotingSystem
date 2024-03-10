import json, subprocess
from web3 import Web3

ganache_url = "http://127.0.0.1:8545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

def launch_blockchain():
    subprocess.run("ganache-cli --accounts=100 --networkId 1 --gasPrice 0 --deterministic --db ./blockchain --account_keys_path ./blockchain/keys.json", shell=True)

def get_accounts():
    if web3.isConnected():
        with open('./blockchain/keys.json', 'r') as file:
            keys = json.load(file)
        return keys["private_keys"]
    else:
        return False