import hashlib


def encrypt(normalString):
    hashedString = hashlib.sha256(normalString.encode('ascii')).hexdigest()
    return hashedString