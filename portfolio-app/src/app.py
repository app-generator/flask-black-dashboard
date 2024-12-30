from flask import Flask
from flask_login import LoginManager
from apps.authentication.oauth import github_blueprint
from apps.authentication.models import Users
from apps.home import blueprint as home_blueprint

app = Flask(__name__)
app.config.from_object('apps.config.Config')

# Initialize extensions
login_manager = LoginManager()
login_manager.init_app(app)

# Register blueprints
app.register_blueprint(github_blueprint, url_prefix="/login")
app.register_blueprint(home_blueprint)


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


if __name__ == '__main__':
    app.run(debug=True)
