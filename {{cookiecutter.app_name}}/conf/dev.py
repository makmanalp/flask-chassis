DEBUG = True
SECRET_KEY = 'lalalalalalala'

SENTRY_DSN = ""

SQLALCHEMY_ECHO = DEBUG
SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"

CACHE_TYPE = "simple"
CACHE_KEY_PREFIX = "{{cookiecutter.app_name}}::"

DEBUG_TB_ENABLED = DEBUG
PROFILE = False
