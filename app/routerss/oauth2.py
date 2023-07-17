from jose import JWTError, jwt
from datetime import datetime, timedelta
import configparser

config = configparser.ConfigParser(interpolation=None)
config.read('app/config.ini')

SECRET_KEY = config.get("jwt_token","SECRET_KEY", raw=True)
ALGORITHM = config.get("jwt_token","ALGORITHM")

ACCESS_TOKEN_EXPIRE_MINUTES = 30

def generate_token(data:dict):
    to_encode = data.copy()
    expiry = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expiry})

    encode_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM )
    return encode_jwt
