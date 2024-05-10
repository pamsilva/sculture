from sculture.schemas import User, Post, Feedback
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

    
def add_post(post: Post, user: User):
    new_post = SPost(**post.dict(), authorId=user.userId)
    
    db = get_db()
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post
    
def add_feedback(feedback: Feedback, post: Post):
    feedback = SFeedback(**feedback.dict(), postId=post.postId)
    
    db = get_db()
    db.add(feedback)
    db.commit()
    db.refresh(feedback)
    return feedback
