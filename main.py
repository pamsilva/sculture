from fastapi import FastAPI, HTTPException, Depends
from typing import List

from sculture.schemas import User, Post, Feedback, NewFeedback, NewUser, NewPost
from sculture.logic import create_user, create_post, get_latest_n_posts, feedback_post, get_current_user

app = FastAPI()



# Endpoint to create a user
@app.post("/users/", response_model=User)
async def create_user_endpoint(user: NewUser):
    return create_user(user)


@app.post("/posts/", response_model=Post)
async def create_new_post(post: NewPost, current_user: User = Depends(get_current_user)):
    return create_post(post, current_user)


# get latest posts from any user
@app.get("/posts/", response_model=List[Post])
async def latest_posts():
    return get_latest_n_posts(10)


@app.post("/feedback/", response_model=Feedback)
async def add_feedback(feedback: NewFeedback, current_user: User = Depends(get_current_user)):
    return feedback_post(feedback, current_user)
