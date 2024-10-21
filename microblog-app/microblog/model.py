# class Post:
#     def __init__(self, post_id, user, content, timestamp, answered_to_id=None):
#         self.post_id = post_id
#         self.user = user
#         self.content = content
#         self.timestamp = timestamp
#         self.answered_to_id = answered_to_id


# class User:
#     def __init__(self, user_id, email, name, desc=None):
#         self.user_id = user_id
#         self.email = email
#         self.name = name
#         self.desc = desc
import datetime
from typing import List, Optional

from sqlalchemy import String, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func
import flask_login

from . import db


class User(db.Model, flask_login.UserMixin):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(128), unique=True)
    name: Mapped[str] = mapped_column(String(64))
    password: Mapped[str] = mapped_column(String(256))
    posts: Mapped[List["Post"]] = relationship(back_populates="user")
    desc: Mapped[Optional[str]] = mapped_column(String(512))


class Post(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user: Mapped["User"] = relationship(back_populates="posts")
    text: Mapped[str] = mapped_column(String(512))
    timestamp: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    response_to_id: Mapped[Optional[int]] = mapped_column(ForeignKey("post.id"))
    response_to: Mapped["Post"] = relationship(
        back_populates="responses", remote_side=[id]
    )
    responses: Mapped[List["Post"]] = relationship(
        back_populates="response_to", remote_side=[response_to_id]
    )