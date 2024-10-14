import datetime
import random
import dateutil.tz

from flask import Blueprint, render_template


from . import model

bp = Blueprint("main", __name__)


@bp.route("/")
def index():
    current_user = model.User(1, "current@example.com", "Current Use")
    user = model.User(2, "mary@example.com", "mary")
    posts = [
        model.Post(
            1, user, "Test post", datetime.datetime.now(dateutil.tz.tzlocal()).strftime('%Y-%m-%d %H:%M')
        ),
        model.Post(
            2, user, "Another post", datetime.datetime.now(dateutil.tz.tzlocal()).strftime('%Y-%m-%d %H:%M')
        ),
        model.Post(
            3, user, "Yet another post", datetime.datetime.now(dateutil.tz.tzlocal()).strftime('%Y-%m-%d %H:%M')
        ),
    ]
    return render_template("main/index.html", posts=posts, current_user=current_user)

@bp.route("/profile_view")
def profile_view():
    current_user = model.User(1, "mary@example.com", "mary", """description (should be limited)
                dslcslcpsel,c;el, iufe weoj wef weoifjwe ijofwej
                we fowojfweoj sfoiwefoijwe oifweoi wefoijwe ijofwejwe j
                w ifew jowhufhuwehou fweihu fwehuoifwehf
                w ef weouf owefouhwefou wefoh weohu fweo joiwejoi """)
    posts = [
        model.Post(
            1, current_user, "Test post", datetime.datetime.now(dateutil.tz.tzlocal()).strftime('%Y-%m-%d %H:%M')
        ),
        model.Post(
            2, current_user, "Another post", datetime.datetime.now(dateutil.tz.tzlocal()).strftime('%Y-%m-%d %H:%M')
        ),
        model.Post(
            3, current_user, "Yet another post", datetime.datetime.now(dateutil.tz.tzlocal()).strftime('%Y-%m-%d %H:%M')
        ),
    ]
    return render_template("main/profile_view.html", posts=posts, current_user=current_user)

@bp.route("/post_view")
def post_view():
    data = makeDummyDataTask5Lab3_1()
    return render_template("main/post_view.html", post=data['main_post'], posts=data['responses'])

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
    