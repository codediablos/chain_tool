import os, sys
from eth_account import Account
import secrets

def generate_ethereum_address():
    # Create a new account
    priv = secrets.token_hex(32)
    private_key = "0x" + priv
    acct = Account.from_key(private_key)
    return private_key, acct.address

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        # Generate the keys and address
        private_key, address = generate_ethereum_address()
        print(f"Private Key: {private_key}")
        print(f"Address: {address}")
        exit(0)

    try:
        num = int(sys.argv[1])
        with open('genr_addr.txt', 'w') as addr_file:
            with open('genr_key.txt', 'w') as key_file:
                for i in range(num):
                    private_key, address = generate_ethereum_address()
                    addr_file.write(f"{address}\n")
                    key_file.write(f"{private_key}\n")
    except FileNotFoundError:
        print(f"The file {file_path} was not found.")
    except ValueError:
        print("Please enter a valid number.")
