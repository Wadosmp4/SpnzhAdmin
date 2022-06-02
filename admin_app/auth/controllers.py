import secrets
import string
from admin_app.auth.models import UserToken, CredentialRequest
from admin_app import db


class UserTokenController:
    db_model = UserToken

    def add_db(self, data):
        obj = self.db_model()
        for d in data:
            if d not in ['id', ]:
                if d in self.db_model.__table__.columns:
                    setattr(obj, d, data[d])
        db.session.add(obj)
        db.session.commit()
        return obj

    def get_by_user_id(self, user_id):
        obj = self.db_model.query.filter(self.db_model.user_id == user_id).first()
        return obj

    def upd_by_user_id(self, user_id, raw):
        pass

    def del_by_user_id(self, user_id):
        token = self.get_by_user_id(user_id)
        if token:
            db.session.delete(token)
            db.session.commit()
        return user_id

    @staticmethod
    def dict_one(obj):
        return obj.serialize

    def check_access_token(self):
        pass


class CredentialRequestController:
    db_model = CredentialRequest

    def add_db(self, data):
        obj = self.db_model()
        for d in data:
            if d not in ['id', ]:
                if d in self.db_model.__table__.columns:
                    setattr(obj, d, data[d])
        db.session.add(obj)
        db.session.commit()
        return obj

    def upd_db(self, obj, raw):
        for r in raw:
            if r not in ['id', ]:
                if hasattr(obj, r):
                    setattr(obj, r, raw[r])
        db.session.commit()
        return obj

    def add_email_changes(self, user_id, email_value, confirm_code):
        data = dict(user_id=user_id,
                    request_type='email',
                    request_value=email_value,
                    confirm_code=confirm_code,
                    status='requested')
        obj = self.add_db(data)
        return obj

    def add_password_changes(self, user_id, passw_value, confirm_code):
        data = dict(user_id=user_id,
                    request_type='passw',
                    request_value=passw_value,
                    confirm_code=confirm_code,
                    status='requested')
        obj = self.add_db(data)
        return obj

    def get_data_changes(self, user_id, confirm_code):
        obj = self.db_model.query.filter_by(user_id=user_id,
                                            status='requested',
                                            confirm_code=confirm_code).first()
        return obj

    @staticmethod
    def create_confirmation_code():
        alphabet = string.ascii_letters + string.digits
        code = ''.join(secrets.choice(alphabet) for i in range(5))
        return code





