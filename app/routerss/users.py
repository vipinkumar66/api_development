from fastapi import (HTTPException, Depends, status,
                     APIRouter)
from sqlalchemy.orm import Session

from app.database import get_db
from app import models, schemas
from app.utils import hash_password

router = APIRouter()

@router.post('/users/register', status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_new_users(user: schemas.UserBase, db:Session=Depends(get_db)):

    # HASHING THE PASSWORD
    hashed_password = hash_password(user.password)
    user.password = hashed_password

    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get('/users/{id}', response_model=schemas.UserOut)
def get_user(id:int, db:Session=Depends(get_db)):

    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"The user with the {id} is not found")
    return user