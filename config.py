import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    WTF_CSRF_ENABLED = True
    SECRET_KEY = os.environ.get(
        'SECRET_KEY') or 'eyJhbGciOiJIUzI1NiIsImV4cCI6MTQ4ODIwNTc2MiwiaWF0IjoxNDg4MTY5NzYy'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    TODO_ADMIN = os.environ.get('ADMIN') or ''
    TODO_MAIL_SENDER = 'todoinc Admin todo@gmail.com'
    MAIL_SUBJECT_PREFIX = '[todo]'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or "todo@gmail.com"
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or "password"
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DEV_DATABASE_URI') or 'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'TEST_DATABASE_URI') or 'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')
    WHOOSH_BASE = os.path.join(basedir, 'test_search.db')


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URI') or 'sqlite:///' + os.path.join(basedir, 'data.sqlite')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
