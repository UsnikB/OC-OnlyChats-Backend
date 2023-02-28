from database import db
from models.User import User
from models.UserType import UserType

def add_data():

    # Create admin node for user types
    admin = UserType.query.filter_by(name="admin").first()
    if not admin:
        admin = UserType(name="admin")
        db.session.add(admin)
        db.session.commit()
    
    customer = UserType.query.filter_by(name="customer").first()
    if not customer:
        customer = UserType(name="customer")
        db.session.add(customer)
        db.session.commit()
    user_1 = User.query.filter_by(username="admin").first()
    if not user_1:
        new_admin_user = User(username="admin", email="admin@example.com", password="password", user_type="admin")
        db.session.add(new_admin_user)
        db.session.commit()
    user_2 = User.query.filter_by(username="usnik").first()
    if not user_2:
        new_first_user = User(username="usnik", email="usnikbiswas@gmail.com", password="Qwe123")
        db.session.add(new_first_user)
        db.session.commit()
