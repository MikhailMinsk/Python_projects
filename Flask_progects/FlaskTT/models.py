from app import db


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    text = db.Column(db.String(500), nullable=False)

    def __init__(self, *args, **kwargs):
        super(Message, self).__init__(*args, **kwargs)

    def __repr__(self):
        return '<Post id: {}, name: {}, text message: {}>'.format(self.id, self.name, self.text)
