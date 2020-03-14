from . import db
from werkzeug.security import generate_password_hash

class UserProfile(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    __tablename__ = 'user_profiles'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    gender = db.Column(db.String(25), unique=True)
    email = db.Column(db.String(200))
    location = db.Column(db.String(200))
    biography = db.Column(db.String(150))
    image = db.Column(db.String(255))
    joined_on = db.Column(db.Date)


    def _init_(self, first_name, last_name, gender, email, location, biography, image, joined_on):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.email = email
        self.location = location
        self.biography = biography
        self.image = image
        self.joined_on = joined_on

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.first_name)
