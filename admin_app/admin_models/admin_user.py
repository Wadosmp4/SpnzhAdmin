from admin import BaseAdmin
from admin_app import admin, db
from admin_app.models.user_models import (User, UserSettings, UserRecommend, Friend,
                                          Profile, UserDevice, UserFollower)

from admin_app.utils import send_api_request, REGISTER_USER_SPNZH_LINK, show_message


class UserAdmin(BaseAdmin):
    column_list = ('id', 'user_name', 'first_name', 'last_name', 'email', 'description')
    form_columns = ("user_name", "email", "first_name", "last_name",
                    "password", "birth_date", "show_city", "show_account")

    def create_model(self, form):
        data = form.data

        result = send_api_request(REGISTER_USER_SPNZH_LINK, data)

        if not result:
            return False
        return True


class UserSettingsAdmin(BaseAdmin):
    column_list = ('user_id', 'notif_following', 'notif_friends', 'notif_followers', 'notif_my_locations',
                   'notif_my_groups', 'notif_around_me', 'around_radius', 'quick_post_1', 'quick_post_2',
                   'map_style', 'time_format', 'measurements')
    form_columns = ('user_id', 'notif_following', 'notif_friends', 'notif_followers', 'notif_my_locations',
                    'notif_my_groups', 'notif_around_me', 'around_radius', 'quick_post_1', 'quick_post_2',
                    'map_style', 'time_format', 'measurements')

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


class UserRecommendAdmin(BaseAdmin):
    column_list = ('user_id', 'recommend_user_id', 'created_at')
    form_columns = ('user_id', 'recommend_user_id', 'created_at')

    def create_model(self, form):
        if (not User.query.get(form.data['user_id'])
                or not User.query.get(form.data['recommend_user_id'])):
            show_message('Non-existing user id', 'error')
            return False
        return super().create_model(form)

    def update_model(self, form, model):
        if (not User.query.get(form.data['user_id'])
                or not User.query.get(form.data['recommend_user_id'])):
            show_message('Non-existing user id', 'error')
            return False
        return super().update_model(form, model)


class FriendAdmin(BaseAdmin):
    column_list = ('user_id', 'friend_user_id', 'status', 'created_at', 'updated_at', 'blocked_by')
    form_columns = ('user_id', 'friend_user_id', 'status', 'created_at', 'updated_at', 'blocked_by')

    def create_model(self, form):
        if (form.data['friend_user_id'] == form.data['user_id']
                or not User.query.get(form.data['friend_user_id'])
                or not User.query.get(form.data['user_id'])):
            show_message('Non-existing user id', 'error')
            return False
        return super().create_model(form)

    def update_model(self, form, model):
        if (not User.query.get(form.data['user_id'])
                or not User.query.get(form.data['recommend_user_id'])):
            show_message('Non-existing user id', 'error')
            return False
        return super().update_model(form, model)


class UserDeviceAdmin(BaseAdmin):
    model_to_create = UserDevice
    column_list = ('user_id', 'device_token', 'is_sandbox', 'status', 'mobile_os', 'info', 'datetime')
    form_columns = ('user_id', 'device_token', 'is_sandbox', 'status', 'mobile_os', 'info', 'datetime')

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


class ProfileAdmin(BaseAdmin):
    column_list = ('user_id', 'address', 'phone', 'skype', 'work_info', 'app_settings', 'last_lon', 'last_lat')
    form_columns = ('user_id', 'address', 'phone', 'skype', 'work_info', 'app_settings', 'last_lon', 'last_lat')

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


class UserFollowerAdmin(BaseAdmin):
    column_list = ('user_id', 'user_id_follow', 'datetime')
    form_columns = ('user_id', 'user_id_follow', 'datetime')

    def create_model(self, form):
        if (form.data['user_id'] == form.data['user_id_follow']
                or not User.query.get(form.data['user_id'])
                or not User.query.get(form.data['user_id_follow'])):
            show_message('Non-existing user id', 'error')
            return False
        return super().create_model(form)

    def update_model(self, form, model):
        if (form.data['user_id'] == form.data['user_id_follow']
                or not User.query.get(form.data['user_id'])
                or not User.query.get(form.data['user_id_follow'])):
            show_message('Non-existing user id', 'error')
            return False
        return super().update_model(form, model)


def init_user_admin():
    admin.add_view(UserAdmin(User, db.session, category='User'))
    admin.add_view(UserSettingsAdmin(UserSettings, db.session, category='User'))
    admin.add_view(UserRecommendAdmin(UserRecommend, db.session, category='User'))
    admin.add_view(FriendAdmin(Friend, db.session, category='User'))
    admin.add_view(UserDeviceAdmin(UserDevice, db.session, category='User'))
    admin.add_view(ProfileAdmin(Profile, db.session, category='User'))
    admin.add_view(UserFollowerAdmin(UserFollower, db.session, category='User'))
