from admin_app import db


class FavoriteLocation(db.Model):
    __tablename__ = 'locations_favorites'
    user_id = db.Column(db.Integer())
    location_id = db.Column(db.Integer())
    created_at = db.Column(db.DateTime(), nullable=False, default=db.func.current_timestamp())
    __table_args__ = (
        db.PrimaryKeyConstraint(
            user_id, location_id,
        ),
    )

    @property
    def serialize(self):
        row = {}
        for c in self.__table__.columns:
            row[c.name] = getattr(self, c.name)
        return row


class Location(db.Model):
    __tablename__ = 'locations'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    address = db.Column(db.Text(), nullable=True, default=None)
    user_id = db.Column(db.Integer(), nullable=False)
    lat = db.Column(db.Float(), nullable=False, index=True)
    lon = db.Column(db.Float(), nullable=False, index=True)
    created_at = db.Column(db.DateTime(), nullable=False, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime(), nullable=False, default=db.func.current_timestamp(),
                           onupdate=db.func.current_timestamp())

    @property
    def serialize(self):
        row = {}
        for c in self.__table__.columns:
            row[c.name] = getattr(self, c.name)
        return row


class LocationRecommend(db.Model):
    __tablename__ = 'locations_recommend'
    user_id = db.Column(db.Integer())
    location_id = db.Column(db.Integer())
    created_at = db.Column(db.DateTime(), nullable=False, default=db.func.current_timestamp())
    __table_args__ = (
        db.PrimaryKeyConstraint(
            user_id, location_id,
        ),
    )

    @property
    def serialize(self):
        row = {}
        for c in self.__table__.columns:
            row[c.name] = getattr(self, c.name)
        return row


class LocationShare(db.Model):
    __tablename__ = 'locations_share'
    user_id = db.Column(db.Integer())
    location_id = db.Column(db.Integer())
    created_at = db.Column(db.DateTime(), nullable=False, default=db.func.current_timestamp())
    __table_args__ = (
        db.PrimaryKeyConstraint(
            user_id, location_id,
        ),
    )

    @property
    def serialize(self):
        row = {}
        for c in self.__table__.columns:
            row[c.name] = getattr(self, c.name)
        return row
