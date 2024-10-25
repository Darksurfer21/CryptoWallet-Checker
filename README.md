# CryptoWallet-Checker

This script reads a list of mnemonic phrases, derives Ethereum addresses, and checks each for any balance. If a wallet with a balance is found, it displays the wallet type, address, mnemonic phrase, and balance. Users can choose to continue or stop the process after each wallet with a balance is found.

# Features

1. Wallet Identification: Detects the wallet type (Trust Wallet, MetaMask, or Other) based on standard Ethereum paths.

2. Balance Checking: Checks the balance of Ethereum addresses derived from provided mnemonic phrases.

3. User-Controlled Processing: Allows users to stop or continue checking after each wallet with a balance is found.

5. Concurrency: Uses threading for faster processing, making it suitable for handling large mnemonic files.

6. Detailed Reporting: Provides a summary of all checked phrases, including the number of wallets found with a balance.

# How It Works

Load Mnemonics: The script reads a list of mnemonic phrases from mnemonics.txt, with one phrase per line.

Generate Addresses: It derives Ethereum addresses for each mnemonic using a standard derivation path (m/44'/60'/0'/0/0).

Check Balance: For each derived address, it checks the balance on the Ethereum mainnet.

Display Results: If a balance is found, the script displays the wallet type, address, mnemonic, and balance in ETH, and prompts the user to continue or stop.

Save Results: Wallets with a balance are saved to found_wallets.txt for future reference.

# Prerequisites

Python: Ensure Python 3.6 or higher is installed.

Infura API: Obtain a Project ID from Infura to access the Ethereum mainnet.

Dependencies: Install required packages using:
bash
pip install web3 bip44
Usage
Set Up:

Replace YOUR_INFURA_PROJECT_ID in the script with your actual Infura Project ID.
Place mnemonics.txt in the same directory, containing one mnemonic phrase per line.
Run the Script:

```bash
python mnemonic_checker.py
'''


# Interact:

The script will begin checking balances and display results in the console.

After finding a wallet with balance, it will ask if you want to continue. Type Y to proceed or N to stop.

The checking process will stop if you input 'N' or type 'stop' in the console.

# View Results:

All wallets with a balance are saved in found_wallets.txt, showing wallet type, address, mnemonic, and balance in ETH.
Important Notes
Concurrency: The script uses threading to handle multiple mnemonics simultaneously, improving speed.
Eth Balance Display: Balances are shown in Ether (ETH).
File Safety: found_wallets.txt is updated with each wallet found with balance, so ensure no sensitive information is left in the file if sharing it.
Example
'''plaintext                            Found wallet with balance!       Wallet Type: Trust Wallet / MetaMask Address: 0x123456789ABCDEF... Mnemonic: example mnemonic phrase Balance: 0.15 ETH                                                           Do you want to continue checking? (Y/N): Y


This README.md covers the key features, setup, and usage instructions, making it easy for users to understand and run the code 

