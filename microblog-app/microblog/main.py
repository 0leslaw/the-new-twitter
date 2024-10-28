import datetime
from os import abort
import random
import dateutil.tz

from flask import Blueprint, render_template, request, redirect, url_for, flash
import flask_login


from . import model
from . import db

bp = Blueprint("main", __name__)


@bp.route("/")
@flask_login.login_required
def index():
    query = db.select(model.Post).order_by(model.Post.timestamp.desc()).limit(10)
    posts = db.session.execute(query).scalars().all()
    
    return render_template("main/index.html", posts=posts, current_user=flask_login.current_user)

@bp.route("/profile_view/<int:user_id>")
@flask_login.login_required
def profile_view(user_id=None):
    if not user_id:
        user = flask_login.current_user        
        posts = user.posts
    else:
        user = db.session.get(model.User, user_id)
        posts = db.session.query(model.Post).filter(model.Post.user_id == user_id).all()
        print(posts)
        print(user)
    return render_template("main/profile_view.html", posts=posts, user=user, is_current=user == flask_login.current_user)

@bp.route("/post_view/<int:post_id>")
@flask_login.login_required
def post_view(post_id):
    post = db.session.get(model.Post, post_id)
    if not post:
        abort(404, "Post id {} doesn't exist.".format(post_id))
    return render_template("main/post_view.html", post=post, posts=post.responses)

@bp.route("/new_post/<int:response_to_id>", methods=["POST"]) 
@bp.route("/new_post", methods=["POST"])
@flask_login.login_required
def new_post(response_to_id=None):
    text = request.form.get("thoughtContent")
    if text:
        post = model.Post(
            response_to=db.session.get(model.Post, response_to_id) if response_to_id else None,
            response_to_id=response_to_id, 
            user=flask_login.current_user, 
            text=text, 
            timestamp=datetime.datetime.now(dateutil.tz.tzlocal())
        )
        db.session.add(post)
        db.session.commit()
        flash("Your post has been published")
        return redirect(url_for("main.post_view", post_id=post.id))
    flash("You need to write something to post")
    return redirect(url_for("main.index"))