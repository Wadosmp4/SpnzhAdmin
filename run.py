from admin_app.admin_models.admin_user import init_user_admin
from admin_app.admin_models.admin_notification import init_notification_admin
from admin_app.admin_models.admin_invite import init_invite_admin
from admin_app.admin_models.admin_location import init_location_admin
from admin_app.admin_models.admin_group import init_group_admin
from admin_app.admin_models.admin_storage import init_storage_admin
from admin_app.admin_models.admin_chat import init_chat_admin
from admin_app.admin_models.admin_article import init_article_admin

from admin_app import app
from admin_app.api import api_init
from admin_app.signals import init_signals

app.register_blueprint(api_init)

init_signals(app)

init_user_admin()
init_notification_admin()
init_invite_admin()
init_location_admin()
init_group_admin()
init_storage_admin()
init_chat_admin()
init_article_admin()

if __name__ == "__main__":
    app.run(debug=True)
