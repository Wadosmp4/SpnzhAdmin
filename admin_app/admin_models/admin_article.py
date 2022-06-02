from admin import BaseAdmin
from admin_app import admin, db
from admin_app.models.user_models import User
from admin_app.models.group_models import Groups
from admin_app.models.article_models import (Article, ArticlesGroups, ArticlesLikes,
                                             ArticlesUsers, ArticlesViews, ArticlesShares)

from admin_app.utils import show_message


class ArticleAdmin(BaseAdmin):
    column_list = ('id', 'name', 'description', 'datetime', 'user_id', 'type', 'time_visible',
                   'lat', 'lon', 'image_link', 'video_link', 'video_image_link', 'sound_link',
                   'mode', 'views_count', 'tags', 'place', 'phone', 'email', 'site', 'event_datetime',
                   'tickets', 'group_id', 'sound_duration', 'time_delay')
    form_columns = ('name', 'description', 'datetime', 'user_id', 'type', 'time_visible',
                    'lat', 'lon', 'image_link', 'video_link', 'video_image_link', 'sound_link',
                    'mode', 'views_count', 'tags', 'place', 'phone', 'email', 'site', 'event_datetime',
                    'tickets', 'group_id', 'sound_duration', 'time_delay')

    def create_model(self, form):
        if (not User.query.get(form.data['user_id'])
                or (form.data['group_id'] and not Groups.query.get(form.data['group_id']))):
            show_message('Non-existing user or group id', 'error')
            return False
        return super().create_model(form)

    def update_model(self, form, model):
        if (not User.query.get(form.data['user_id'])
                or (form.data['group_id'] and not Groups.query.get(form.data['group_id']))):
            show_message('Non-existing user or group id', 'error')
            return False
        return super().update_model(form, model)


class ArticlesGroupsAdmin(BaseAdmin):
    column_list = ('article_id', 'group_id', 'created_at')
    form_columns = ('article_id', 'group_id', 'created_at')

    def create_model(self, form):
        if (not Article.query.get(form.data['article_id'])
                or not Groups.query.get(form.data['group_id'])):
            show_message('Non-existing article or group id', 'error')
            return False
        return super().create_model(form)

    def update_model(self, form, model):
        if (not Article.query.get(form.data['article_id'])
                or not Groups.query.get(form.data['group_id'])):
            show_message('Non-existing article or group id', 'error')
            return False
        return super().update_model(form, model)


# class ArticlesUsersAdmin(BaseAdmin):
#     column_list = ('article_id', 'user_id', 'created_at')
#     form_columns = ('article_id', 'user_id', 'created_at')
#
#     def create_model(self, form):
#         if (not Article.query.get(form.data['article_id'])
#                 or not User.query.get(form.data['user_id'])):
#             flash(gettext('Non-existing article or group id'), 'error')
#             return False
#
#         return super().create_model(form)
#
#     def update_model(self, form, model):
#         if (not Article.query.get(form.data['article_id'])
#                 or not User.query.get(form.data['user_id'])):
#             flash(gettext('Non-existing article or group id'), 'error')
#             return False
#
#         return super().update_model(form, model)


class ArticlesLikesAdmin(BaseAdmin):
    column_list = ('id', 'user_id', 'article_id', 'like_type', 'datetime')
    form_columns = ('user_id', 'article_id', 'like_type', 'datetime')

    def create_model(self, form):
        if (not Article.query.get(form.data['article_id'])
                or not User.query.get(form.data['user_id'])):
            show_message('Non-existing article or user id', 'error')
            return False
        return super().create_model(form)

    def update_model(self, form, model):
        if (not Article.query.get(form.data['article_id'])
                or not User.query.get(form.data['user_id'])):
            show_message('Non-existing article or user id', 'error')
            return False
        return super().update_model(form, model)


class ArticlesViewsAdmin(BaseAdmin):
    column_list = ('article_id', 'user_id', 'created_at')
    form_columns = ('article_id', 'user_id', 'created_at')

    def create_model(self, form):
        if (not Article.query.get(form.data['article_id'])
                or not User.query.get(form.data['user_id'])):
            show_message('Non-existing article or user id', 'error')
            return False
        return super().create_model(form)

    def update_model(self, form, model):
        if (not Article.query.get(form.data['article_id'])
                or not User.query.get(form.data['user_id'])):
            show_message('Non-existing article or user id', 'error')
            return False
        return super().update_model(form, model)


class ArticlesSharesAdmin(BaseAdmin):
    column_list = ('id', 'user_id', 'article_id', 'user_id_for', 'datetime')
    form_columns = ('user_id', 'article_id', 'user_id_for', 'datetime')

    def create_model(self, form):
        if ((not Article.query.get(form.data['article_id'])
                or not User.query.get(form.data['user_id'])
                or not User.query.get(form.data['user_id_for']))
                or form.data['user_id'] == form.data['user_id_for']):
            show_message('Non-existing article or user id', 'error')
            return False
        return super().create_model(form)

    def update_model(self, form, model):
        if ((not Article.query.get(form.data['article_id'])
                or not User.query.get(form.data['user_id'])
                or not User.query.get(form.data['user_id_for']))
                or form.data['user_id'] == form.data['user_id_for']):
            show_message('Non-existing article or user id', 'error')
            return False
        return super().update_model(form, model)


def init_article_admin():
    admin.add_view(ArticleAdmin(Article, db.session, category='Article'))
    admin.add_view(ArticlesGroupsAdmin(ArticlesGroups, db.session, category='Article'))
    # admin.add_view(ArticlesUsersAdmin(ArticlesUsers, db.session, category='Article'))
    admin.add_view(ArticlesLikesAdmin(ArticlesLikes, db.session, category='Article'))
    admin.add_view(ArticlesViewsAdmin(ArticlesViews, db.session, category='Article'))
    admin.add_view(ArticlesSharesAdmin(ArticlesShares, db.session, category='Article'))
