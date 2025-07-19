from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class PasswordHelper:
    @classmethod
    def hash_password(cls, pwd: str) -> str:
        return pwd_context.hash(pwd)

    @classmethod
    def check_password(cls, pwd: str, hashed_pwd: str) -> bool:
        return pwd_context.verify(pwd, hashed_pwd)
