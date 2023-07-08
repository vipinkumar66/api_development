from fastapi import (FastAPI,HTTPException, status,
                     Response, Depends)
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange
import models, schemas
from database import engine, get_db
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get('/sqlalchemy')
def getall_posts(db:Session = Depends(get_db)):
    """
    This is to talk to the database and get the
    required data
    """
    posts = db.query(models.Post).all()
    return {"data":posts}

@app.post('/sqlalchemy/createpost')
def create_new_post(post:schemas.PostBase, db:Session=Depends(get_db)):
    # new_post = models.Post(title = post.title, content=post.content, published=post.published)
    new_post = models.Post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return {"post":new_post}

@app.get('/sqlalchemy/posts/<int:pk>')
def get_individual_post(id:int, db:Session=Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    print(post)
    return {"data":post}

@app.get('/sqlalchemy/post/delete/<id:int>')
def delete_post(id:int, db:Session=Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id)
    if post.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    post.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
