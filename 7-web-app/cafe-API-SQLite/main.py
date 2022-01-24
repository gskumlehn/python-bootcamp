from flask import Flask, jsonify, request, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from random import choice

# CREATES API KEY
API_MASTER_KEY = "TopSecretAPIKey"

# Initialises Flask
app = Flask(__name__)

# Initialises Bootstrap
app.config['SECRET_KEY'] = "jfhgwkefjh902bwd0234g2o"
Bootstrap(app)

# Initialises Database
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///cafes.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Creates table model
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    seats = db.Column(db.String(250))
    coffee_price = db.Column(db.String(250))

    # Creates method to convert to dict
    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

# Home with link to Documentation
@app.route("/")
def home():
    render_template("index.html")

# Returns all data
@app.route("/all")
def all():
    cafes_list = [cafe.to_dict() for cafe in db.session.query(Cafe).all()]
    return jsonify(cafes=cafes_list)

# Returns random data
@app.route("/random")
def random():
    cafes_list = db.session.query(Cafe).all()
    random_cafe = choice(cafes_list)
    return jsonify(cafe=random_cafe.to_dict())

# Search data by location
@app.route("/search")
def search():
    loc_query = request.args.get("loc")
    cafes_list = [cafe.to_dict() for cafe in Cafe.query.filter_by(location=loc_query)]
    if cafes_list == []:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location"})
    else:
        return jsonify(cafes=cafes_list)

# Adds data
@app.route("/add", methods=["POST"])
def add():
    new_cafe = Cafe(name=request.form.get("name"),
                    map_url=request.form.get("map_url"),
                    img_url=request.form.get("img_url"),
                    location=request.form.get("loc"),
                    has_sockets=bool(request.form.get("sockets")),
                    has_toilet=bool(request.form.get("toilet")),
                    has_wifi=bool(request.form.get("wifi")),
                    can_take_calls=bool(request.form.get("calls")),
                    seats=request.form.get("seats"),
                    coffee_price=request.form.get("coffee_price"))
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"response": "Successfully added the new cafe."})

# Updates data
@app.route("/update_price/<int:cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    cafe_to_update = Cafe.query.get(cafe_id)
    if cafe_to_update != None:
        new_price = request.args.get("new_price")
        cafe_to_update.coffee_price = new_price
        db.session.commit()
        return jsonify(success="Successfully updated the price."), 200
    else:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database"}), 404

# Deletes data, key required
@app.route("/report_closed/<int:cafe_id>", methods=["DELETE"])
def report_closed(cafe_id):
    key = request.args.get("api-key")
    if key == API_MASTER_KEY:
        cafe_to_delete = Cafe.query.get(cafe_id)
        if cafe_to_delete != None:
            db.session.delete(cafe_to_delete)
            db.session.commit()
            return jsonify(success="Closed Cafe deleted successfully"), 200
        else:
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database"}), 404
    else:
        return jsonify(error="Sorry, that's not allowed. Make sure you have the correct api-key"), 403


if __name__ == "__main__":
    app.run(debug=True)
