from pydantic import BaseModel
from datetime import datetime


class User(BaseModel):
    userId: int
    name: str
    active: bool
    apiKey: str


class Post(BaseModel):
    postId: int
    authorId: int
    created: datetime
    title: str
    body: str
    active: bool


class Feedback(BaseModel):
    feedbackId: int
    postId: int
    positive: bool
