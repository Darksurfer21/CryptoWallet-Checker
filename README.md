# CryptoWallet-Checker

# Crypto Wallet Mnemonic Phrase Checker

This script reads a list of mnemonic phrases, derives Ethereum addresses, and checks each for any balance. If a wallet with a balance is found, it displays the wallet type, address, mnemonic phrase, and balance. Users can choose to continue or stop the process after each wallet with a balance is found.

# Features

Wallet Identification: Detects the wallet type (Trust Wallet, MetaMask, or Other) based on standard Ethereum paths.
Balance Checking: Checks the balance of Ethereum addresses derived from provided mnemonic phrases.
User-Controlled Processing: Allows users to stop or continue checking after each wallet with a balance is found.
Concurrency: Uses threading for faster processing, making it suitable for handling large mnemonic files.
Detailed Reporting: Provides a summary of all checked phrases, including the number of wallets found with a balance.
