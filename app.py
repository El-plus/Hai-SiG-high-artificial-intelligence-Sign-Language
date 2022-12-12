from flask import Flask, render_template, request
import pickle

from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from tensorflow.keras.applications.vgg16 import preprocess_input
from tensorflow.keras.applications.vgg16 import decode_predictions
from tensorflow.keras.applications.vgg16 import VGG16


app = Flask(__name__)
moddel = pickle.load(open('model.pkl', 'rb'))

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def predict():
    imagefile = request.files['imagefile']
    image_path = "./images/" + imagefile.filename
    imagefile.save(image_path)

    image = load_img(image_path, target_size=(150, 150))
    image = img_to_array(image)
    image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
    image = preprcoess_input(image)
    vgg_model = model.predict(image)
    label = decode_predictions(vgg_model)
    label = label[0][0]

    classifcation = '%s (%.2f%%)' % (label[1], label[2]*100)

    return render_template('index.html', prediction=classifcation)

if __name__ == '__main__':
    app.run(port=3000, debug=True)

