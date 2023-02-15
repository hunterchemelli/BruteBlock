# Hunter Chemelli
# uses bip39_mnemonics_generator module (Copyright (c) 2018 Steven Hatzakis) to generate seed phrases to brute force find the seed phrase associated with a known ethereum account

from decouple import config
from web3 import Web3
import bip39_mnemonics_generator

TARGET_ADDRESS = config("TARGET_ADDRESS")
HTTP_PROVIDER = config("HTTP_PROVIDER")

FOUND = False

# establish connection to the ethereum blockchain
w3 = Web3(Web3.HTTPProvider(HTTP_PROVIDER))
# enable unaudited hd wallet features
w3.eth.account.enable_unaudited_hdwallet_features()

# find the address of the account associated with the current seed phrase
def find_address():
    # generate seed phrase using bip39_mnemonics_generator module
    seed_phrase = bip39_mnemonics_generator.main()
    # find the account associated with the seed phrase
    account = w3.eth.account.from_mnemonic(seed_phrase)
    # return the public address of the account
    return account.address, seed_phrase


# check if the address of the current account is the target address
def check_address(seed_phrase, address):
    # stop the program if the target address is found and print the seed phrase
    if address == TARGET_ADDRESS:
        global FOUND
        FOUND = True
        print("Seed phrase: " + seed_phrase)

if __name__ == "__main__":
    while FOUND == False:
        seed_phrase, address = find_address()
        check_address(seed_phrase, address)