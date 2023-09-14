from flask_wtf.file import FileAllowed, FileField, FileRequired
from wtforms import Form,StringField, IntegerField, BooleanField, TextAreaField, DecimalField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class AddProducts(Form):
    name = StringField("Name", validators=[DataRequired()])
    price = IntegerField("Price:RS ", validator=[DataRequired()])
    stock = IntegerField("Stock", validators=[DataRequired()])
    desc = TextAreaField("Description", validators=[DataRequired()])
    colors = TextAreaField("Colors", validators=[DataRequired()])
    image_1 = FileField('Image 1', validators=[FileAllowed(['jpg, jpeg, png, svg, gif'])])
