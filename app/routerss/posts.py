from fastapi import (HTTPException, Depends, status, Response,
                     APIRouter)
from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.database import get_db
from app import models, schemas
from app.routerss import oauth2

router = APIRouter(
    prefix="/sqlalchemy",
    tags=['Posts']
)

@router.get('/', response_model=List[schemas.PostResponse])
# @router.get('/')
def getall_posts(db:Session = Depends(get_db), current_user:int = Depends(oauth2.get_current_user), limit:int=10, skip:int=0, search:Optional[str] = ""):
    """
    This is to talk to the database and get the
    required data
    """
    # print(current_user.email)
    posts = db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()

    results = db.query(models.Post, func.count(models.Votes.post_id).label("votes")).join(models.Votes, models.Votes.post_id == models.Post.id , isouter=True).group_by(models.Post.id).all()
    posts_list = []
    for post, votes in results:
        post_dict = post.__dict__  # Get the Post object as a dictionary
        post_dict["votes"] = votes  # Add the vote count to the dictionary
        posts_list.append(post_dict)

    return posts_list



@router.post('/createpost', response_model=schemas.PostResponse)
def create_new_post(post:schemas.PostCreate, db:Session=Depends(get_db), current_user:int = Depends(
    oauth2.get_current_user
)):
    # new_post = models.Post(title = post.title, content=post.content, published=post.published)
    user_id = current_user.id
    new_post = models.Post(user_id=user_id, **post.dict())

    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


@router.get('/posts/<int:pk>')
def get_individual_post(id:int, db:Session=Depends(get_db)):
    print(id)
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    print(post)
    return post


@router.get('/post/delete/<id:int>')
def delete_post(id:int, db:Session=Depends(get_db),
                userid:int = Depends(oauth2.get_current_user)):
    post = db.query(models.Post).filter(models.Post.id == id)
    if post.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    post.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put('/post/update/<id:int>')
def update_post(id:int, post:schemas.PostCreate, db:Session=Depends(get_db),
                userid:int = Depends(oauth2.get_current_user)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    first_post = post_query.first()
    if first_post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    post_query.update(post.dict(), synchronize_session=False)
    db.commit()
    return post_query.first()