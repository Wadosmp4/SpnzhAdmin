from admin_app.models.user_models import Friend, UserFollower
from admin_app.models.invite_model import Invite
from admin_app.models.group_models import GroupFollower

from flask_sqlalchemy import models_committed
from admin_app.utils import send_api_request, ADD_NOTIFICATION_URL


def send_notif_after_creating(sender, changes):
    for target, operation in changes:
        if isinstance(target, Friend) and operation == 'insert':
            send_api_request(ADD_NOTIFICATION_URL,
                             {'type_event': 'add_friend_user',
                              'user_id': target.user_id,
                              'friend_user_id': target.friend_user_id})
        elif isinstance(target, Invite) and operation == 'insert':
            if target.obj_type == 'group':
                send_api_request(ADD_NOTIFICATION_URL,
                                 {'type_event': 'invite_to_group',
                                  'user_ids': [target.user_id],
                                  'group_id': target.obj_id})
            elif target.obj_type == 'event':
                send_api_request(ADD_NOTIFICATION_URL,
                                 {'type_event': 'invite_to_event',
                                  'user_ids': [target.user_id],
                                  'article_id': target.obj_id})
        elif isinstance(target, GroupFollower) and operation == 'insert':
            send_api_request(ADD_NOTIFICATION_URL,
                             {'type_event': 'new_group_member',
                              'user_id': target.user_id,
                              'group_id': target.group_id_follow})
        elif isinstance(target, UserFollower) and operation == 'insert':
            send_api_request(ADD_NOTIFICATION_URL,
                             {'type_event': 'add_follow_user',
                              'user_id': target.user_id,
                              'follow_user_id': target.user_id_follow})


def init_signals(app):
    models_committed.connect(send_notif_after_creating, app)
