from flask import flash
from flask_admin.contrib.sqla import ModelView
from flask_admin.babel import gettext

from admin_app import db


class BaseAdmin(ModelView):
    page_size = 10

    # def is_accessible(self):
    #     return current_user.is_admin()

    def create_model(self, form):
        data = form.data

        try:
            user_settings = self.model(**data)
        except Exception as e:
            flash(gettext(e.__repr__()), 'error')
            return False

        db.session.add(user_settings)
        db.session.commit()
        return True
