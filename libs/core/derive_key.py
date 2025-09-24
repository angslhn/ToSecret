from base64 import urlsafe_b64encode
from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def derive_key(salt: bytes, password: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=SHA256(),
        length=32,
        salt=salt,
        iterations=1_200_000
    )
    
    return urlsafe_b64encode(kdf.derive(password))