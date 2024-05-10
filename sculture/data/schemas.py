from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    userId = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    active = Column(Boolean)
    apiKey = Column(String, unique=True)

    posts = relationship("Post", back_populates="author")

class Post(Base):
    __tablename__ = 'posts'

    postId = Column(Integer, primary_key=True, index=True)
    authorId = Column(Integer, ForeignKey('users.userId'))
    created = Column(DateTime, default=datetime.utcnow)
    title = Column(String)
    body = Column(String)
    active = Column(Boolean)

    author = relationship("User", back_populates="posts")
    feedback = relationship("Feedback", back_populates="post")

class Feedback(Base):
    __tablename__ = 'feedback'

    feedbackId = Column(Integer, primary_key=True, index=True)
    postId = Column(Integer, ForeignKey('posts.postId'))
    positive = Column(Boolean)

    post = relationship("Post", back_populates="feedback")
