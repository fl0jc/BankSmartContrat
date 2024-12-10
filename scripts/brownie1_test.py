import json
from brownie import Bank, accounts, chain
from web3 import Web3, HTTPProvider

def main():
    w3 = Web3(HTTPProvider('http://127.0.0.1:8545'))
    f = open('/Users/florian/Documents/GitHub/BankSmartContrat/build/contracts/Bank.json')
    data = json.load(f)

    abi = data['abi']
    address = '0x7433c538ae2b187443224f80617aaa04D6d085a9'
    bank_contract = Bank.at(address)
    contract = w3.eth.contract(address=address, abi=abi)

    blocks = bank_contract.get_blocks({'from':accounts[1]})
    for num in blocks:
        block = chain[num]
        tx = w3.eth.getTransaction(block.transactions[0])
        hist = contract.decode_function_input(tx.input) 

        if str(hist[0]) == '<Function deposit_funds()>':
            print("Funds Deposited:", tx.value)
        elif str(hist[0]) == '<Function withdraw_funds(uint256)>':
            print("Funds Withdrawn:", hist[1]['_funds'])
        else:
            print("Funds transferred to account number", hist[1]['receiving_address'], ":", hist[1]['_funds'])