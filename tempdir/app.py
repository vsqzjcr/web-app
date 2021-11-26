from flask import Flask, url_for, redirect
from flask import request
from flask import render_template
app = Flask(__name__)
@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
 return render_template('index.html')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('index'))

    # show the form, it wasn't submitted
    return render_template('login.html')
@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('index'))

    # show the form, it wasn't submitted
    return render_template('registration.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)

