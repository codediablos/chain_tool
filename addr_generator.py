from eth_account import Account
import secrets

def generate_ethereum_address():
    # Create a new account
    priv = secrets.token_hex(32)
    private_key = "0x" + priv
    acct = Account.from_key(private_key)
    return private_key, acct.address

# Generate the keys and address
private_key, address = generate_ethereum_address()

print(f"Private Key: {private_key}")
print(f"Address: {address}")
