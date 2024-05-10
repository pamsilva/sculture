from sculture.schemas import User, Post, NewFeedback
from sculture.data.db import get_db
from sculture.data.schemas import User as SUser
from sculture.data.schemas import Post as SPost
from sculture.data.schemas import Feedback as SFeedback

def add_user(user: User):
    user = SUser(**user)
    
    db = get_db()
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_user(user_id: int):
    db = get_db()
    user = db.query(SUser).filter(SUser.userId == user_id).first()
    return user


def get_post(post_id: int):
    db = get_db()
    post = db.query(SPost).filter(SPost.postId == post_id).first()
    return post


def get_latest_n_posts(n: int):
    db = get_db()
    posts = db.query(SPost).filter(SPost.active == True).order_by(SPost.created.desc()).limit(n).all()
    return posts

    
def add_post(post: dict, user: User):
    new_post = SPost(**post)
    
    db = get_db()
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


def update_post(post: dict):
    db = get_db()
    tpost = db.query(SPost).filter(SPost.postId == post["postId"]).first()
    tpost.title = post["title"]
    tpost.body = post["body"]
    tpost.active = post["active"]
    db.flush()
    db.commit()
    db.refresh(tpost)
    return tpost


def add_feedback(feedback: dict, post: Post):
    feedback = SFeedback(**feedback)
    
    db = get_db()
    db.add(feedback)
    db.commit()
    db.refresh(feedback)
    return feedback
