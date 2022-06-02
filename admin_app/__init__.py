from flask import Flask
from flask_admin import Admin
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask.json import JSONEncoder
from datetime import date

app = Flask('adminapp')

app.config.from_object('config')
app.url_map.strict_slashes = False
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

admin = Admin(app, name='SpnzhAdmin', template_mode='bootstrap3')


class AppJSONEncoder(JSONEncoder):
    def default(self, obj):
        try:
            if isinstance(obj, date):
                return obj.isoformat()
            iterable = iter(obj)
        except TypeError:
            pass
        else:
            return list(iterable)
        return JSONEncoder.default(self, obj)


app.json_encoder = AppJSONEncoder
db = SQLAlchemy(app)

login_manager = LoginManager(app)
