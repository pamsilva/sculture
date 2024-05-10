from pydantic import BaseModel
from datetime import datetime


class User(BaseModel):
    name: str
    apiKey: str


class Post(BaseModel):
    title: str
    body: str


class Feedback(BaseModel):
    postId: int
    positive: bool
