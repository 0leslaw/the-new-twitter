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
    # current_user = model.User(email="mary@example.com", name="mary")
    user = model.User(email="mary@example.com", name="mary")
    posts = [
        model.Post(user=user, text="Test post", timestamp=datetime.datetime.now(dateutil.tz.tzlocal())),
        model.Post(user=user, text="Another post", timestamp=datetime.datetime.now(dateutil.tz.tzlocal())),
    ]
    return render_template("main/index.html", posts=posts, current_user=flask_login.current_user)

@bp.route("/profile_view")
@flask_login.login_required
def profile_view():
    posts = [
        model.Post(user=flask_login.current_user, text="Test post", timestamp=datetime.datetime.now(dateutil.tz.tzlocal())),
        model.Post(user=flask_login.current_user, text="Another post", timestamp=datetime.datetime.now(dateutil.tz.tzlocal())),
    ]
    return render_template("main/profile_view.html", posts=posts, current_user=flask_login.current_user)

@bp.route("/post_view/<int:post_id>")
@flask_login.login_required
def post_view(post_id):
    post = db.session.get(model.Post, post_id)
    if not post:
        abort(404, "Post id {} doesn't exist.".format(post_id))
    return render_template("main/post_view.html", post=post, posts=post.responses)

@bp.route("/new_post", methods=["POST"])
@flask_login.login_required
def new_post():
    text = request.form.get("thoughtContent")
    if text:
        post = model.Post(user=flask_login.current_user, text=text, timestamp=datetime.datetime.now(dateutil.tz.tzlocal()))
        db.session.add(post)
        db.session.commit()
        flash("Your post has been published")
        return redirect(url_for("main.post_view", post_id=post.id))
    flash("You need to write something to post")
    return redirect(url_for("main.index"))

def makeDummyDataTask5Lab3_1():
    posts = []
    users = []
    lorem = " At vero eos et accusamus et iusto odio dignissimos ducimus, qui blanditiis praesentium voluptatum deleniti atque corrupti, quos dolores et quas molestias"
    ran = random.randint(50, 100)
    for i in range(10):
        users.append(
            model.User(
                i, f"user{i}@gmail.com", f"user{i}", f"user{i}"+lorem[:random.randint(50, 100)]
            )
        )
    for i in range(1,10):
        lor = lorem[:ran]
        posts.append(
            model.Post(
                    i,
                    users[i],
                    f"user{i}"+lorem,
                    datetime.datetime.now(dateutil.tz.tzlocal()).strftime('%Y-%m-%d %H:%M'),
                    0
                )
            )
        ran = random.randint(50, 100)
        
        
    main_post = model.Post(
                    0,
                    users[0],
                    "user0"+lorem[:ran],
                    datetime.datetime.now(dateutil.tz.tzlocal()).strftime('%Y-%m-%d %H:%M')
                )
        
    return {'main_post': main_post, 'responses': posts}
    