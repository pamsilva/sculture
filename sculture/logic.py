from datetime import datetime
from fastapi import Header, FastAPI, HTTPException, Depends

from sculture.schemas import User, NewPost, Feedback, NewFeedback, NewUser
from sculture.data.interface import add_user, add_post, add_feedback, get_user, get_post, get_latest_n_posts as db_get_latest_n_posts

fake_users_db = {}


def get_current_user(apiKey: str = Header(...), userId: int = Header(...)):
    user = get_user(userId)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    if user.active == False:
        raise HTTPException(status_code=400, detail="Inactive user")
    
    return user


def create_user(user: NewUser):
    user = add_user({
        **user.dict(),
        "active": True,
    })
    return user


def create_post(post: NewPost, current_user: User):
    new_post = {
        **post.dict(),
        "authorId": current_user.userId,
        "created": datetime.utcnow(),
        "active": True,
    }
    new_post = add_post(new_post, current_user)
    return new_post


def get_latest_n_posts(n: int):
    return db_get_latest_n_posts(n)


def feedback_post(feedback: NewFeedback, current_user: User):
    post = get_post(feedback.postId)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    
    return add_feedback(feedback.dict(), current_user)
