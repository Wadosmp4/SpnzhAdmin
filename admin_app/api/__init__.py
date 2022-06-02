import jwt
import logging
import datetime
from flask import Blueprint, request

from admin_app import login_manager
from admin_app.models.user_models import User
from admin_app.auth.controllers import UserTokenController
from admin_app.auth.errors import ValidHeaderTokenMissingException, TokenIsInvalidException
from admin_app.utils import wrap_response
from admin_app import app


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__file__)

url_prefix = '/api/v1'
api_init = Blueprint('api_init', __name__, url_prefix=url_prefix)


@app.before_request
def get_request_host():
    app.config['APP_DOMAIN'] = request.host_url.strip('/')


@login_manager.request_loader
def load_user_from_request(request):
    api_key = request.headers.get('x-access-tokens')
    data = None
    if api_key:
        try:
            data = jwt.decode(api_key, app.config['SECRET_KEY'], 'HS256')
        except BaseException:
            return None
        try:
            user = User.query.filter_by(id=data['id']).first()
        except BaseException:
            return None
        if user:
            token = UserTokenController().get_by_user_id(user.id)
            if token and token.access_expired_at > datetime.datetime.utcnow():
                return user
            else:
                return None
    return None


@login_manager.unauthorized_handler
def token_required_message():
    api_key = request.headers.get('x-access-tokens')
    if api_key:
        return wrap_response(TokenIsInvalidException().__format__(), errors=True)
    return wrap_response(ValidHeaderTokenMissingException().__format__(), errors=True)
