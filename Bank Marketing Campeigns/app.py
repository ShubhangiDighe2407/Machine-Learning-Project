import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

# Create flask app
flask_app = Flask(__name__,template_folder='templates')
model = pickle.load(open("Model1.pkl", "rb"))

@flask_app.route("/")
def home():
    return render_template("index2.html")
@flask_app.route("/predict", methods = ["POST"])
def predict():
    float_features = [str(x) for x in request.form.values()]
    features = [np.array(float_features)]
    prediction = model.predict(features)

    if prediction[0] == 0:
        prediction="Customer will not subscribe for deposites"
    else:
        prediction="Customer will  subscribe for deposites"

    return render_template("index2.html", prediction = prediction)

if __name__ == "__main__":
    flask_app.run(host='0.0.0.0',port=8080)  