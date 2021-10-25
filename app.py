import pickle
import re
from flask import Flask, render_template, request
from flask.helpers import flash

app = Flask(__name__)
model1 = pickle.load(open('model.pkl','rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_score',methods=['POST'])
def predict_score():
    bat_team = request.form['batting_team']
    bowl_team = request.form['bowling_team']
    if(bat_team==bowl_team):
        return render_template('home.html',output_text='The batting team and the bowling team cannot be the same.')
    elif(bat_team=='select' or bowl_team=='select'):
        return render_template('home.html',output_text='Please fill all the blanks.')
    else:
        score = int(request.form['score'])
        wickets = int(request.form['wickets'])
        overs = int(request.form['overs'])
        pred = model1.predict([[bat_team,bowl_team,score,wickets,overs]])
        output = int(pred)
        return render_template('home.html',output_text='Predicted Score : {}'.format(output))

if __name__=="__main__":
    app.run(debug=True)