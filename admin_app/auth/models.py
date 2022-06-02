import datetime
from admin_app import db


class UserToken(db.Model):
    __tablename__ = 'user_token'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer(), nullable=False, index=True)
    access_token = db.Column(db.String(150), nullable=False, default='')
    access_expired_at = db.Column(db.DateTime(timezone=False), default=db.func.current_timestamp() + datetime.timedelta(days=30))
    access_created_at = db.Column(db.DateTime(timezone=False), default=db.func.current_timestamp())

    @property
    def serialize(self):
        row = {}
        for c in self.__table__.columns:
            row[c.name] = getattr(self, c.name)
        return row


class CredentialRequest(db.Model):
    __tablename__ = 'credentials_requests'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer(), nullable=False, index=True)
    request_type = db.Column(db.Enum('passw', 'email', 'notset'), nullable=False, default='notset')
    request_value = db.Column(db.String(200), nullable=False, default='')
    confirm_code = db.Column(db.String(20), nullable=False, default='')
    status = db.Column(db.Enum('requested','confirmed'), nullable=False, default='requested')
    created_at = db.Column(db.DateTime(timezone=False), default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime(), nullable=False, default=db.func.current_timestamp(),
                           onupdate=db.func.current_timestamp())

    @property
    def serialize(self):
        row = {}
        for c in self.__table__.columns:
            row[c.name] = getattr(self, c.name)
        return row
