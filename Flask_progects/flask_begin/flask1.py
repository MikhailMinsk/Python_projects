# веб-сервер Werkzoug, работает с протоколом WSGI и лежит в основе Flask

# 1. По адресу /locales должен возвращаться массив в формате json с тремя локалями: ['ru', 'en', 'it']
# 2. По адресу /sum/<int:first>/<int:second> должен получать в url-адресе два числа, возвращать их сумму
# 3. По адресу /greet/<user_name> должен получать имя пользователя, возвращать текст 'Hello, имя_которое_прислали'
# 4. По адресу /form/user должен принимать POST запрос с параментрами: email, пароль и подтверждение пароля.
# Необходимо валидировать email, что обязательно присутствует, валидировать пароли, что они минимум 6 символов
# в длину и совпадают. Возрващать пользователю json вида:
#  "status" - 0 или 1 (если ошибка валидации),
#  "errors" - список ошибок, если они есть,
#  или пустой список.
# 5. По адресу /serve/<path:filename> должен возвращать содержимое запрашиваемого файла из папки ./files.
# Файлы можно туда положить любые текстовые. А если такого нет - 404.

import config1
from flask import Flask, request
from flask.json import jsonify
from flask_wtf import FlaskForm
from wtforms import StringField, validators, ValidationError

app = Flask(__name__)
app.config.from_object(config1)


@app.route('/')
def home():
    return 'hello world'


@app.route('/test')
def home2():
    return 'hello , user'


@app.route('/hello/<user>')
def home3(user):
    return 'hello , user : ' + user


@app.route('/locales')
def home4():
    dict_ = {'ru': 'russian', 'en': 'english', 'it': 'italian'}
    return jsonify(dict_)


@app.route('/strings/<str1>/<str2>/<str3>')
def strings(str1, str2, str3):
    if len(str1) < len(str2) < len(str3):
        return str3
    elif len(str2) < len(str3) < len(str1):
        return str1
    else:
        return str2


@app.route('/sum/<first>/<second>')
def sum_(first, second):
    return str(int(first) + int(second))
    # return 'sum = {}'.format(first + second)


@app.route('/serve/<path:filename>', methods=['GET', 'POST'])
def path_file(filename):
    from os import path
    if not path.exists('./files/' + filename):
        return '404: File doesnt exist'
    else:
        with open('./files/' + filename) as f:
            text = f.read()
    return text


#  _________________________________________________________________

# def confirm_pas(form,field):
#     # print(form.data['password']==form.data['confirm_pass'])
#     # print(form.data['confirm_pass'])
#     # print(form.data['password'])
#
#     if form.data['password'] != form.data['confirm_pass']:
#         raise ValidationError('Error password')
#     else:
#         print('ok')


class NewForm(FlaskForm):
    email = StringField(validators=[
        validators.Length(min=5, max=35),
        validators.Email()
    ])
    password = StringField(label='pass:', validators=[
        validators.Length(min=3, max=12)
    ])
    password2 = StringField(label='confirm pass:', validators=[
        validators.Length(min=3, max=12),
        validators.equal_to('password', message='Wrong')
        # confirm_pas
    ])


@app.route('/form/user', methods=['GET', 'POST'])
def func_get_post():
    if request.method == 'POST':
        output = {0: 'Its OK', 1: 'Error'}
        print(request.form)
        user_form = NewForm(request.form)
        print(user_form.validate())
        if user_form.validate():
            return jsonify(output[0])
        else:
            print(user_form.errors)
            return jsonify(output[1], user_form.errors)

    return 'Hello user!'


if __name__ == '__main__':
    app.run()
