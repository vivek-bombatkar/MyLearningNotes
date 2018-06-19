

import web3, json, requests
from web3 import Web3, HTTPProvider
provider = HTTPProvider( 'http://localhost:60303' )
web3 = Web3(provider)

web3.eth.enable_unaudited_features()
with open(r'C:\Users\vkbomb\Downloads\MetaMaskAccountOnePrivateKey') as keyfile:
    encrypted_key = keyfile.read()
    print("encrypted_key : " + encrypted_key)
    private_key = web3.eth.accounts.decrypt(encrypted_key, 'Test!234') # Meta20!8
    print("private_key : " + private_key )

nonce = web3.eth.getTransactionCount('0x3dd4a296a99eb452296e8edf343d113b0b8b33a7')
print("nonce : " + nonce )
tx = {'value': 1000000000000000000, 'to': '0xbb626261a288fce1b678dff15eca7a2805c80242', 'nonce': nonce, 'chainId': 4, 'gasLimit': 6994000, 'gasPrice': 1000000000 }
tx['gas'] = web3.eth.estimateGas(tx)

signed = web3.eth.account.signTransaction(tx, private_key)
print("signed : " + signed)
web3.eth.sendRawTransaction(signed.rawTransaction)