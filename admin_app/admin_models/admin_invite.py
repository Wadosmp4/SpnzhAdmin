from admin import BaseAdmin
from admin_app import admin, db
from admin_app.models.user_models import User
from admin_app.models.invite_model import Invite

from admin_app.utils import show_message


class InviteAdmin(BaseAdmin):
    model_to_create = Invite
    column_list = ('id', 'user_id', 'obj_id', 'obj_type', 'status', 'created_at', 'updated_at')
    form_columns = ('user_id', 'obj_id', 'obj_type', 'status', 'created_at', 'updated_at')

    def create_model(self, form):
        if not User.query.get(form.data['user_id']):
            show_message('Non-existing user id', 'error')
            return False
        return super().create_model(form)

    def update_model(self, form, model):
        if not User.query.get(form.data['user_id']):
            show_message('Non-existing user id', 'error')
            return False
        return super().update_model(form, model)


def init_invite_admin():
    admin.add_view(InviteAdmin(Invite, db.session, category='Invite'))
