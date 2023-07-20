from fastapi import (HTTPException, Depends, status, Response,
                     APIRouter)
from .. import schemas, database, models
from . import oauth2
from sqlalchemy.orm import Session
router = APIRouter(
    prefix="/votes"
)

@router.post('/', status_code=status.HTTP_201_CREATED)
def votes(vote:schemas.Vote, db:Session = Depends(database.get_db),
          current_user:int = Depends(oauth2.get_current_user)):

    post = db.query(models.Votes).filter(models.Votes.post_id == vote.post_id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"sorry the post with current id not found")

    vote_query = db.query(models.Votes).filter(models.Votes.post_id == vote.post_id, models.Votes.user_id == current_user.id)
    found_vote = vote_query.first()

    if (vote.dir==1):
        if found_vote:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"Sorry but {current_user.email} has already liked the post")
        new_vote = models.Votes(post_id = vote.post_id, user_id = current_user.id)
        db.add(new_vote)
        db.commit()
        return {"message":f"The post with id {vote.post_id} is added to your liked list"}

    else:
        if not found_vote:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The {vote.post_id} is not in your liked list.")
        vote_query.delete(synchronize_session=False)
        db.commit()
        return {"Message":"Succesfully removed the post from your liked list"}
