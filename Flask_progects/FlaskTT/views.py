from app import app, db
from flask import render_template, request, flash, url_for, redirect
from models import Message
from form import MessageForm
from flask.json import jsonify


@app.route('/', methods=['GET'])
def main_page():
    """
    database connection function. sends all messages to the form
    :return: connection with main page
    """
    all_message = Message.query.all()
    return render_template('index.html', messages=all_message)


@app.route('/message', methods=['POST'])
def add_page():
    """
    processes user messages
    :return:connection with main page or error's page
    """
    form = MessageForm(request.form)

    if form.validate():
        try:
            db.session.add(Message(**form.data))
            db.session.commit()
            return redirect(url_for('main_page'))
        except Exception as ex:
            return render_template('errors.html', error=ex)

    return render_template('errors.html', error=jsonify(form.errors))
