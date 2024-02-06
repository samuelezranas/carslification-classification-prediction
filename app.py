from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from sklearn.linear_model import LinearRegression
import joblib
import numpy as np


app = Flask(__name__)

dic = {0: 'SUV',
       1: 'bus',
       2: 'sedan',
       3: 'fire engine',
       4: 'heavy truck',
       5: 'jeep',
       6: 'minibus',
       7: 'racing car',
       8: 'taxi',
       9: 'truck'
}

model_image = load_model('modelmobil.h5')
model_ford = joblib.load('estimasi_ford.sav')

model_image.make_predict_function()

def predict_label_image(img_path):
    i = image.load_img(img_path, target_size=(224, 224))
    i = image.img_to_array(i) / 255.0
    i = i.reshape(1, 224, 224, 3)
    predict_x = model_image.predict(i)
    classes_x = np.argmax(predict_x, axis=1)
    return dic[classes_x[0]]

# routes
@app.route("/", methods=['GET', 'POST'])
def main():
    return render_template("index.html")

@app.route("/submit", methods=['POST'])
def get_output():
    if request.method == 'POST':
        img = request.files['my_image']

        img_path = "../carslification/static/test/" + img.filename
        img.save(img_path)

        p_image = predict_label_image(img_path)

    return render_template("index.html", prediction_image=p_image, img_path=img_path)

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Assuming 'mpg', 'engine_size', 'tax', 'year', 'mileage' are input fields for the respective values
        mpg = float(request.form['mpg'])
        engine_size = float(request.form['engine_size'])
        tax = float(request.form['tax'])
        year = float(request.form['year'])
        mileage = float(request.form['mileage'])

        # Preprocess the input values if needed (you may need to adjust this based on your model preprocessing)
        # For example, encode categorical variables or scale numerical features

        # Make a prediction
        input_data = np.array([[mpg, engine_size, tax, year, mileage]])
        prediction_ford = model_ford.predict(input_data)

        # Process the prediction result if needed

        return render_template('index.html', prediction_ford=prediction_ford)


if __name__ == '__main__':
    app.run(debug=True)
