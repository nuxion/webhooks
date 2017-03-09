import os
import binascii


# TOKEN generators from https://github.com/python/cpython/blob/3.6/Lib/secrets.py
DEFAULT_ENTROPY = 32  # number of bytes to return by default

def token_bytes(nbytes=None):
    """Return a random byte string containing *nbytes* bytes.
    If *nbytes* is ``None`` or not supplied, a reasonable
    default is used.
    >>> token_bytes(16)  #doctest:+SKIP
    b'\\xebr\\x17D*t\\xae\\xd4\\xe3S\\xb6\\xe2\\xebP1\\x8b'
    """
    if nbytes is None:
        nbytes = DEFAULT_ENTROPY
    return os.urandom(nbytes)

def token_hex(nbytes=None):
    """Return a random text string, in hexadecimal.
    The string has *nbytes* random bytes, each byte converted to two
    hex digits.  If *nbytes* is ``None`` or not supplied, a reasonable
    default is used.
    >>> token_hex(16)  #doctest:+SKIP
    'f9bf78b9a18ce6d46a0cd2b0b86df9da'
    """
    return binascii.hexlify(token_bytes(nbytes)).decode('ascii')

if __name__ =="__main__":
    print ("Token generated: token_hex(16)) 
    print ("Put in webhooks/instance/config.py")
