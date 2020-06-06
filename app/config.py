"Central configuration"
import os

PHOTOS_BUCKET = os.environ.get('PHOTOS_BUCKET')
FLASK_SECRET = os.environ.get('FLASK_SECRET')

DATABASE_HOST = os.environ.get('DATABASE_HOST')
DATABASE_USER = os.environ.get('DATABASE_USER')
DATABASE_PASSWORD = os.environ.get('DATABASE_PASSWORD')
DATABASE_DB_NAME = os.environ.get('DATABASE_DB_NAME')

AWS_REGION = "us-west-2"
COGNITO_POOL_ID = os.environ.get('COGNITO_POOL_ID')
COGNITO_CLIENT_ID = os.environ.get('COGNITO_CLIENT_ID')
COGNITO_CLIENT_SECRET = os.environ.get('COGNITO_CLIENT_SECRET')
COGNITO_DOMAIN = os.environ.get('COGNITO_DOMAIN')
BASE_URL = os.environ.get('BASE_URL')
