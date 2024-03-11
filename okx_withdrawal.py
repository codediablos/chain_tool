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
    toAddr = "0x524595497F85B7D6104828f647cF95033ec09F7E"
    amt = "4"
    result = withdrawal("ZETA", "ZETA-ZetaChain", toAddr, amt)
    print(result)
