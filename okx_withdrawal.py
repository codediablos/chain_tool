import os

# python-dotenv should have been installed from the dependencies
from dotenv import load_dotenv
import okx.Account as Account
import okx.Funding as Funding

# read information from .env file
load_dotenv()

apikey = os.getenv('API_KEY')
secretkey = os.getenv('SECRET_KEY')
passphrase = os.getenv('PASSPHRASE')

flag = '0'
fundingAPI = Funding.FundingAPI(apikey, secretkey, passphrase, False, flag)

# Define the path to your file
file_path = 'addr_list.txt'

# Addresses to send ZETA or ZETA-based token to
recipient_addresses = []

# Open the file and read the addresses
try:
    with open(file_path, 'r') as file:
        for line in file:
            # Strip newlines and whitespace
            address = line.strip()
            # Add the address to the list if it's not empty
            if address:
                recipient_addresses.append(address)
except FileNotFoundError:
    print(f"The file {file_path} was not found.")

def get_currencies(name, chain):
    result = fundingAPI.get_currencies()
    for coin in result['data']:
        if coin['ccy'] == name and coin['chain'] == chain:
            return coin
    return None

def withdrawal(name, chain, toAddr, amt):
    coin = get_currencies(name, chain)
    return fundingAPI.withdrawal(
        ccy=coin['ccy'],
        toAddr=toAddr,
        amt=amt,
        fee=coin['minFee'],
        dest="4",
        chain=coin['chain']
    )

if __name__ == "__main__":
    amt = "4"
    for address in recipient_addresses:
        result = withdrawal("ZETA", "ZETA-ZetaChain", address, amt)
    print(result)
