from flask import Flask
from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField
from wtforms.validators import InputRequired, Email, NumberRange

app = Flask(__name__)


class RegistrationForm(FlaskForm):
    phone = StringField()
    name = StringField()
    address = StringField()


@app.route("/registration", methods=["POST"])
def registration():
    form = RegistrationForm()
    if not phone:
        pass
