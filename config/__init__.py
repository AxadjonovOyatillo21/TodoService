import os




class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.urandom(100)
    USERNAME = os.getenv("USERNAME") or None 
    PASSWORD = os.getenv("PASSWORD") or None
    SERVER = os.getenv("SERVER") or None
    PORT = os.getenv("PORT") or None 
    DB_NAME = os.getenv("DB_NAME") or None
    if all([USERNAME, PASSWORD, SERVER, PORT, DB_NAME]): 
        SQLALCHEMY_DATABASE_URI = f"postgresql://{USERNAME}:{PASSWORD}@{SERVER}:{PORT}/{DB_NAME}"
    else:
        SQLALCHEMY_DATABASE_URI = "sqlite:///database/database.db"
