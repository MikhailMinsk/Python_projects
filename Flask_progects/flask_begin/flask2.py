# 1.Сделать валидатор для Job
# он принимать только значения IT, Bank, HR
# 2. валидация дня рождения пользователя
# он должен валидироваться с текущим

from time import strftime

from flask import Flask, request
from flask.json import jsonify
from flask_wtf import FlaskForm
from wtforms import StringField, validators, ValidationError

app = Flask(__name__)
app.config.update({
    'SECRET_KEY': 'parolb',
    'DEBUG': True,
    'WTF_CSRF_ENABLED': False
})


def month(form, field):
    if field.data != strftime("%m"):
        raise ValidationError('Your date is bad')


class MyForm(FlaskForm):
    work_ok = ['IT', 'Bank', 'HR']
    work = StringField(label='work', validators=[
        validators.length(min=2, max=4),
        validators.any_of(work_ok, message='Wrong input work !')
    ])
    month = StringField(label='month', validators=[
        validators.length(min=2, max=2),
        month

    ])


@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'GET':
        return 'Hi, stupid user, Im your machine god'
    elif request.method == 'POST':
        print(request.form)
        form = MyForm(request.form)
        print(form.validate())
        if form.validate():
            return 'Ok'
        else:
            return jsonify(form.errors)

    else:
        return 'Something wrong...'


if __name__ == '__main__':
    app.run()
