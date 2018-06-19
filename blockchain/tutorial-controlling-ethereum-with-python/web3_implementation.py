import json
import web3

from web3 import Web3, HTTPProvider, TestRPCProvider
from solc import compile_source
from web3.contract import ConciseContract

# Solidity source code
contract_source_code = '''
pragma solidity ^0.4.0;

contract Greeter {
    string public greeting;

    function Greeter() {
        greeting = 'Hello';
    }

    function setGreeting(string _greeting) public {
        greeting = _greeting;
    }

    function greet() constant returns (string) {
        return greeting;
    }
}
'''

### https://github.com/ethereum/py-solc/issues/46
compiled_sol = compile_source(contract_source_code) # Compiled source code
contract_interface = compiled_sol['<stdin>:Greeter']

#TODO
#https://www.google.de/search?rlz=1C1CHBF_enDE771DE771&ei=pkwpW9WyG8yukwWK6YuIDg&q=windows+Exception%3A+%60TestRPCProvider%60+requires+the+%60eth-testrpc%60+package+to+be+installed&oq=windows+Exception%3A+%60TestRPCProvider%60+requires+the+%60eth-testrpc%60+package+to+be+installed&gs_l=psy-ab.3...668654.668654.0.668856.2.2.0.0.0.0.1540.1648.0j1j8-1.2.0....0...1c.1.64.psy-ab..0.1.1537...35i39k1.0.74phguNF9NQ
#https://medium.com/@PrateeshNanada/steps-to-install-testrpc-in-windows-10-96989a6cd594
#https://github.com/trufflesuite/ganache-cli/wiki/Installing-TestRPC-on-Windows

# web3.py instance
w3 = Web3(TestRPCProvider())

# Instantiate and deploy contract
contract = w3.eth.contract(abi=contract_interface['abi'], bytecode=contract_interface['bin'])

# Get transaction hash from deployed contract
tx_hash = contract.deploy(transaction={'from': w3.eth.accounts[0], 'gas': 410000})

# Get tx receipt to get contract address
tx_receipt = w3.eth.getTransactionReceipt(tx_hash)
contract_address = tx_receipt['contractAddress']

# Contract instance in concise mode
abi = contract_interface['abi']
contract_instance = w3.eth.contract(address=contract_address, abi=abi,ContractFactoryClass=ConciseContract)

# Getters + Setters for web3.eth.contract object
print('Contract value: {}'.format(contract_instance.greet()))
contract_instance.setGreeting('Nihao', transact={'from': w3.eth.accounts[0]})
print('Setting value to: Nihao')
print('Contract value: {}'.format(contract_instance.greet()))
