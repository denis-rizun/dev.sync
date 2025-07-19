from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class PasswordHelper:

    @staticmethod
    def hash_password(pwd: str) -> str:
        return pwd_context.hash(pwd)

    @staticmethod
    def check_password(pwd: str, hashed_pwd: str) -> bool:
        return pwd_context.verify(pwd, hashed_pwd)
