import os

# Statement for enabling the development environment
DEBUG = True

# Define the application directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Define the database - we are working with
DB_USERNAME = 'root'
DB_PASSWORD = 'mysql'
DB_HOST = 'localhost'
DB_NAME = 'spnzh'

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' + \
                          DB_USERNAME + ':' + \
                          DB_PASSWORD + '@' + \
                          DB_HOST + '/' + \
                          DB_NAME + '?charset=utf8mb4&binary_prefix=true'

DATABASE_CONNECT_OPTIONS = {}