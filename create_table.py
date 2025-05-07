from pacote import db, app
from pacote.models import User, Post

# comando para criar todas as tables
with app.app_context():
    db.create_all()
