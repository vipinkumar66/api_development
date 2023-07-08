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



all_posts = [
    {
        "id":1,
        "title":"Django",
        "content":"It is a python framework",
        "published":True,
        "ratings":"5"
    },
    {
        "id":2,
        "title":"FatsAPI",
        "content":"It is a framework based for makeing API",
        "published":False,
        "ratings":"4"
    }
]

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    ratings: Optional[int] = None

def find_post(id):
    for post in all_posts:
        if post['id'] == id:
            return post

def search_post_to_delete(id):
    for id_value, post_data in enumerate(all_posts):
        if post_data['id'] == id:
            print(True)
            return id_value

def search_post_to_update(id):
    for id_value, post_data in enumerate(all_posts):
        if post_data['id'] == id:
            return post_data


@app.get("/")
async def root():
    return {"message":"Hello stranger"}

@app.post("/get_data/", status_code=status.HTTP_201_CREATED)
# def get_post_data(payload: dict= Body(...)):
def get_post_data(new_post:Post):
    print(new_post)
    #so here our each post will be a type of pydantic model
    user_post = new_post.dict()
    user_post['id'] = randrange(3, 567890)
    all_posts.append(user_post)
    return {"Message":"Post data has been recieved", "data":user_post}

@app.get('/retrieve/post/{id}')
def get_individual_post( id:int):
    post = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"the post with the id: {id} was not found")
    return {"message":"Here is the post you requested",
            "data":post}

@app.delete('/delete/post/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_individual_post(id:int):
    # if request.method == "delete":
    get_id = search_post_to_delete(id)
    print(f"getid: {get_id}")
    if get_id is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"The post with id: {id} not found")
    else:
        all_posts.pop(get_id)
        return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put('/update/post/{id}', status_code=status.HTTP_201_CREATED)
def update_individual_post(id:int, updated_post:Post):
    # if request.method == "delete":
    get_post = search_post_to_update(id)
    # all_posts.remove(post)
    get_post.update(updated_post)
    return {"message":"The post has been updated and here is the data",
            "data":get_post}

@app.get('/sqlalchemy')
def create_post(db:Session = Depends(get_db)):
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
def get_individual(id:int, db:Session=Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    print(post)
    return {"data":post}

# @app.get('/')