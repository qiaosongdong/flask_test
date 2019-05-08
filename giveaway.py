# -*- coding: utf-8 -*-

from flask import Flask, request, render_template
import random

app = Flask(__name__)
candidate = []

@app.route('/roll', methods=['GET'])
def roll_home():
    return render_template('roll.html')
    

@app.route('/giveaway', methods=['GET'])
def giveaway_form():
    return render_template('giveaway.html')

@app.route('/giveaway', methods=['POST'])
def giveaway():
    username = request.form['username']
    print(username)
    #username = str(username)[1:-1]
    if username not in candidate:
        candidate.append(username)
        print(candidate)
        return render_template('signin-ok.html', username=username)
    return render_template('giveaway.html', message='Username exist', username=username)

@app.route('/roll', methods=['POST'])
def roll():
    result = random.choice(candidate)
    return render_template('roll-result.html', username=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
