"""Forms for playlist app."""

from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import InputRequired, Length
from flask_wtf import FlaskForm


class PlaylistForm(FlaskForm):
    """Form for adding playlists."""

    name = StringField("Playlist Name", validators=[InputRequired(), Length(max=100)])
    description = TextAreaField("Description", validators=[Length(max=500)])  # Added description


class SongForm(FlaskForm):
    """Form for adding songs."""

    title = StringField("Song Title", validators=[InputRequired(), Length(max=100)])
    artist = StringField("Artist", validators=[InputRequired(), Length(max=100)])
    album = StringField("Album", validators=[Length(max=100)])  # Added album field
    duration = StringField("Duration (seconds)", validators=[InputRequired()])  # Added duration field


# DO NOT MODIFY THIS FORM - EVERYTHING YOU NEED IS HERE
class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""

    song = SelectField('Song To Add', coerce=int)
