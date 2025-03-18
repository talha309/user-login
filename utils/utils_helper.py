import os
import jwt
from passlib.context import CryptContext
from typing import Optional
from datetime import datetime, timedelta
from dotenv import load_dotenv

pwd_context = CryptContext(schemes=("bcrpt"),depreacated= "auto")

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")

# Create token
def create_access_token(data: dict, expire_delta: Optional[timedelta] = None):
    try:
        to_encode = data.copy()
        expire = datetime.utcnow() + (expire_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
        to_encode.update({"exp": expire})
        return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    except Exception as e:
        print('An exception occurred')
        print(e)
        return None

# Decode the token
def decode_access_token(token: str):
    try:
        decode_token = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return decode_token
    except Exception as e:
        print('An exception occurred')
        print(e)
        return None


# check plain password and hash password 
# palin acheive from user and hash achieve from data-base
def verfiy_password (plain_password, hashed_password):
    return pwd_context.verify(plain_password,hashed_password)


# convert plain password into hashed password 

def hash_password(password):
    return pwd_context.hash(password)