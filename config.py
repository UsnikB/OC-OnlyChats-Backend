# config.py

class Config:
    SECRET_KEY = 'Nn06zKYQs25e57HniSFwfJN1l'
    JWT_ALGORITHM = 'HS256'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://usnik:qwe123@db/code'