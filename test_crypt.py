import crypt

text = "Hello world!"
key = "password"

enc = crypt.encrypt(text, key)

print("Encrypted: ", enc)

print("Decrypted: ", crypt.decrypt(enc, key))