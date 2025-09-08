import os
import numpy as np
from flask import Flask, request, jsonify, send_from_directory
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from flask_cors import CORS

# Initialize Flask
app = Flask(__name__, static_folder="build", static_url_path="")
CORS(app)

# Load trained model
MODEL_PATH = "isl_model.h5"
model = load_model(MODEL_PATH)

# Class labels (adjust according to your dataset)
class_labels = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

# Prediction endpoint
@app.route("/predict", methods=["POST"])
def predict():
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    file = request.files["image"]
    img_path = "temp.jpg"
    file.save(img_path)

    # Preprocess image
    img = image.load_img(img_path, target_size=(64, 64))  # adjust size if needed
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0

    # Model prediction
    predictions = model.predict(img_array)
    predicted_class = class_labels[np.argmax(predictions)]

    return jsonify({"prediction": predicted_class})


# Serve React frontend
@app.route("/")
def serve_frontend():
    return send_from_directory(app.static_folder, "index.html")

@app.route("/<path:path>")
def serve_static_files(path):
    return send_from_directory(app.static_folder, path)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
