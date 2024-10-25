from web3 import Web3
from bip44 import Wallet
import time
import concurrent.futures
import threading

# Global variable to control processing
processing = True

# Function to identify wallet type based on derivation path
def identify_wallet_type(path):
    if path == "m/44'/60'/0'/0/0":
        return "Trust Wallet / MetaMask"
    else:
        return "Other Wallet"

# Function to check the balance of an address
def check_balance(address):
    try:
        # Connect to Ethereum network (you can change the provider if needed)
        w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID'))
        balance = w3.eth.get_balance(address)
        return balance
    except Exception as e:
        print(f"Error checking balance for {address}: {e}")
        return 0

# Function to generate address from mnemonic phrase and identify wallet type
def get_address_and_type_from_mnemonic(mnemonic, path="m/44'/60'/0'/0/0"):
    try:
        wallet = Wallet(mnemonic)
        address = wallet.derive_address(path)
        wallet_type = identify_wallet_type(path)
        return address, wallet_type
    except Exception as e:
        print(f"Error generating address from mnemonic: {e}")
        return None, None

# Function to process a single mnemonic and return details if it has a balance
def process_mnemonic(mnemonic):
    mnemonic = mnemonic.strip()
    if not mnemonic:
        return None, None, None, None

    # Derive address and identify wallet type
    address, wallet_type = get_address_and_type_from_mnemonic(mnemonic)
    if address:
        balance = check_balance(address)
        if balance > 0:
            return address, wallet_type, mnemonic, balance
    return None, None, None, None

# Function to listen for user commands to stop processing
def listen_for_stop_command():
    global processing
    while processing:
        command = input("Enter 'stop' to stop processing: ")
        if command.strip().lower() == 'stop':
            processing = False
            print("Stopping the processing...")

# Main function to read mnemonics, check balances, and save results
def check_mnemonic_phrases(file_path):
    global processing

    with open(file_path, 'r') as file:
        mnemonics = file.readlines()

    found_wallets = []
    total_processed = 0

    # Start the thread for listening to commands
    command_thread = threading.Thread(target=listen_for_stop_command)
    command_thread.start()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = {executor.submit(process_mnemonic, mnemonic): mnemonic for mnemonic in mnemonics}

        for future in concurrent.futures.as_completed(futures):
            total_processed += 1
            address, wallet_type, mnemonic, balance = future.result()

            if address:
                # Display wallet details when a balance is found
                print(f"\nFound wallet with balance!\nWallet Type: {wallet_type}\nAddress: {address}\nMnemonic: {mnemonic}\nBalance: {Web3.fromWei(balance, 'ether')} ETH\n")
                
                # Ask the user if they want to continue
                user_input = input("Do you want to continue checking? (Y/N): ").strip().lower()
                if user_input == 'n':
                    processing = False
                    break  # Exit if user chooses not to continue
                else:
                    print("Continuing with the next mnemonic...")

                found_wallets.append((address, wallet_type, mnemonic, balance))
            else:
                print(f"No balance found for mnemonic: {mnemonic}")

            # Show checking process
            if not processing:
                break  # Exit if processing is stopped

            print("Checking process continues...")

            # Optional: sleep for a bit to avoid hitting API rate limits
            time.sleep(1)

    # Save found wallets to a new file
    if found_wallets:
        with open('found_wallets.txt', 'a') as found_file:
            for wallet in found_wallets:
                address, wallet_type, mnemonic, balance = wallet
                found_file.write(f"Wallet Type: {wallet_type}\nAddress: {address}\nMnemonic: {mnemonic}\nBalance: {Web3.fromWei(balance, 'ether')} ETH\n\n")

    # Summary report
    print(f"\nTotal mnemonics processed: {total_processed}")
    print(f"Total wallets found with balance: {len(found_wallets)}")

# Usage
if __name__ == "__main__":
    check_mnemonic_phrases('mnemonics.txt')
