from brownie import Bank, accounts

def main():
    Bank.deploy({'from': accounts[0], 'gas_price': '10 gwei', 'gas_limit': 3000000})
