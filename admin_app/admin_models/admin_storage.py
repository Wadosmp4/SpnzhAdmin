from admin import BaseAdmin
from admin_app import admin, db
from admin_app.models.user_models import User
from admin_app.models.filestorage_models import ImageStorage, SoundStorage, VideoStorage

from admin_app.utils import show_message


class StorageAdmin(BaseAdmin):
    column_list = ('id', 'local_url', 'content_type', 'user_id', 'used_for', 'info', 'datetime')
    form_columns = ('local_url', 'content_type', 'user_id', 'used_for', 'info', 'datetime')

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


def init_storage_admin():
    admin.add_view(StorageAdmin(ImageStorage, db.session, category='FileStorage'))
    admin.add_view(StorageAdmin(SoundStorage, db.session, category='FileStorage'))
    admin.add_view(StorageAdmin(VideoStorage, db.session, category='FileStorage'))
