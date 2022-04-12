from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class NymoPostForm(FlaskForm):
    text = TextAreaField('', validators=[DataRequired()], render_kw={"placeholder": "Spill the Beans"})
    submit = SubmitField('Post')
