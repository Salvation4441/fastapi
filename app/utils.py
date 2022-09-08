from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# this hash the password
def hash(password: str):
    return pwd_context.hash(password)


# try to verify the hashed password
def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)
