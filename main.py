from flask import Flask, render_template, request
from keras.preprocessing.image import img_to_array
from keras.models import load_model
import cv2
import numpy as np

from flask_cors import CORS, cross_origin

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model = load_model(os.path.join(BASE_DIR , 'capstone_1.2_model.hdf5'))

ALLOWED_EXT = set(['jpg' , 'jpeg' , 'png' , 'jfif'])
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXT

classes = ['acne-cystic', 'acne-excoriated', 'acne-open-comedo', 
           'acne-pustular', 'acne-scar', 'closed-comedo', 'milia',
           'perioral-dermatitis', 'Rhinophyma', 'Rosacea', 'rosacea-nose']

# Process image and predict label
def processImg(IMG_PATH):
    # Preprocess image
    image = cv2.imread(IMG_PATH)
    image = cv2.resize(image, (224, 224))
    image = image.astype("float") / 255.0
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)

    res = model.predict(image)
    label = np.argmax(res)
    print("Label", label)
    labelName = classes[label]
    print("Label name:", labelName)
    return labelName


# Initializing flask application
app = Flask(__name__)
cors = CORS(app)

@app.route("/")
def main():
    return """
        Application is working
    """

# About page with render template
@app.route("/about")
def postsPage():
    return render_template("about.html")

# Process images
@app.route("/process", methods=["POST"])
def processReq():
    data = request.files["img"]
    data.save("img.jpg")

    resp = processImg("img.jpg")


    return resp


if __name__ == "__main__":
    app.run(debug=True)