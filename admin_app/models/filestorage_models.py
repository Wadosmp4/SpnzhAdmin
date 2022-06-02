from admin_app import db


class ImageStorage(db.Model):
    __tablename__ = 'fts_images'
    id = db.Column(db.Integer(), primary_key=True)
    local_url = db.Column(db.String(200), nullable=False, default='')
    content_type = db.Column(db.String(50), nullable=False, default='')
    user_id = db.Column(db.Integer(), nullable=False)
    used_for = db.Column(db.String(50), nullable=False, default='')
    info = db.Column(db.Text(), nullable=False, default='')
    datetime = db.Column(db.DateTime(), nullable=False, default=db.func.current_timestamp())

    @property
    def serialize(self):
        row = {}
        for c in self.__table__.columns:
            row[c.name] = getattr(self, c.name)
        return row


class SoundStorage(db.Model):
    __tablename__ = 'sounds'
    id = db.Column(db.Integer(), primary_key=True)
    local_url = db.Column(db.String(200), nullable=False, default='')
    content_type = db.Column(db.String(50), nullable=False, default='')
    user_id = db.Column(db.Integer(), nullable=False)
    used_for = db.Column(db.String(50), nullable=False, default='')
    info = db.Column(db.Text(), nullable=False, default='')
    datetime = db.Column(db.DateTime(), nullable=False, default=db.func.current_timestamp())

    @property
    def serialize(self):
        row = {}
        for c in self.__table__.columns:
            row[c.name] = getattr(self, c.name)
        return row


class VideoStorage(db.Model):
    __tablename__ = 'videos'
    id = db.Column(db.Integer(), primary_key=True)
    local_url = db.Column(db.String(200), nullable=False, default='')
    content_type = db.Column(db.String(50), nullable=False, default='')
    user_id = db.Column(db.Integer(), nullable=False)
    used_for = db.Column(db.String(50), nullable=False, default='')
    info = db.Column(db.Text(), nullable=False, default='')
    datetime = db.Column(db.DateTime(), nullable=False, default=db.func.current_timestamp())

    @property
    def serialize(self):
        row = {}
        for c in self.__table__.columns:
            row[c.name] = getattr(self, c.name)
        return row
