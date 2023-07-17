from jose import JWTError, jwt
from fastapi import Depends, status, HTTPException
from fastapi.security.oauth2 import OAuth2PasswordBearer
from datetime import datetime, timedelta
import configparser
from app import schemas

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')

config = configparser.ConfigParser(interpolation=None)
config.read('app/config.ini')

SECRET_KEY = config.get("jwt_token","SECRET_KEY", raw=True)
ALGORITHM = config.get("jwt_token","ALGORITHM")

ACCESS_TOKEN_EXPIRE_MINUTES = 30

def generate_token(data:dict):
    to_encode = data.copy()
    expiry = datetime.utcnownow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expiry})

    encode_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM )
    return encode_jwt

def verify_access_token(token:str, credential_exception):
    try:
        decode_jwt = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        get_id = decode_jwt.get("user_id")
        if get_id is None:
            raise credential_exception
        token_data = schemas.TokenData(id=get_id)
    except JWTError:
        raise credential_exception
    return token_data

def get_current_user(token:str = Depends(oauth2_scheme)):
    credential_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=f"credentials were not verified", headers=
                            {"WWW-Authenticate":"Bearer"})
    return verify_access_token(token, credential_exception)