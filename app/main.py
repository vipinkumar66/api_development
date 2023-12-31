from fastapi import (FastAPI)

from app import models
from app.database import engine
from app.routerss import posts, users, auth, votes

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# THE ROUTER OBJECTS ARE ABLE TO SKIP OUR PATHS INTO
# DIFFERENT FILES AND THAN WE ARE ABLE TO USE THEM
app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(votes.router)