import json
from admin_app import db


class Notification(db.Model):
    __tablename__ = 'notifications'
    id = db.Column(db.Integer(), primary_key=True)
    to_user_id = db.Column(db.Integer(), nullable=False)
    type = db.Column(db.String(20), nullable=False, default='')
    name = db.Column(db.String(100), nullable=False, default='')
    content = db.Column(db.Text(), nullable=False)
    status = db.Column(db.Enum('created', 'sent', 'received'), nullable=False, default='created')
    created_at = db.Column(db.DateTime(timezone=False), default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime(), nullable=False, default=db.func.current_timestamp(),
                           onupdate=db.func.current_timestamp())

    @property
    def serialize(self):
        row = {}
        for c in self.__table__.columns:
            row[c.name] = getattr(self, c.name)
            if c.name == 'content' and row[c.name] != '' and row[c.name] is not None:
                row[c.name] = json.loads(row[c.name])
        return row


class NotificationSubscription(db.Model):
    __tablename__ = 'notifications_subscriptions'
    user_id = db.Column(db.Integer())
    obj_id = db.Column(db.Integer())
    obj_type = db.Column(db.Enum('profile', 'group', 'location'), nullable=False, default='profile')
    created_at = db.Column(db.DateTime(), nullable=False, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime(), nullable=False, default=db.func.current_timestamp(),
                           onupdate=db.func.current_timestamp())

    __table_args__ = (
        db.PrimaryKeyConstraint(
            user_id, obj_id, obj_type,
        ),
    )

    @property
    def serialize(self):
        row = {}
        for c in self.__table__.columns:
            row[c.name] = getattr(self, c.name)
        return row


class NotificationsTimeVisit(db.Model):
    __tablename__ = 'notifications_time_visit'
    user_id = db.Column(db.Integer(), primary_key=True)
    last_visit_time = db.Column(db.DateTime(), nullable=True, default=None)

    @property
    def serialize(self):
        row = {}
        for c in self.__table__.columns:
            row[c.name] = getattr(self, c.name)
        return row


class NotificationViewed(db.Model):
    __tablename__ = 'notifications_viewed'
    notification_id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), nullable=False)
    read_time = db.Column(db.DateTime(), nullable=False, default=db.func.current_timestamp())

    @property
    def serialize(self):
        row = {}
        for c in self.__table__.columns:
            row[c.name] = getattr(self, c.name)
        return row
