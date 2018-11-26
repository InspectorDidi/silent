import chilkat
crypt = chilkat.CkCrypt2()
crypt.put_CryptAlgorithm("aes")
crypt.put_KeyLength(256).
prng = chilkat.CkPrng()
secretKeyHex = prng.genRandom(32,"hex")
#  It is important that the number of bytes in the secret key
#  matches the value specified in the KeyLength property (above).
crypt.SetEncodedKey(secretKeyHex,"hex")
print("randomly generated key: " + secretKeyHex)
crypt.put_HashAlgorithm("SHA256")
crypt.put_EncodingMode("hex")
secretKeyHex = crypt.hashStringENC("mypassword")
crypt.SetEncodedKey(secretKeyHex,"hex")
print("password-based key: " + secretKeyHex)


This source code is by https://www.example-code.com/python/generate_encryption_key.asp.
They hold all rights to this code to.
