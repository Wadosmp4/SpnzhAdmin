import json
import requests
import logging
from flask import jsonify, make_response, flash
from flask_admin.babel import gettext

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__file__)

HEADERS = {'Content-Type': 'application/json'}
ADD_NOTIFICATION_URL = 'http://127.0.0.1:5070/api/v1/notifications/add'
REGISTER_USER_SPNZH_LINK = 'http://127.0.0.1:5065/api/v1/user/register'


def send_api_request(link, request_body):
    try:
        result = requests.post(link, data=json.dumps(request_body, default=str), headers=HEADERS)
    except BaseException as e:
        flash(gettext(e.__repr__()))
        return None

    return result


def show_message(text: str, type: str):
    flash(gettext(text), type)


# def send_notification(notification_request_body):
#     # {'type_event': 'add_friend_user', 'user_id': current_user_id, 'friend_user_id': friend_to_add.friend_user_id}
#     result = requests.post(ADD_NOTIFICATION_URL, data=json.dumps(notification_request_body), headers=HEADERS)
#
#     return result


def wrap_response(data, errors=None):
    body = data
    if not errors:
        return make_response(jsonify({'status': 'true', 'data': body}), 200)
    else:
        return make_response(jsonify({'status': 'false', 'error': body}), 404)
