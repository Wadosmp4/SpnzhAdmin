from admin import BaseAdmin
from admin_app import admin, db
from admin_app.models.user_models import User
from admin_app.models.article_models import Article
from admin_app.models.group_models import Groups
from admin_app.models.chat_models import Comment, Room, Message, UserRoom, ChatTimeVisit

from admin_app.utils import show_message


class CommentAdmin(BaseAdmin):
    column_list = ('id', 'article_id', 'user_id', 'name', 'email', 'body',
                   'created', 'updated', 'active', 'image_link')
    form_columns = ('article_id', 'user_id', 'name', 'email', 'body',
                    'created', 'updated', 'active', 'image_link')

    def create_model(self, form):
        if (not User.query.get(form.data['user_id'])
                or not Article.query.get(form.data['article_id'])):
            show_message('Non-existing user or article id', 'error')
            return False
        return super().create_model(form)

    def update_model(self, form, model):
        if (not User.query.get(form.data['user_id'])
                or not Article.query.get(form.data['article_id'])):
            show_message('Non-existing user or article id', 'error')
            return False
        return super().update_model(form, model)


class RoomAdmin(BaseAdmin):
    column_list = ('id', 'name', 'display_name', 'type', 'group_id')
    form_columns = ('name', 'display_name', 'type', 'group_id')

    def create_model(self, form):
        if form.data['group_id'] and not Groups.query.get(form.data['group_id']):
            show_message('Non-existing group id', 'error')
            return False
        return super().create_model(form)

    def update_model(self, form, model):
        if form.data['group_id'] and not Groups.query.get(form.data['group_id']):
            show_message('Non-existing group id', 'error')
            return False
        return super().update_model(form, model)


class MessageAdmin(BaseAdmin):
    column_list = ('id', 'sender_id', 'sender_username', 'room_id', 'created_at', 'content', 'message_type')
    form_columns = ('sender_id', 'sender_username', 'room_id', 'created_at', 'content', 'message_type')

    def create_model(self, form):
        if (not User.query.get(form.data['sender_id'])
                or not Room.query.get(form.data['room_id'])):
            show_message('Non-existing user or room id', 'error')
            return False
        return super().create_model(form)

    def update_model(self, form, model):
        if (not User.query.get(form.data['sender_id'])
                or not Room.query.get(form.data['room_id'])):
            show_message('Non-existing user or room id', 'error')
            return False
        return super().update_model(form, model)


class UserRoomAdmin(BaseAdmin):
    column_list = ('user_id', 'room_id')
    form_columns = ('user_id', 'room_id')

    def create_model(self, form):
        if (not User.query.get(form.data['user_id'])
                or not Room.query.get(form.data['room_id'])):
            show_message('Non-existing user or room id', 'error')
            return False
        return super().create_model(form)

    def update_model(self, form, model):
        if (not User.query.get(form.data['user_id'])
                or not Room.query.get(form.data['room_id'])):
            show_message('Non-existing user or room id', 'error')
            return False
        return super().update_model(form, model)


def init_chat_admin():
    admin.add_view(CommentAdmin(Comment, db.session, category='Chat'))
    admin.add_view(RoomAdmin(Room, db.session, category='Chat'))
    admin.add_view(MessageAdmin(Message, db.session, category='Chat'))
    admin.add_view(UserRoomAdmin(UserRoom, db.session, category='Chat'))
