from flask import Flask
from flask import redirect, url_for, request
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_security import SQLAlchemyUserDatastore, Security, current_user
from flask_sqlalchemy import SQLAlchemy

from config import Configure

app = Flask(__name__)
app.config.from_object(Configure)
db = SQLAlchemy(app)

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

from models import *


class AdminMix:
    def is_accessible(self):
        return current_user.has_role('admin')

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('security.login', next=request.url))


# change create in AdminPanel, auto slug
class BaseModelView(ModelView):
    def on_model_change(self, form, model, is_created):
        model.generate_slug()
        return super(BaseModelView, self).on_model_change(form, model, is_created)


class AdminView(AdminMix, ModelView):
    pass


class HomeAdminView(AdminMix, AdminIndexView):
    pass


# view of the create in AdminPanel
class PostAdminView(AdminMix, BaseModelView):
    form_columns = ['title', 'body', 'tags']


class TagAdminView(AdminMix, BaseModelView):
    form_columns = ['name', 'posts']


admin = Admin(app, 'AdminPanel', url='/', index_view=HomeAdminView(name='Home'))
admin.add_view(PostAdminView(Post, db.session))
admin.add_view(TagAdminView(Tag, db.session))

# user and admin

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)
