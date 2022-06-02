import hashlib

from admin_app import db
from flask_login import UserMixin


class Friend(db.Model):
    __tablename__ = 'friends'
    user_id = db.Column(db.Integer(), primary_key=True)
    friend_user_id = db.Column(db.Integer(), primary_key=True)
    status = db.Column(db.Enum('requested', 'approved', 'blocked', 'rejected'), nullable=False, default='requested')
    created_at = db.Column(db.DateTime(), nullable=False, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime(), nullable=False, default=db.func.current_timestamp(),
                           onupdate=db.func.current_timestamp())
    blocked_by = db.Column(db.Integer(), nullable=True, default=None)

    @property
    def serialize(self):
        row = {}
        for c in self.__table__.columns:
            row[c.name] = getattr(self, c.name)
        return row


class Profile(db.Model):
    __tablename__ = 'fts_user_profile'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer(), nullable=False, index=True)
    address = db.Column(db.UnicodeText(), nullable=False, default='')
    phone = db.Column(db.String(50), nullable=False, default='')
    skype = db.Column(db.String(50), nullable=False, default='')
    work_info = db.Column(db.String(200), nullable=False, default='')
    app_settings = db.Column(db.JSON(), nullable=True, default=None)
    last_lon = db.Column(db.Float(), nullable=True, default=None)
    last_lat = db.Column(db.Float(), nullable=True, default=None)

    @property
    def serialize(self):
        row = {}
        for c in self.__table__.columns:
            if c.name == 'id':
                row['user_profile_id'] = getattr(self, c.name)
            else:
                row[c.name] = getattr(self, c.name)
        return row


class UserDevice(db.Model):
    __tablename__ = 'fts_user_devices'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer(), nullable=False)
    device_token = db.Column(db.Unicode(200), nullable=False, server_default=u'', unique=True)
    is_sandbox = db.Column(db.Integer(), nullable=False, default=0)
    status = db.Column(db.Integer(), nullable=False, default=1)
    mobile_os = db.Column(db.Integer(), nullable=False, default=0)
    info = db.Column(db.Text(), nullable=False, server_default=u'', default='')
    datetime = db.Column(db.DateTime(timezone=False), default=db.func.current_timestamp())

    @property
    def serialize(self):
        row = {}
        for c in self.__table__.columns:
            row[c.name] = getattr(self, c.name)
        return row


class UserFollower(db.Model):
    __tablename__ = 'users_followers'
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), nullable=False)
    user_id_follow = db.Column(db.Integer(), nullable=False)
    datetime = db.Column(db.DateTime(), nullable=False, default=db.func.current_timestamp())

    @property
    def serialize(self):
        row = {}
        for c in self.__table__.columns:
            row[c.name] = getattr(self, c.name)
        return row


class User(db.Model, UserMixin):
    __tablename__ = 'fts_users'
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.Unicode(50), nullable=False, server_default=u'', unique=True)
    first_name = db.Column(db.Unicode(100), nullable=True, server_default=None)
    last_name = db.Column(db.Unicode(100), nullable=True, server_default=None)
    display_name = db.Column(db.Unicode(100), nullable=True, server_default=None)
    email = db.Column(db.Unicode(100), nullable=False, server_default=u'', unique=True)
    description = db.Column(db.UnicodeText(), nullable=False, default='', server_default=u'')
    password = db.Column(db.String(100), nullable=True, server_default=None)
    type = db.Column(db.String(50), nullable=False, default=5)
    logged_by = db.Column(db.Integer(), nullable=False, default=0)  # 0 - user_name, 1 - Facebook, 2 - Apple ID, 3 - Google
    uid = db.Column(db.String(100), nullable=False, default='', server_default=u'', unique=True)
    reg_date = db.Column(db.DateTime(timezone=False), default=db.func.current_timestamp())
    birth_date = db.Column(db.Date(), nullable=True, server_default=None)
    show_city = db.Column(db.Boolean, default=True)
    show_account = db.Column(db.Boolean, default=False)
    uuid = db.Column(db.String(200), nullable=False, default='', server_default=u'')  # , unique=True

    def check_password_correction(self, attempted_password):
        return hashlib.md5(attempted_password.encode('utf-8')).hexdigest() == self.password

    def check_email_correction(self, attempted_email):
        return attempted_email == self.email

    @property
    def serialize(self):
        row = {}
        for c in self.__table__.columns:
            if c.name in ('reg_date', ):
                row[c.name] = getattr(self, c.name).strftime('%Y-%m-%d')
            # elif c.name in ('password', 'logged_by'):
            #     pass
            else:
                row[c.name] = getattr(self, c.name)
        return row


class UserRecommend(db.Model):
    __tablename__ = 'users_recommend'
    user_id = db.Column(db.Integer())
    recommend_user_id = db.Column(db.Integer())
    created_at = db.Column(db.DateTime(), nullable=False, default=db.func.current_timestamp())

    __table_args__ = (
        db.PrimaryKeyConstraint(
            user_id, recommend_user_id,
        ),
    )

    @property
    def serialize(self):
        row = {}
        for c in self.__table__.columns:
            row[c.name] = getattr(self, c.name)
        return row


class UserSettings(db.Model):
    __tablename__ = 'user_settings'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False, index=True)
    notif_following = db.Column(db.Boolean(), nullable=False, server_default='0')
    notif_friends = db.Column(db.Boolean(), nullable=False, server_default='0')
    notif_followers = db.Column(db.Boolean(), nullable=False, server_default='0')
    notif_my_locations = db.Column(db.Boolean(), nullable=False, server_default='0')
    notif_my_groups = db.Column(db.Boolean(), nullable=False, server_default='0')
    notif_around_me = db.Column(db.Boolean(), nullable=False, server_default='0')
    around_radius = db.Column(db.Integer, nullable=False, default=100)
    quick_post_1 = db.Column(db.String(50), nullable=False, default='')
    quick_post_2 = db.Column(db.String(50), nullable=False, default='')
    map_style = db.Column(db.String(50), nullable=False, default='')
    time_format = db.Column(db.String(20), nullable=False, default='')
    measurements = db.Column(db.String(20), nullable=False, default='')

    @property
    def serialize(self):
        row = {}
        for c in self.__table__.columns:
            row[c.name] = getattr(self, c.name)
        return row
