#http://dominikharz.me/blockchain/2017/02/14/ethereum-python-integration.html

from web3 import Web3, TestRPCProvider

class ContractHandler:
  def __init__(self):
    self.web3 = Web3(RPCProvider(host='localhost', port='8545'))
    with open(str(path.join(dir_path, 'contract_abi.json')), 'r') as abi_definition:
      self.abi = json.load(abi_definition)
    self.contract_address = your_contract_address
    self.contract = self.web3.eth.contract(self.abi, self.contract_address)
