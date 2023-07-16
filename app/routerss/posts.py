from fastapi import (HTTPException, Depends, status, Response,
                     APIRouter)
from typing import List
from sqlalchemy.orm import Session

from app.database import get_db
from app import models, schemas

router = APIRouter()

@router.get('/sqlalchemy', response_model=List[schemas.PostResponse])
def getall_posts(db:Session = Depends(get_db)):
    """
    This is to talk to the database and get the
    required data
    """
    posts = db.query(models.Post).all()
    return posts


@router.post('/sqlalchemy/createpost', response_model=schemas.PostResponse)
def create_new_post(post:schemas.PostResponse, db:Session=Depends(get_db)):
    # new_post = models.Post(title = post.title, content=post.content, published=post.published)
    new_post = models.Post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


@router.get('/sqlalchemy/posts/<int:pk>')
def get_individual_post(id:int, db:Session=Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    print(post)
    return post


@router.get('/sqlalchemy/post/delete/<id:int>')
def delete_post(id:int, db:Session=Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id)
    if post.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    post.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put('/sqlalchemy/post/update/<id:int>')
def update_post(id:int, post:schemas.PostCreate, db:Session=Depends(get_db)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    first_post = post_query.first()
    if first_post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    post_query.update(post.dict(), synchronize_session=False)
    db.commit()
    return post_query.first()