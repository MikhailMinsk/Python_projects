from flask import Flask, render_template

app = Flask(__name__)

# TODO: to add logic to the initial form

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/registration')
def registration():
    return render_template('registration.html')


@app.route('/search')
def search():
    return render_template('search.html')


@app.route('/contacts')
def contacts():
    return render_template('contacts.html')


@app.route('/post')
def post():
    return render_template('post.html')


if __name__ == '__main__':
    app.run()
