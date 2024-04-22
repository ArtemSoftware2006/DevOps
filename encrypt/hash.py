import hashlib

secret = 'Secret'

bsercret = secret.encode()

m = hashlib.md5()

m.update(bsercret)

print(m.digest())