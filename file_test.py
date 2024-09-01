from pacote import db, app
from pacote.models import User, Post

# with app.app_context():
#     obj = Post(title= 'novo', content= 'content', id_user=3)
#     db.session.add(obj)
#     db.session.commit()


with app.app_context():
    posts = Post.query.all()
    for post in posts:
        post.author.username = post.author.username.title()
        print(post.author.username, post.id, post.author.id)
    db.session.commit()
