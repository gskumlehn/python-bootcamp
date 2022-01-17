from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateTimeField, SelectField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField("Location URL on Google Maps", validators=[DataRequired(), URL()])
    opens = StringField("Opening Time e.g. 8AM", validators=[DataRequired()])
    closes = StringField("Closing Time e.g. 9PM", validators=[DataRequired()])
    coffee_rating = SelectField("Coffee Rating",
                                choices=["☕","☕☕","☕☕☕","☕☕☕☕","☕☕☕☕☕"], validators=[DataRequired()])
    wifi_rating = SelectField("WiFi Rating",
                              choices=["✘","💪","💪💪","💪💪💪","💪💪💪💪","💪💪💪💪💪"], validators=[DataRequired()])
    po_rating = SelectField("Power Outlet Rating",
                            choices=["✘","🔌","🔌🔌","🔌🔌🔌","🔌🔌🔌🔌","🔌🔌🔌🔌🔌"],  validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add',methods=["GET","POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print("True")
        with open("cafe-data.csv", "a", encoding="utf8") as file:
            file.write(f"\n{form.cafe.data},"
                       f"{form.location.data},"
                       f"{form.opens.data},"
                       f"{form.closes.data},"
                       f"{form.coffee_rating.data},"
                       f"{form.wifi_rating.data},"
                       f"{form.po_rating.data}")
        return redirect(url_for("cafes"))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding="utf8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
