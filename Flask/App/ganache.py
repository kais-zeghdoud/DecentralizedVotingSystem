from web3 import Web3

ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))


def get_accounts():
    if web3.isConnected():
        accounts = {}
        for account in web3.eth.accounts:
            address = account
            pk = web3.eth.account.privateKeyToAccount(account).privateKey
            accounts[address] = pk
        return accounts
    else:
        return False
print(get_accounts())