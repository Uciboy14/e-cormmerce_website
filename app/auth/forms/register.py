from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(4, 40)])
    username = StringField("Username", validators=[DataRequired(), Length(4, 25)])
    email = StringField("Email", validators=[DataRequired(), Length(6, 64), Email()])
    password = PasswordField("New Password",
        validators=[DataRequired(),
        EqualTo('confirm', message="Passwords must match")
    ])
    confirm = PasswordField("Repeat Password")
