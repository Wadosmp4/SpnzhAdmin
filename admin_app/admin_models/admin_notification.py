from admin import BaseAdmin
from admin_app import admin, db
from admin_app.models.user_models import User
from admin_app.models.notification_models import (Notification, NotificationSubscription,
                                                  NotificationViewed, NotificationsTimeVisit)

from admin_app.utils import show_message


class NotificationAdmin(BaseAdmin):
    model_to_create = Notification
    column_list = ('id', 'to_user_id', 'type', 'name', 'content', 'status', 'created_at', 'updated_at')
    form_columns = ('to_user_id', 'type', 'name', 'content', 'status', 'created_at', 'updated_at')

    def create_model(self, form):
        if not User.query.get(form.data['to_user_id']):
            show_message('Non-existing user id', 'error')
            return False
        return super().create_model(form)

    def update_model(self, form, model):
        if not User.query.get(form.data['to_user_id']):
            show_message('Non-existing user id', 'error')
            return False
        return super().update_model(form, model)


class NotificationSubscriptionAdmin(BaseAdmin):
    model_to_create = NotificationSubscription
    column_list = ('user_id', 'obj_id', 'obj_type', 'created_at', 'updated_at')
    form_columns = ('user_id', 'obj_id', 'obj_type', 'created_at', 'updated_at')

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


# non existing table
# class NotificationViewedAdmin(BaseAdmin):
#     model_to_create = NotificationViewed
#     column_list = ('notification_id', 'user_id', 'read_time')
#     form_columns = ('notification_id', 'user_id', 'read_time')
#
#     def create_model(self, form):
#         if (not User.query.get(form.data['user_id'])
#                 or not Notification.query.get(form.data['notification_id'])):
#             flash(gettext('Non-existing user or notification id'), 'error')
#             return False
#
#         return super().create_model(form)


class NotificationsTimeVisitAdmin(BaseAdmin):
    model_to_create = NotificationsTimeVisit
    column_list = ('user_id', 'last_visit_time')
    form_columns = ('user_id', 'last_visit_time')

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


def init_notification_admin():
    admin.add_view(NotificationAdmin(Notification, db.session, category='Notifications'))
    admin.add_view(NotificationSubscriptionAdmin(NotificationSubscription, db.session, category='Notifications'))
    admin.add_view(NotificationsTimeVisitAdmin(NotificationsTimeVisit, db.session, category='Notifications'))
    # admin.add_view(NotificationViewedAdmin(NotificationViewed, db.session))
