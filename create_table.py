from pacote import db, app
from pacote.models import User, Post

with app.app_context():
    db.create_all()