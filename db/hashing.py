from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes=['bcrypt'], deprecated='auto')


class Hash:

    @staticmethod
    def hash(password: str) -> str:
        return pwd_cxt.hash(password)

    @staticmethod
    def verify(hashed: str, plain: str) -> bool:
        return pwd_cxt.verify(plain, hashed)
