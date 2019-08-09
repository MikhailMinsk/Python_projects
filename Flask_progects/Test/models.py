import re

from app import db


def slugify(s):
    pattern = r'[^\w+]'
    return re.sub(pattern, '-', s)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(30), nullable=False)
    text = db.Column(db.Text)
    slug = db.Column(db.String(140))

    def __init__(self, *args, **kwargs):
        super(Post, self).__init__(*args, **kwargs)
        self.generate_slug()

    def generate_slug(self):
        if self.title:
            self.slug = slugify(self.title)

    def __repr__(self):
        return '<Post id: {}, title: {}>'.format(self.id, self.title)


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    text = db.Column(db.String, nullable=False)

    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), index=True)
    post = db.relationship(Post, foreign_keys=[post_id, ])

    def __init__(self, *args, **kwargs):
        super(Comment, self).__init__(*args, **kwargs)

    def __repr__(self):
        return '<Post id: {}, text: {}'.format(self.id, self.text)
