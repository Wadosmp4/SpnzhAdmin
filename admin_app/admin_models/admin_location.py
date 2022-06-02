from admin import BaseAdmin
from admin_app import admin, db
from admin_app.models.user_models import User
from admin_app.models.location_models import Location, FavoriteLocation, LocationShare, LocationRecommend

from admin_app.utils import show_message


class LocationAdmin(BaseAdmin):
    column_list = ('id', 'name', 'address', 'user_id', 'lat', 'lon', 'created_at', 'updated_at')
    form_columns = ('name', 'address', 'user_id', 'lat', 'lon', 'created_at', 'updated_at')

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


class ActionLocationAdmin(BaseAdmin):
    column_list = ('user_id', 'location_id', 'created_at')
    form_columns = ('user_id', 'location_id', 'created_at')

    def create_model(self, form):
        if (not User.query.get(form.data['user_id'])
                or not Location.query.get(form.data['location_id'])):
            show_message('Non-existing user or location id', 'error')
            return False
        return super().create_model(form)

    def update_model(self, form, model):
        if (not User.query.get(form.data['user_id'])
                or not Location.query.get(form.data['location_id'])):
            show_message('Non-existing user or location id', 'error')
            return False
        return super().update_model(form, model)


def init_location_admin():
    admin.add_view(LocationAdmin(Location, db.session, category='Location'))
    admin.add_view(ActionLocationAdmin(LocationShare, db.session, category='Location'))
    admin.add_view(ActionLocationAdmin(FavoriteLocation, db.session, category='Location'))
    admin.add_view(ActionLocationAdmin(LocationRecommend, db.session, category='Location'))
