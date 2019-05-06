from flask import Flask, request, render_template
import random

app = Flask(__name__)
candidate = []

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('form.html')

@app.route('/giveaway', methods=['GET'])
def giveaway_form():
    return render_template('giveaway.html')

@app.route('/giveaway', methods=['POST'])
def giveaway():
    username = request.form['username']
    candidate.append(username)
    if username not in candidate:
        return render_template('signin-ok.html', username=username)
    return render_template('form.html', message='Username exist', username=username)

@app.route('/roll', methods=['GET'])
def roll():
    result = random.choice(candidate)
    return render_template('roll-result.html', username=result)

@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username=='admin' and password=='password':
        return render_template('signin-ok.html', username=username)
    return render_template('form.html', message='Bad username or password', username=username)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
