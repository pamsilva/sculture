from pydantic import BaseModel
from datetime import datetime


class NewUser(BaseModel):
    name: str
    apiKey: str

    
class User(NewUser):
    userId: int
    active: bool

    
class NewPost(BaseModel):
    title: str
    body: str

    
class Post(NewPost):
    postId: int
    authorId: int
    created: datetime
    active: bool


class NewFeedback(BaseModel):
    postId: int
    positive: bool


class Feedback(NewFeedback):
    feedbackId: int
    postId: intdata
    positive: bool
