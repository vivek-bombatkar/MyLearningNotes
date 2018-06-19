#https://ethereum.stackexchange.com/questions/36310/transactions-created-using-web3-py-are-not-being-seen-on-the-ethereum-blockchain

#TODO
#ValueError: {'code': -32000, 'message': 'insufficient funds for gas * price + value'}

import web3
import time
w = web3.Web3(web3.HTTPProvider('https://mainnet.infura.io/12345678'))

# gas example
gas_limit = 250000
gas_price = 60
eth_amount=0
to_addr='0x3eA027E4c97bff4B6AC0F4C8fb35C581b4c5664e'
from_addr='0x3eA027E4c97bff4B6AC0F4C8fb35C581b4c5664e'
key='28b63c696d54c71ee798842d1a5adc8fe11d437526692309010589281e673b06'

transaction = {
    'to':to_addr,
    'from':from_addr,
    'value':int(eth_amount*(10**18)),
    'gas':gas_limit,
    'gasPrice':int(gas_price*(10**9)),
    'chainId':1,
    'nonce':int(time.time())
    }
signed_transaction = w.eth.account.signTransaction(transaction, key)
transaction_id = w.eth.sendRawTransaction(signed_transaction.rawTransaction)

print ('\nhttps://etherscan.io/tx/{0}'.format(transaction_id.hex()))
