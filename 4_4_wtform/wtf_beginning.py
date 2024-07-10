from flask import Flask
from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField
from wtforms.validators import InputRequired, Email, NumberRange

app = Flask(__name__)


class RegistrationForm(FlaskForm):
    phone = StringField()
    name = StringField()
    address = StringField()


@app.route("/register", methods=["POST"])
def register():
    form = RegistrationForm()

    if not form.name.data or not form.phone.data or not form.address.data:
        return f"Invalid input, one field is not filled", 400

    if form.validate_on_submit():
        name, phone = form.name.data, form.phone.data
        return f"Successfully registered user {name} with phone +7{phone}"

    return f"Invalid input, {form.errors}", 400


if __name__ == "__main__":
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)
