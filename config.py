import os

class BaseConfig(object):
  DEBUG = False
  SECRET_KEY = 'Still not secret key'
  SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

class DevConfig(BaseConfig):
  DEBUG = True

class ProdConfig(BaseConfig):
  DEBUG = False