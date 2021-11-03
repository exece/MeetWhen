from datetime import datetime
'''

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

'''

class Destination():
    def __init__(self, name, description, image, currency):
        self.name = name
        self.description = description
        self.image = image
        self.currency = currency
        self.comments = list()

    def add_comment(self, comment):
        self.comments.append(comment)

class Comment():
    def __init__(self, user, text):
        self.user = user
        self.text = text
        self.create_at = datetime.now()  

class Booking:
    def __init__(self, start_date, end_date, user, city):
        self.start_date = start_date
        self.end_date = end_date
        self.booking_date = datetime.now()
        self.user = user
        self.city = city
        self.num_guests = 1
    
    def __repr__(self):
        return f"Booking(User:'{self.user}', Email:'{self.city}', Num of Guests:'{self.num_guests}', )" #finish

    def get_booking_details(self):
        return str(self)


class User:
    def __init__(self):
        self.type = "guest"
        self.user_name = None
        self.password_hash = None
        self.email_id = None

    def reigster(self, user_name, password_hash, email_id):
        self.user_name = user_name
        self.password_hash = password_hash
        self.email_id = email_id
        self.type = 'user'

    def __repr__(self):
        return f"User( user_name:'{self.user_name}', password_hash:'{self.password_hash}', email_id: '{self.email_id}', type: '{self.type}')"


class City:
    def __init__(self, city_name, city_discription):
        self.city_name = city_name
        self.city_description = city_discription

    def __repr__(self):
        return f"City( city_name:'{self.city_name}', city_discription:'{self.city_description}')"

    def getCityDetails(self):
        return str(self)
