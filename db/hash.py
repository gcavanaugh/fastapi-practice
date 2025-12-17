from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes=["bcrypt_sha256"], deprecated="auto")

class Hash():
    def bcrypt(plain: str):
        return pwd_cxt.hash(plain)
    def verify(hashed, plain):
        return pwd_cxt.verify(plain, hashed)