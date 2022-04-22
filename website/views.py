from flask import Blueprint, render_template, request, flash, redirect, url_for, Response, Flask
from flask_login import login_required, current_user
from .models import Post, User, Comment
from . import db
import prometheus_client
from prometheus_client.core import CollectorRegistry
from prometheus_client import Summary, Counter, Histogram, Gauge
import time
views = Blueprint("views", __name__)

_INF = float("inf")

graphs = {}
graphs['c'] = Counter("python_request_operation_total", "The total number of processed request ")
graphs['h'] = Histogram("python_request_duration_seconds", "Histogram for the duration in seconds", buckets=(1,2,5,6,10, _INF))


@views.route("/")
@views.route("/home")
@login_required
def home():
    posts = Post.query.all()
    start = time.time()
    graphs['c'].inc()

    time.sleep(0.600)
    end = time.time()
    graphs['h'].observe(end - start)
    return render_template("home.html", user=current_user, posts=posts)


@views.route("/create-post", methods=['GET', 'POST'])
@login_required
def create_post():
    start = time.time()
    graphs['c'].inc()

    time.sleep(0.600)
    end = time.time()
    graphs['h'].observe(end - start)
    if request.method == "POST":
        text = request.form.get('text')


        if not text:
            flash('Wpis nie może być pusty', category='error')
        else:
            post = Post(text=text, author=current_user.id)
            db.session.add(post)
            db.session.commit()
            flash('Wpis utworzony!', category='success')
            

            return redirect(url_for('views.home'))

    return render_template('create_post.html', user=current_user)


@views.route("/delete-post/<id>")
@login_required
def delete_post(id):
    post = Post.query.filter_by(id=id).first()

    if not post:
        flash("Wpis nie istnieje.", category='error')
    elif current_user.id != post.id:
        flash('Nie masz uprawnień, aby usunąć ten wpis.', category='error')
    else:
        db.session.delete(post)
        db.session.commit()
        flash('Wpis usunięty.', category='success')

    return redirect(url_for('views.home'))


@views.route("/posts/<username>")
@login_required
def posts(username):
    user = User.query.filter_by(username=username).first()

    if not user:
        flash('Nie istnieje użytkownik o tej nazwie.', category='error')
        return redirect(url_for('views.home'))

    posts = user.posts
    return render_template("posts.html", user=current_user, posts=posts, username=username)


@views.route("/create-comment/<post_id>", methods=['POST'])
@login_required
def create_comment(post_id):
    text = request.form.get('text')

    if not text:
        flash('Komentarz nie może być pusty.', category = 'error')
    else:
        post = Post.query.filter_by(id=post_id)
        if post:
            comment = Comment(text=text, author=current_user.id, post_id=post_id)
            db.session.add(comment)
            db.session.commit()
        else:
            flash('Wpis nie istnieje.', category='error')


    return redirect(url_for('views.home'))

@views.route("/delete-comment/<comment_id>")
@login_required
def delete_comment(comment_id):
    comment = Comment.query.filter_by(id=comment_id).first()

    if not comment:
        flash('Komentarz nie istnieje', category='error')
    elif current_user.id != comment.author and current_user.id != comment.post.author:
        flash('Brak uprawnień, aby wykonać tę operację.', category='error')
    else:
        db.session.delete(comment)
        db.session.commit()

    return redirect(url_for('views.home'))


@views.route("/metrics")
def request_count():
    res = []
    for k,v in graphs.items():
        res.append(prometheus_client.generate_latest(v))
    return Response(res, mimetype="text/plain")
