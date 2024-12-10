import json
from web3 import Web3, HTTPProvider

w3 = Web3(HTTPProvider('http://127.0.0.1:8545'))

f = open('/Users/florian/Documents/GitHub/BankSmartContrat/build/contracts/Bank.json')
data = json.load(f)

abi = data['abi']
address = '0x7433c538ae2b187443224f80617aaa04D6d085a9' 

contract = w3.eth.contract(address=address, abi=abi)
print(contract)

isConnected = isConnected = w3.is_connected()
blocknumber = w3.eth.block_number


print('Connected:', isConnected, 'BlockNumber:', blocknumber)

contract.functions.deposit_funds().transact({'from': w3.eth.accounts[2], 'value': 50})
tx = contract.functions.transfer_funds(w3.eth.accounts[1], 25).transact({'from': w3.eth.accounts[2]})

blocks = contract.functions.get_blocks().call({'from': w3.eth.accounts[2]})

for num in blocks:
        block = w3.eth.get_block(num)
        tx = w3.eth.get_transaction(block.transactions[0])
        hist = contract.decode_function_input(tx.input) 

        if str(hist[0]) == '<Function deposit_funds()>':
            print("Funds Deposited:", tx.value)
        elif str(hist[0]) == '<Function withdraw_funds(uint256)>':
            print("Funds Withdrawn:", hist[1]['_funds'])
        else:
            print("Funds transferred to account number", hist[1]['receiving_address'], ":", hist[1]['_funds'])