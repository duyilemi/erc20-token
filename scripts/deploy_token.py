from brownie import Token
from scripts.helper_script import get_account
from web3 import Web3

initial_supply = Web3.toWei(1000, "ether")

def main():
    deploy_token()

def deploy_token():
    account = get_account()
    token = Token.deploy(initial_supply, {"from": account})
    print(token.name())
