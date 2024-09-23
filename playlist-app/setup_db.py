from flask import Flask
from models import db, Playlist, Song, PlaylistSong

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///playlist-app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

db.init_app(app)

with app.app_context():
    db.create_all()
    print("Database tables created!")
