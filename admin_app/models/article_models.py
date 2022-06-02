from admin_app import db


class ArticlesGroups(db.Model):
    __tablename__ = 'articles_groups'
    article_id = db.Column(db.Integer(), nullable=False)
    group_id = db.Column(db.Integer(), nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False, default=db.func.current_timestamp())

    __table_args__ = (
        db.PrimaryKeyConstraint(
            article_id, group_id,
        ),
    )

    @property
    def serialize(self):
        row = {}
        for c in self.__table__.columns:
            row[c.name] = getattr(self, c.name)
        return row


class Article(db.Model):
    __tablename__ = 'articles'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text(), nullable=False)
    datetime = db.Column(db.DateTime(), nullable=False, default=db.func.current_timestamp())
    user_id = db.Column(db.Integer(), nullable=False, index=True)
    type = db.Column(db.String(20), nullable=True, default=None)
    time_visible = db.Column(db.Integer(), nullable=False)
    lat = db.Column(db.Float(), nullable=True, default=None)
    lon = db.Column(db.Float(), nullable=True, default=None)
    image_link = db.Column(db.Text(), nullable=True, default=None)
    video_link = db.Column(db.Text(), nullable=True, default=None)
    video_image_link = db.Column(db.Text(), nullable=True, default=None)
    sound_link = db.Column(db.Text(), nullable=True, default=None)
    mode = db.Column(db.Enum('global', 'friends', 'incognito', 'followers', 'groups', 'anonymous', 'private', 'members'), nullable=False, default='global')
    views_count = db.Column(db.Integer(), nullable=False, default=0)
    tags = db.Column(db.String(250), nullable=False, default='')
    place = db.Column(db.String(250), nullable=False, default='')
    phone = db.Column(db.String(50), nullable=True, default=None)
    email = db.Column(db.String(100), nullable=True, default=None)
    site = db.Column(db.String(100), nullable=True, default=None)
    event_datetime = db.Column(db.DateTime(), nullable=True, default=None)
    tickets = db.Column(db.String(200), nullable=True, default=None)
    group_id = db.Column(db.Integer(), nullable=True, index=True)
    sound_duration = db.Column(db.Integer(), nullable=True, default=None)
    time_delay = db.Column(db.Integer(), nullable=False, default=0)

    @property
    def serialize(self):
        row = {}
        for c in self.__table__.columns:
            row[c.name] = getattr(self, c.name)
        return row


class ArticlesLikes(db.Model):
    __tablename__ = 'articles_likes'
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), nullable=False)
    article_id = db.Column(db.Integer(), nullable=False)
    like_type = db.Column(db.Integer(), nullable=False, default=1)
    datetime = db.Column(db.DateTime(), default=db.func.current_timestamp())

    @property
    def serialize(self):
        row = {}
        for c in self.__table__.columns:
            row[c.name] = getattr(self, c.name)
        return row


class ArticlesShares(db.Model):
    __tablename__ = 'articles_shares'
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), nullable=False)
    article_id = db.Column(db.Integer(), nullable=False)
    user_id_for = db.Column(db.Integer(), nullable=False)
    datetime = db.Column(db.DateTime(), default=db.func.current_timestamp())

    @property
    def serialize(self):
        row = {}
        for c in self.__table__.columns:
            row[c.name] = getattr(self, c.name)
        return row


class ArticlesUsers(db.Model):
    __tablename__ = 'articles_users'
    article_id = db.Column(db.Integer(), nullable=False)
    user_id = db.Column(db.Integer(), nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False, default=db.func.current_timestamp())

    __table_args__ = (
        db.PrimaryKeyConstraint(
            article_id, user_id,
        ),
    )

    @property
    def serialize(self):
        row = {}
        for c in self.__table__.columns:
            row[c.name] = getattr(self, c.name)
        return row


class ArticlesViews(db.Model):
    __tablename__ = 'articles_views'
    article_id = db.Column(db.Integer(), nullable=False)
    user_id = db.Column(db.Integer(), nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False, default=db.func.current_timestamp())

    __table_args__ = (
        db.PrimaryKeyConstraint(
            article_id, user_id,
        ),
    )

    @property
    def serialize(self):
        row = {}
        for c in self.__table__.columns:
            row[c.name] = getattr(self, c.name)
        return row
