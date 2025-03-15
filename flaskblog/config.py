import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    SECRET_KEY = 'bc0ada4a75941bc0234a9508e3999bcd'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIl_USER')
    MAIL_PASSWORD = os.environ.get('EMAIl_PASS')

