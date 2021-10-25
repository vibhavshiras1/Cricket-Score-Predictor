import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

data = pd.read_csv('ipl_score.csv')

def convert(team):
    team_dict = {'RCB':1,'CSK':2,'DC':3,'MI':4,'KXIP':5,'SRH':6,'RR':7,'KKR':8}
    return team_dict[team]

data['batting_team'] = data['batting_team'].apply(lambda x:convert(x))
data['bowling_team'] = data['bowling_team'].apply(lambda x:convert(x))

x = data.iloc[:,:5]
y = data.iloc[:,-1]

regressor = LinearRegression()
regressor.fit(x,y)

pickle.dump(regressor,open('model.pkl','wb'))

model1 = pickle.load(open('model.pkl','rb'))

score1 = model1.predict([[1,5,88,1,10]])

print(score1)
