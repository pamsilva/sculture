from fastapi import Header, FastAPI, HTTPException, Depends

from sculture.schemas import User, Post
from sculture.data.interface import add_user, add_post, add_feedback, get_user

fake_users_db = {}


def get_current_user(apiKey: str = Header(...), userId: int = Header(...)):
    user = get_user(userId)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    if user.active == False:
        raise HTTPException(status_code=400, detail="Inactive user")
    
    return user


def create_user(user: User):
    user = add_user({
        **user.dict(),
        "active": True,
    })
    return user


def create_post(post: Post, current_user: User):
    new_post = {
        **post.dict(),
        "authorId": current_user.userId,
        "created": datetime.utcnow(),
        "active": True,
    }
    new_post = add_post(post, current_user)
    return new_post


def get_latest_n_posts(n: int):
    # get latest n posts
    return []


def feedback_post(post: Post, positive: bool, current_user: User):
    new_feedback = {
        "postId": post.postId,
        "positive": positive
    }
    return add_feedback(new_feedback, current_user)
