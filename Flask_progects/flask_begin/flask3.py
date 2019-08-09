# +1. Пользователь по GET запросу на адрес / получает
# сообщение: "Число загадано"
# 2. Пользователь по POST запросе на адрес /guess
# получает один из следующих результатов: ">", "<", "="
# 3. Если число угадано - загадываем новое число
# 4. Flask при старте сервера - устанавливает seed для
# random, генерирует случайное число для угадывания
# 5. Администратор задает seed для модуля рандом через
# переменную окружения FLASK_RANDOM_SEED

from random import randint

import config1
from flask import Flask, request
from flask_wtf import FlaskForm
from wtforms import IntegerField, validators

app = Flask(__name__)
app.config.from_object(config1)

# app.config.update({
#     'SECRET_KEY': 'parolb',
#     'DEBUG': True,
#     'WTF_CSRF_ENABLED': False
# })


hidden_number = None
counter_win = 0
numb_user = None


def new_numb():
    global hidden_number
    hidden_number = randint(1, 10)
    print('Number from randint: ', hidden_number)


def numb_to_global(form, field):
    global numb_user
    numb_user = field.data
    print('Number from user: ', numb_user)


def func_eq(numb1, numb2):
    global counter_win
    if numb1 == numb2:
        counter_win += 1
        new_numb()
        return 'Greate. You are won {} times . New number is create. Continue'.format(counter_win)
    elif numb1 > numb2:
        return 'Number is greater'
    else:
        return 'Number less'


class NewForm(FlaskForm):
    number = IntegerField(label='number', validators=[
        numb_to_global
    ])


@app.route('/', methods=['GET'])
def home():
    if request.method == "GET":
        new_numb()
        return 'Number made ! Send number to /guess. Number must be integer from 1 to 10'
    else:
        return 'Send number to "/guess"'


@app.route('/guess', methods=['POST'])
def guess():
    global hidden_number, numb_user
    if request.method == "GET":
        return 'Send a number'
    else:
        form = NewForm(request.form)
        if form.validate():
            if hidden_number is None:
                return 'You want to go to "/" and then return to "/guess"'
            else:
                return func_eq(hidden_number, numb_user)
        else:
            return 'Errors: {}'.format(form.errors)


if __name__ == '__main__':
    app.run()
