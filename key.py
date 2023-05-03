from algosdk import account, mnemonic
private_key, address = account.generate_account()
mnemonic_phrase = mnemonic.from_private_key(private_key)
print(f"Private key: {private_key}")
print(f"Public address: {address}")
print(f"Mnemonic phrase: {mnemonic_phrase}")