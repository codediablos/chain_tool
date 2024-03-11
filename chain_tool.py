import os
from dotenv import load_dotenv

from hexbytes import HexBytes

from web3 import Web3
from eth_account import Account

load_dotenv()

# Connection to the Zeta Chain network
zeta_rpc_url = 'https://zetachain-mainnet-archive.allthatnode.com:8545'  # Replace with the actual Zeta Chain RPC URL
web3 = Web3(Web3.HTTPProvider(zeta_rpc_url))

# Check if connected to Zeta Chain network
if not web3.is_connected():
    raise ConnectionError("Failed to connect to Zeta Chain Network")

# Your wallet private key (NEVER share this with anyone!)
private_key = os.getenv('EVM_PRIVATE_KEY')  # It's safer to use an environment variable

if not private_key:
    raise ValueError("Private key not provided.")

send_amount = os.getenv('SEND_AMOUNT')
amount_value = 0.0
try:
    amount_value = float(send_amount)
    if amount_value == 0.0:
        raise ValueError("Invalid amount: 0.0")
except ValueError:
    print(f"Invalid amount: {send_amount}")

# Your wallet address
from_address = Account.from_key(private_key).address

# Ensure your wallet has enough balance for transactions + gas fees
balance = web3.eth.get_balance(from_address)
print(f"Current balance: {web3.from_wei(balance, 'ether')} ZETA or ZETA-based token")

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

# Amount of ZETA or ZETA-based token to send to each address
amount = web3.to_wei(amount_value, 'ether')  # Example: 0.1 ZETA or ZETA-based token

# Sending ZETA or ZETA-based token to each address
for address in recipient_addresses:
    nonce = web3.eth.get_transaction_count(from_address)

    # Transaction parameters
    tx = {
        'chainId': 7000,
        'nonce': nonce,
        'to': HexBytes(address),
        'value': amount,
        'gas': 21000,  # Adjust based on Zeta Chain's conditions
        'gasPrice': web3.to_wei('50', 'gwei'),  # Adjust based on current network conditions on Zeta Chain
    }

    # Sign the transaction
    signed_tx = web3.eth.account.sign_transaction(tx, private_key)

    # Send the transaction
    tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    print(f"Transaction sent to {address}, tx hash: {web3.to_hex(tx_hash)}")

    # Wait for the transaction to be mined
    tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
    print(f"Transaction receipt: {tx_receipt}")
