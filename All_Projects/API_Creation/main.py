import sqlalchemy
from flask import Flask, jsonify, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import random

from werkzeug.exceptions import BadRequestKeyError

app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500))
    img_url = db.Column(db.String(500))
    location = db.Column(db.String(250))
    seats = db.Column(db.String(250))
    has_toilet = db.Column(db.Boolean)
    has_wifi = db.Column(db.Boolean)
    has_sockets = db.Column(db.Boolean)
    can_take_calls = db.Column(db.Boolean)
    coffee_price = db.Column(db.String(250))

    def to_dict(self):
        dictionary = {}
        for column in self.__table__.columns:
            dictionary[column.name] = getattr(self, column.name)
        return dictionary


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/random")
def random_cafe():
    num = random.randint(1, 21)
    cafe = Cafe.query.filter_by(id=num).first()
    return jsonify(cafe={
        "name": cafe.name,
        "id": cafe.id,
        "map_url": cafe.map_url,
        "img_url": cafe.img_url,
        "location": cafe.location,
        "has_sockets": cafe.has_sockets,
        "has_wifi": cafe.has_wifi,
        "has_toilets": cafe.has_toilet,
        "take_Calls": cafe.can_take_calls,
        "seats": cafe.seats,
        "price": cafe.coffee_price
    })


@app.route("/all")
def get():
    all_cafes = db.session.query(Cafe).all()
    return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])


@app.route("/search")
def find():
    query_location = request.args.get("loc")
    cafe = db.session.query(Cafe).filter_by(location=query_location).first()
    try:
        return jsonify(cafe=cafe.to_dict())
    except AttributeError:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."})


@app.route('/post', methods=['POST', 'GET'])
def add_cafe():
    name: str = request.form.get('name', type=str)
    map_url: str = request.form.get('map_url', type=str)
    img_url: str = request.form.get('img_url', type=str)
    location: str = request.form.get('location', type=str)
    seats: str = request.form.get('seats', type=str)
    has_toilet: bool = request.form.get('has_toilet', type=bool)
    has_wifi: bool = request.form.get('has_wifi', type=bool)
    has_sockets: bool = request.form.get('has_sockets', type=bool)
    can_take_calls: bool = request.form.get('can_take_calls', type=bool)
    coffee_price: str = request.form.get('coffee_price', type=str)

    if request.method == 'POST':
        current_cafe_name = name
        found_cafe = Cafe.query.filter_by(name=current_cafe_name).first()
        if found_cafe:
            return jsonify(error={"Already Added": "Sorry, this cafe and its location had already been added."})
        else:
            add_a_cafe = Cafe(
                name=name,
                map_url=map_url,
                img_url=img_url,
                location=location,
                seats=seats,
                has_toilet=has_toilet,
                has_wifi=has_wifi,
                has_sockets=has_sockets,
                can_take_calls=can_take_calls,
                coffee_price=coffee_price
            )
            db.session.add(add_a_cafe)
            db.session.commit()
            return_added_cafe = Cafe.query.filter_by(name=current_cafe_name).first()
            return jsonify(Response={"Success": "Cafe has been successfully added"})


@app.route("/update-price/<cafe_id>", methods=["PATCH"])
def update_record(cafe_id):
    new_price = request.args.get("new_price")
    cafe = Cafe.query.filter_by(id=cafe_id).first()
    if cafe.coffee_price == new_price:
        return jsonify(response={"Status": 'The current price is same as new price'})
    else:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"Status": "Your record has been successfully updated"})


@app.route("/report-closed/<cafe_id>", methods=["DELETE"])
def delete_record(cafe_id):
    if request.args.get("api-key") == "TopSecretAPIKey":
        cafe_to_delete = Cafe.query.get(cafe_id)
        db.session.delete(cafe_to_delete)
        db.session.commit()
        return jsonify(response={"Success": "True", "Message": "You have successfully deleted record"})
    else:
        return jsonify(response={"Success": "False", "Status": "403"})


if __name__ == '__main__':
    app.run(debug=True)
