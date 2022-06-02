from admin_app import db


class ChatTimeVisit(db.Model):
    __tablename__ = 'chat_time_visit'
    user_id = db.Column(db.Integer())
    room_id = db.Column(db.Integer())
    last_join_time = db.Column(db.DateTime(), nullable=True, default=None)
    last_leave_time = db.Column(db.DateTime(), nullable=True, default=None)
    last_message_id = db.Column(db.Integer(), nullable=True, default=None)
    __table_args__ = (
        db.PrimaryKeyConstraint(
            user_id, room_id,
        ),
    )

    @property
    def serialize(self):
        row = {}
        for c in self.__table__.columns:
            row[c.name] = getattr(self, c.name)
        return row


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer(), primary_key=True)
    article_id = db.Column(db.Integer(), nullable=False)
    user_id = db.Column(db.Integer(), nullable=False)
    name = db.Column(db.String(80), nullable=True, default=None)
    email = db.Column(db.String(100), nullable=True, default=None)
    body = db.Column(db.Text(), nullable=True, default=None)
    created = db.Column(db.DateTime(), nullable=False, default=db.func.current_timestamp())
    updated = db.Column(db.DateTime(), nullable=True, default=None, onupdate=db.func.current_timestamp())
    active = db.Column(db.SmallInteger(), nullable=False, default=1)
    image_link = db.Column(db.String(240), nullable=True, default=None)

    @property
    def serialize(self):
        row = {}
        for c in self.__table__.columns:
            row[c.name] = getattr(self, c.name)
        return row


class Message(db.Model):
    __tablename__ = 'messages'
    id = db.Column(db.Integer(), primary_key=True)
    sender_id = db.Column(db.Integer(), nullable=False)
    sender_username = db.Column(db.String(50), nullable=False)
    room_id = db.Column(db.Integer(), nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False, default=db.func.current_timestamp())
    content = db.Column(db.Text(), nullable=False)
    message_type = db.Column(db.Enum('text', 'location', 'image', 'sound', 'video'), nullable=False, default='text')

    @property
    def serialize(self):
        row = {}
        for c in self.__table__.columns:
            row[c.name] = getattr(self, c.name)
        return row


class Room(db.Model):
    __tablename__ = 'rooms'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    display_name = db.Column(db.String(100), nullable=True, default=None)
    type = db.Column(db.Enum('private', 'public', 'group'), nullable=False, default='private')
    group_id = db.Column(db.Integer(), nullable=True, default=None)

    @property
    def serialize(self):
        row = {}
        for c in self.__table__.columns:
            row[c.name] = getattr(self, c.name)
        return row


class UserRoom(db.Model):
    __tablename__ = 'user_room'
    user_id = db.Column(db.Integer())
    room_id = db.Column(db.Integer())
    __table_args__ = (
        db.PrimaryKeyConstraint(
            user_id, room_id,
        ),
    )

    @property
    def serialize(self):
        row = {}
        for c in self.__table__.columns:
            row[c.name] = getattr(self, c.name)
        return row
