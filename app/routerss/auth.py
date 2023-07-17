from fastapi import Depends, APIRouter, HTTPException, status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from app.database import get_db
from app import schemas, models, utils
from app.routerss import oauth2

from sqlalchemy.orm import Session

router = APIRouter(
    tags=['Authentication']
)

@router.post('/login')
# def user_login(user_credentials:schemas.UserLogin, db:Session=Depends(get_db)):
def user_login(user_credentials:OAuth2PasswordRequestForm = Depends(), db:Session=Depends(get_db)):

    user_details = db.query(models.User).filter(models.User.email == user_credentials.username).first()
    if not user_details:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials")

    if not utils.verify_password(user_credentials.password, user_details.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials")

    jwt_token = oauth2.generate_token({"user_id":user_details.id})

    return {"Token":jwt_token, "Token Type":"Bearer"}


