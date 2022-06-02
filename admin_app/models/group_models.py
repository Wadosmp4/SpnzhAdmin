from admin_app import db


class FavoriteGroup(db.Model):
    __tablename__ = 'groups_favorites'
    user_id = db.Column(db.Integer())
    group_id = db.Column(db.Integer())
    created_at = db.Column(db.DateTime(), nullable=False, default=db.func.current_timestamp())
    __table_args__ = (
        db.PrimaryKeyConstraint(
            user_id, group_id,
        ),
    )

    @property
    def serialize(self):
        row = {}
        for c in self.__table__.columns:
            row[c.name] = getattr(self, c.name)
        return row


class GroupFollower(db.Model):
    __tablename__ = 'groups_followers'
    user_id = db.Column(db.Integer())
    group_id_follow = db.Column(db.Integer())
    status = db.Column(db.Enum('approved', 'blocked'), nullable=False, default='approved')
    created_at = db.Column(db.DateTime(), nullable=False, default=db.func.current_timestamp())
    __table_args__ = (
        db.PrimaryKeyConstraint(
            user_id, group_id_follow,
        ),
    )

    @property
    def serialize(self):
        row = {}
        for c in self.__table__.columns:
            row[c.name] = getattr(self, c.name)
        return row


class Groups(db.Model):
    __tablename__ = 'groups'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(200), nullable=False, unique=True)
    short_description = db.Column(db.Text(), nullable=True, default='')
    description = db.Column(db.Text(), nullable=True, default='')
    creator_user_id = db.Column(db.Integer(), nullable=False)
    mode = db.Column(db.Enum('public', 'private'), nullable=False, default='public')
    created_at = db.Column(db.DateTime(), nullable=False, default=db.func.current_timestamp())
    allow_join_request = db.Column(db.Boolean(), nullable=False, default=1)
    messaging_type = db.Column(db.String(20), nullable=True, default='')

    @property
    def serialize(self):
        row = {}
        for c in self.__table__.columns:
            row[c.name] = getattr(self, c.name)
        return row


class GroupRecommend(db.Model):
    __tablename__ = 'groups_recommend'
    user_id = db.Column(db.Integer())
    group_id = db.Column(db.Integer())
    created_at = db.Column(db.DateTime(), nullable=False, default=db.func.current_timestamp())
    __table_args__ = (
        db.PrimaryKeyConstraint(
            user_id, group_id,
        ),
    )

    @property
    def serialize(self):
        row = {}
        for c in self.__table__.columns:
            row[c.name] = getattr(self, c.name)
        return row


class GroupShare(db.Model):
    __tablename__ = 'groups_share'
    user_id = db.Column(db.Integer())
    group_id = db.Column(db.Integer())
    created_at = db.Column(db.DateTime(), nullable=False, default=db.func.current_timestamp())
    __table_args__ = (
        db.PrimaryKeyConstraint(
            user_id, group_id,
        ),
    )

    @property
    def serialize(self):
        row = {}
        for c in self.__table__.columns:
            row[c.name] = getattr(self, c.name)
        return row


class UsersGroups(db.Model):
    __tablename__ = 'users_groups'
    user_id = db.Column(db.Integer())
    group_id = db.Column(db.Integer())
    user_status = db.Column(db.Enum('requested', 'approved', 'blocked'), nullable=False, default='requested')
    user_role = db.Column(db.Enum('creator', 'admin_models', 'member'), nullable=False, default='member')
    created_at = db.Column(db.DateTime(), nullable=False, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime(), nullable=False, default=db.func.current_timestamp(),
                           onupdate=db.func.current_timestamp())
    __table_args__ = (
        db.PrimaryKeyConstraint(
            user_id, group_id,
        ),
    )

    @property
    def is_creator(self):
        if self.user_role == 'creator':
            return True
        else:
            return False

    @property
    def is_admin(self):
        if self.user_role == 'admin_models':
            return True
        else:
            return False

    @property
    def serialize(self):
        row = {}
        for c in self.__table__.columns:
            row[c.name] = getattr(self, c.name)
        return row
