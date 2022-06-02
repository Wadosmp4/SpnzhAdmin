from admin_app import db


class Invite(db.Model):
    __tablename__ = 'invites'
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), nullable=False)
    obj_id = db.Column(db.Integer(), nullable=False)
    obj_type = db.Column(db.Enum('event', 'group', 'notset'), nullable=False, default='notset')
    status = db.Column(db.Enum('created', 'yes', 'maybe', 'no'), nullable=False, default='created')
    created_at = db.Column(db.DateTime(timezone=False), default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime(), nullable=False, default=db.func.current_timestamp(),
                           onupdate=db.func.current_timestamp())

    @property
    def serialize(self):
        row = {}
        for c in self.__table__.columns:
            row[c.name] = getattr(self, c.name)
        return row
