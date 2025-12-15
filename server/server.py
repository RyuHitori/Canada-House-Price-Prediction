from flask import Flask, request, jsonify, render_template
import util

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    estimated_price = None

    if request.method == "POST":
        data = {
            "City": request.form["City"],
            "Province": request.form["Province"],
            "Bedrooms": int(request.form["Bedrooms"]),
            "Bathrooms": int(request.form["Bathrooms"]),
            "Acreage": float(request.form["Acreage"]),
            "Property Type": request.form["Property Type"],
            "Square Footage": float(request.form["Square Footage"]),
            "Garage": request.form["Garage"],
            "Parking": request.form["Parking"],
            "Fireplace": request.form["Fireplace"],
            "Heating": request.form["Heating"],
            "Waterfront": request.form["Waterfront"],
            "Sewer": request.form["Sewer"],
            "Pool": request.form["Pool"],
            "Garden": request.form["Garden"],
            "Balcony": request.form["Balcony"],
        }

        estimated_price = util.get_estimated_price(data)

    return render_template(
        "index.html",
        estimated_price=estimated_price,
        categories=util.get_categories(),
    )


@app.route("/predict_home_price", methods=["POST"])
def predict_home_price():
    data = request.get_json()
    estimated_price = util.get_estimated_price(data)
    return jsonify({"estimated_price": estimated_price})


if __name__ == "__main__":
    print("Starting Flask Server for Home Price Prediction...")
    util.load_saved_artifacts()
    app.run(debug=True)
