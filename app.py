from flask import Flask, jsonify
from faker import Faker

import pandas as pd
import requests

fake = Faker()
app = Flask(__name__)


#task1
@app.route('/requieremets/')
def req_file():
    a = open('requirements.txt', 'r')
    return a.read()


#task2
@app.route('/generate-users/')
def g_users():
    users = [''.join(fake.name() + fake.ascii_email()) for i in range(100)]
    return jsonify(users)

#task3
@app.route('/mean/')
def mean():
    df = pd.read_csv('hw.csv')
    height = (df[' "Height(Inches)"'].sum() / len(df.index)) * 2.54
    weight = (df[' "Weight(Pounds)"'].sum() / len(df.index)) * 0.453592
    return 'Средний рост: ' + str(height) + ' см. ' + '<br>' + ' Средний вес: ' + str(weight) + ' Кг.'


#task4
@app.route('/space/')
def space():
    cos = requests.get('http://api.open-notify.org/astros.json')
    a = cos.json()['number']
    return 'Космонавтов:' + str(a)

if __name__ == '__main__':
    app.run()
