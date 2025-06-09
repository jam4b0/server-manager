from flask import Flask
from flask_login import LoginManager
from config import SECRET_KEY
from modules.auth import auth_bp, login_manager
from modules.smb import smb_bp
from modules.nfs import nfs_bp
from modules.usermgmt import usermgmt_bp

def create_app():
    app = Flask(__name__)
    app.secret_key = SECRET_KEY

    login_manager.init_app(app)

    app.register_blueprint(auth_bp)
    app.register_blueprint(smb_bp, url_prefix="/smb")
    app.register_blueprint(nfs_bp, url_prefix="/nfs")
    app.register_blueprint(usermgmt_bp, url_prefix="/users")

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host='192.168.178.200', port=5000, debug=True)
