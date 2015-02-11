from flask.ext.sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from . import db, login_manager, mdb
from flask.ext.login import UserMixin
from time import strftime
import json
from bson.json_util import dumps
from flask import Response

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    default = db.Column(db.Boolean, default=False, index=True)
    permissions = db.Column(db.Integer)
    users = db.relationship('User', backref='role', lazy='dynamic')
    def __repr__(self):
        return '<Role %r>' % self.name
    
    @staticmethod
    def insert_roles():
        roles = {
                'Viewer': (Permission.VIEW_DATA, True),
                'Viewer_Notify': (Permission.VIEW_DATA |
                    Permission.RECV_NOTIFICATIONS, False),
                'Tester': (Permission.VIEW_DATA |
                    Permission.RECV_NOTIFICATIONS |
                    Permission.EXEC_TESTS |
                    Permission.EXEC_COMMANDS, False),
                'Admin': (0x08, False)
                }
        for r in roles:
            role = Role.query.filter_by(name=r).first()
            if role is None:
                role = Role(name=r)
            role.permissions = roles[r][0]
            role.default = roles[r][1]
            db.session.add(role)
        db.session.commit()

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return self.username
    
    @property
    def password(self):
        raise AttributeError('Password malformed')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        if self.role is None:
            self.role = Role.query.filter_by(default=True).first()

    def can(self, permissions):
        return self.role is not None and (self.role.permissions & permissions) == permissions

    def is_admin(self):
        return self.can(Permission.ADMINISTER)

class Permission:
    VIEW_DATA = 0x01
    RECV_NOTIFICATIONS = 0x2
    EXEC_TESTS = 0X03
    EXEC_COMMANDS = 0x03
    ADMINISTER = 0x08

#Flask-Login requires we setup a callback function that loads the user by user_id.
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def mongo_jsonify(data):
    return Response(dumps(data), mimetype='application/json')



class TelemData():
    def getMostRecent(self, amount=1):
        """Return entire recently inserted JSON data, in descending order.

        Arguments:
        amount (int): The amount of docs you want returned. (default 1)
        
        Returns:
        dict: All data is returned as valid JSON, in a dictionary.

        Raises:
        KeyError: If there is no data from the MongoDB database.
        """
        obj = mdb.db.data.find({}, {"_id": False}).sort([{"timestamp", -1}]).limit(amount)
        obj = json.loads(dumps(obj))
        return obj

    def getField(self, field, subfield=None, amount=5):
        """Get the requested field from the most recently inserted JSON data, in descending order

        Arguments:
        amount (int): The amount of the specified field you want returned (default 5)

        Returns:
        dict: All data is returned in a dictionary.

        None: No data for the requested field was found.
        """
        data = self.getMostRecent(amount)
        datar = []
        for doc in data:
            try:
                if subfield == None:
                    datar.append(doc[field])
                else:
                    datar.append(doc[field][subfield])
            except KeyError:
                return None
        return datar
