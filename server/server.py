from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Home Price Prediction API is running!"

@app.route("/predict_home_price", methods=["POST"])
def predict_home_price():
    data = request.get_json()

    estimated_price = util.get_estimated_price(data)

    response = jsonify({
        "estimated_price": estimated_price
    })
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


if __name__ == "__main__":
    print("Starting Flask Server for Home Price Prediction...")
    util.load_saved_artifacts()
    app.run(debug=True)
