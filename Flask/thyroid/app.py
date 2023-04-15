from flask import Flask, request, render_template
app = Flask(__name__, template_folder='templates')
import pickle
import numpy as np
import pandas as pd

model = pickle.load(open('thyroid_prediction.pickle', 'rb'))

app = Flask(__name__)

@app.route('/')
def about():
    return render_template('home.html')
    return render_template('img.jpg')
    return render_template('style.css')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/predict')
def predict():
    return render_template('predict')

@app.route('/pred', methods = ['POST'])
def pred():
    goitre = request.form['goitre']
    tumor = request.form['tumor']
    hypopituitary = request.form['hypopituitary']
    psych = request.form['psych']
    tsh = request.form['tsh']
    t3 = request.form['t3']
    tt4 = request.form['tt4']
    t4u = request.form['t4u']
    fti = request.form['fti']
    tbg = request.form['tbg']
    variables = [[int(goitre),int(tumor),int(hypopituitary),int(psych),int(tsh),int(t3),int(tt4),int(t4u),int(fti),int(tbg)]]
    print(variables)
    print(model.predict(variables))
    output = model.predict(variables)
    return render_template('submit.html',prediction_text = output[0])

if __name__=='__main__':
    app.run()