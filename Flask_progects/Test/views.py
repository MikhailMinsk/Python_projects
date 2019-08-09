from flask import render_template, request, url_for, redirect

from app import app, db
from models import Post, Comment


@app.route('/')
def main():
    return redirect('main')


@app.route('/main', methods=['GET'])
def all_posts():
    return render_template('index.html', posts=Post.query.all())


@app.route('/new_post', methods=['POST'])
def new_post():
    title = request.form['title']
    text = request.form['text']

    try:
        db.session.add(Post(title=title, text=text))
        db.session.commit()
    except Exception as ex:
        print('Something wrong ', repr(ex))

    return redirect(url_for('main'))


@app.route('/<slug>', methods=['GET'])
def post(slug):
    post = Post.query.filter(Post.slug == slug).first_or_404()
    return render_template('post.html', post=post, comments=Comment.query.filter(Comment.post_id == post.id).all())


@app.route('/<slug>/comment', methods=['POST'])
def comment(slug):
    text = request.form['text']
    post = Post.query.filter(Post.slug == slug).first_or_404()

    try:
        db.session.add(Comment(text=text, post_id=post.id))
        db.session.commit()
    except Exception as ex:
        print('Something wrong ', repr(ex))

    return render_template('post.html', post=post, comments=Comment.query.filter(Comment.post_id == post.id).all())
