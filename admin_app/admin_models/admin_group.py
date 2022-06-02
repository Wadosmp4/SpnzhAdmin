from admin import BaseAdmin
from admin_app import admin, db
from admin_app.models.user_models import User
from admin_app.models.group_models import (Groups, UsersGroups, GroupShare, FavoriteGroup,
                                           GroupFollower, GroupRecommend)

from admin_app.utils import show_message


class GroupAdmin(BaseAdmin):
    column_list = ('id', 'name', 'short_description', 'description', 'creator_user_id',
                   'mode', 'created_at', 'allow_join_request', 'messaging_type')
    form_columns = ('name', 'short_description', 'description', 'creator_user_id',
                    'mode', 'created_at', 'allow_join_request', 'messaging_type')

    def create_model(self, form):
        if not User.query.get(form.data['creator_user_id']):
            show_message('Non-existing user id', 'error')
            return False
        return super().create_model(form)

    def update_model(self, form, model):
        if not User.query.get(form.data['creator_user_id']):
            show_message('Non-existing user id', 'error')
            return False
        return super().update_model(form, model)


class UsersGroupsAdmin(BaseAdmin):
    column_list = ('user_id', 'group_id', 'user_status', 'user_role', 'created_at', 'updated_at')
    form_columns = ('user_id', 'group_id', 'user_status', 'user_role', 'created_at', 'updated_at')

    def create_model(self, form):
        if (not User.query.get(form.data['user_id'])
                or not Groups.query.get(form.data['group_id'])):
            show_message('Non-existing user or group id', 'error')
            return False
        return super().create_model(form)

    def update_model(self, form, model):
        if (not User.query.get(form.data['user_id'])
                or not Groups.query.get(form.data['group_id'])):
            show_message('Non-existing user or group id', 'error')
            return False
        return super().update_model(form, model)


class GroupShareAdmin(BaseAdmin):
    column_list = ('user_id', 'group_id', 'created_at')
    form_columns = ('user_id', 'group_id', 'created_at')

    def create_model(self, form):
        if (not User.query.get(form.data['user_id'])
                or not Groups.query.get(form.data['group_id'])):
            show_message('Non-existing user or group id', 'error')
            return False
        return super().create_model(form)

    def update_model(self, form, model):
        if (not User.query.get(form.data['user_id'])
                or not Groups.query.get(form.data['group_id'])):
            show_message('Non-existing user or group id', 'error')
            return False
        return super().update_model(form, model)


class GroupFollowerAdmin(BaseAdmin):
    column_list = ('user_id', 'group_id_follow', 'status', 'created_at')
    form_columns = ('user_id', 'group_id_follow', 'status', 'created_at')

    def create_model(self, form):
        if (not User.query.get(form.data['user_id'])
                or not Groups.query.get(form.data['group_id_follow'])):
            show_message('Non-existing user or group id', 'error')
            return False
        return super().create_model(form)

    def update_model(self, form, model):
        if (not User.query.get(form.data['user_id'])
                or not Groups.query.get(form.data['group_id_follow'])):
            show_message('Non-existing user or group id', 'error')
            return False
        return super().update_model(form, model)


def init_group_admin():
    admin.add_view(GroupAdmin(Groups, db.session, category='Groups'))
    admin.add_view(UsersGroupsAdmin(UsersGroups, db.session, category='Groups'))
    admin.add_view(GroupShareAdmin(GroupShare, db.session, category='Groups'))
    admin.add_view(GroupShareAdmin(FavoriteGroup, db.session, category='Groups'))
    admin.add_view(GroupShareAdmin(GroupRecommend, db.session, category='Groups'))
    admin.add_view(GroupFollowerAdmin(GroupFollower, db.session, category='Groups'))
