from web3 import Web3
import json


# contract info
contract_ABI = json.loads('[{"inputs": [{"internalType": "uint256","name": "num","type": "uint256"}],"name": "store","outputs": [],"stateMutability": "nonpayable","type": "function"},{"inputs": [],"name": "retrieve","outputs": [{"internalType": "uint256","name": "","type": "uint256"}],"stateMutability": "view","type": "function"}]')
contract_address = "0xCD088Fd40A0C88CE62f9f44A8EA2237014027980"


# infura info
infura_api_key = "" # this is required
infura_base_url = "https://kovan.infura.io/v3/"

# user account info
public_key = "0xcafc4D40877005f869d998b70d15492e058aF5f2"
private_key = "" # this is required if a payment is needed





# connect to the http provider
provider = Web3.HTTPProvider(infura_base_url + infura_api_key)
web3 = Web3(provider)

# built contract
contract = web3.eth.contract(address=contract_address, abi=contract_ABI)


# get
data = contract.functions.retrieve().call()
print(data)


# set
# num = 10
# transaction_base = {
#     'nonce': web3.eth.getTransactionCount(public_key)
#     }

# unsigned_transaction = contract.functions.store(num).buildTransaction(transaction_base)

# signed_transaction = web3.eth.account.signTransaction(unsigned_transaction, private_key=private_key)

# transaction_hash = web3.eth.sendRawTransaction(signed_transaction.rawTransaction)
# print(transaction_hash)



