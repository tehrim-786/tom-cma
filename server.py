from flask import Flask,render_template,request,flash
# from urllib import request
import cv2

import tensorflow
from tensorflow.keras.models import load_model
import numpy as np

international = load_model('models/int_2_Class_4.model')
pakistani = load_model('models/176_2.model')

def internationalPredict(path):
    
    
    image = cv2.imread(path)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image_rgb= cv2.resize(image_rgb,(416,416))
    image_rgb= image_rgb.reshape(1,416,416,3)
    
    return np.argmax(international.predict(image_rgb))

def pakistanPredict(path):
    image = cv2.imread(path)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image_rgb= cv2.resize(image_rgb,(416,416))
    image_rgb= image_rgb.reshape(1,416,416,3)
    
    return np.argmax(pakistani.predict(image_rgb))


app = Flask(__name__)


@app.route('/',methods=['GET','POST'])
def home():
    return render_template('fyp.html')

@app.route('/converter',methods=['GET','POST'])
def converter():
    return render_template('converter.html')
@app.route('/detection',methods=['GET','POST'])
def detection():
    return render_template('pic.html')
@app.post('/international')
def predict1():
    if request.method == 'POST':
        
        img = request.files['image']
        img_path = 'static/'+img.filename
        img.save(img_path)
        
        
        p = internationalPredict(img_path)
    return render_template('fyp.html',inter=p,img_path = img_path)
@app.post('/pakistan')
def predict2():
    if request.method == 'POST':
        
        img = request.files['image']
        img_path = 'static/'+img.filename
        img.save(img_path)
        
        
        p = pakistanPredict(img_path)
    return render_template('fyp.html',pak=p,img_path = img_path)
if __name__ == '__main__':
    app.run(debug=True)
    