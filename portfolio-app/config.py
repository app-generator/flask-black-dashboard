import os
import random
import string
from datetime import timedelta


class Config(object):
    # Base directory
    BASEDIR = os.path.abspath(os.path.dirname(__file__))

    # App paths
    APP_ROOT = os.path.dirname(os.path.abspath(__file__))
    TEMPLATES_ROOT = os.path.join(APP_ROOT, 'templates')
    STATIC_ROOT = os.path.join(APP_ROOT, 'static')

    # Portfolio settings
    PORTFOLIO_NAME = "My Investment Portfolio"
    DEFAULT_CAPITAL = 250000.00
    CURRENCY = "USD"

    # Database settings
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DB_PATH = os.path.join(BASEDIR, 'db', 'db.sqlite3')
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{DB_PATH}'

    # Assets paths
    ASSETS_ROOT = os.getenv('ASSETS_ROOT', '/static/assets')
    UPLOAD_FOLDER = os.path.join(STATIC_ROOT, 'uploads')

    # Security
    SECRET_KEY = os.getenv('SECRET_KEY', ''.join(
        random.choice(string.ascii_lowercase) for i in range(32)))
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_DURATION = timedelta(days=7)

    # GitHub OAuth
    GITHUB_ID = os.getenv('GITHUB_ID', None)
    GITHUB_SECRET = os.getenv('GITHUB_SECRET', None)
    SOCIAL_AUTH_GITHUB = bool(GITHUB_ID and GITHUB_SECRET)

    # API settings
    API_PREFIX = '/api/v1'

    # Portfolio data settings
    PORTFOLIO_CATEGORIES = [
        'Stocks',
        'Bonds',
        'Crypto',
        'Commodities',
        'Real Estate'
    ]

    # Chart settings
    CHART_COLORS = {
        'primary': '#e14eca',
        'info': '#1d8cf8',
        'success': '#00f2c3',
        'warning': '#ff8d72',
        'danger': '#fd5d93'
    }


class ProductionConfig(Config):
    DEBUG = False
    ENV = 'production'


class DevelopmentConfig(Config):
    DEBUG = True
    ENV = 'development'


# Load configuration
config_dict = {
    'Production': ProductionConfig,
    'Development': DevelopmentConfig
}
