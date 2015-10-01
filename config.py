import os

class BaseConfig(object):
  DEBUG = False
  SECRET_KEY = '\xab%\x82\xa7\x1d\xa7\xa9\x91\xdc\x84\xb7pWF\x9fm\x1f_\xa4\xec\xf9\xf4\xb5\xd3'
  SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

class DevConfig(BaseConfig):
  DEBUG = True

class ProdConfig(BaseConfig):
  DEBUG = False