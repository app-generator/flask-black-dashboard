from . import routes
from flask import Blueprint

blueprint = Blueprint(
    'portfolio_blueprint',
    __name__,
    url_prefix='/portfolio'
)
