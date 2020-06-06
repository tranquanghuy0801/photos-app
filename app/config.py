"Central configuration"
import os
from dotenv import load_dotenv

load_dotenv(verbose=True)

PHOTOS_BUCKET = os.environ['PHOTOS_BUCKET']
FLASK_SECRET = os.environ['FLASK_SECRET']

DATABASE_HOST = os.environ['DATABASE_HOST']
DATABASE_USER = os.environ['DATABASE_USER']
DATABASE_PASSWORD = os.environ['DATABASE_PASSWORD']
DATABASE_DB_NAME = os.environ['DATABASE_DB_NAME']

AWS_REGION = "us-west-2"
COGNITO_POOL_ID = os.environ['COGNITO_POOL_ID']
COGNITO_CLIENT_ID = os.environ['COGNITO_CLIENT_ID']
COGNITO_CLIENT_SECRET = os.environ['COGNITO_CLIENT_SECRET']
COGNITO_DOMAIN = os.environ['COGNITO_DOMAIN']
BASE_URL = os.environ['BASE_URL']
