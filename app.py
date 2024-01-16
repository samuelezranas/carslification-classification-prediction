from flask import Flask, render_template, request

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

app = Flask(__name__)

dic = {0 : 'SUV',  
       1 : 'bus',
       2 : 'sedan', 
       3 : 'fire engine',
       4 : 'heavy truck',
       5 : 'jeep',
       6 : 'minibus',
       7 : 'racing car',
       8 : 'taxi',
       9 : 'truck'}

model = load_model('modelmobil.h5')

model.make_predict_function()

def predict_label(img):
	i = image.load_img(img, target_size=(224,224))
	i = image.img_to_array(i)/255.0
	i = i.reshape(1, 224,224,3)
	predict_x=model.predict(i)
	classes_x=np.argmax(predict_x,axis=1)
	return dic[classes_x[0]]


# routes
@app.route("/", methods=['GET', 'POST'])
def main():
	return render_template("index.html")


@app.route("/submit", methods = ['GET', 'POST'])
def get_output(): 
	if request.method == 'POST':
		img = request.files['my_image']

		p = predict_label(img)

	return render_template("index.html", prediction = p, img = img)

if __name__ =='__main__':
	#app.debug = True
	app.run(debug = True)