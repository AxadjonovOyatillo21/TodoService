import os

SECRET_KEY = os.urandom(100)
PORT = 8080
#============================#
#                            #
#-- Database configuration --#
#                            #
#============================#

SQLALCHEMY_TRACK_MODIFICATIONS = False
USERNAME = os.getenv("USERNAME") or None 
PASSWORD = os.getenv("PASSWORD") or None
SERVER = os.getenv("SERVER") or None
PORT = os.getenv("PORT") or None 
DB_NAME = os.getenv("DB_NAME") or None
DB = os.getenv("DB")
if all([USERNAME, PASSWORD, SERVER, PORT, DB_NAME, DB]): 
    SQLALCHEMY_DATABASE_URI = f"{DB}://{USERNAME}:{PASSWORD}@{SERVER}:{PORT}/{DB_NAME}"
else:
    SQLALCHEMY_DATABASE_URI = "sqlite:///database/database.sqlite"
