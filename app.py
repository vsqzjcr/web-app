from flask import Flask, url_for, redirect
from flask import request
from flask import render_template
import sqlite3 as sql
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user_data'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
ma = Marshmallow(app)

class User(db.Model):
    __tablename__="user"
    user_id = db.Column(db.String(50), primary_key = True)
    user_username = db.Column(db.String(50))
    user_password = db.Column(db.String(50))
    user_email = db.Column(db.String(50))

    def __init__(self,user_id,user_username,user_password,user_email):
        self.user_id = user_id
        self.user_username = user_username
        self.user_password = user_password
        self.user_email = user_email
    
class UserSchema(ma.Schema):
    class Meta:
        fields = ("user_id", "user_username", "user_password", "user_email")

user_schema = UserSchema()
users_schema = UserSchema(many = True)

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    return render_template('dashboard.html')

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
 return render_template('index.html')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form["username"]
        password = request.form["password"]

        con = sql.connect("user_data")
        con.row_factory = sql.Row

        cur = con.cursor()

        cur.execute("select * from user where user_username ='{}' and user_password='{}';".format(username, password))

        user = cur.fetchone()

        if (user is None):
            return render_template("login.html")
        else:
            if (len(user) > 0):
                return redirect(url_for("dashboard"))
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else

    # show the form, it wasn't submitted
    return render_template('login.html')
@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        name = request.form.get('name')
        username = request.form.get('username')
        password = request.form.get('password')
        password2 = request.form.get('password2')
        email = request.form.get('email')

        if password != password2:
            error = "Password does not match"
            
        else:
            new_user = User(name,username,password,email)
            db.session.add(new_user)
            db.session.commit()
        # do stuff when the form is submitted
        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
            return redirect(url_for('login'))
            return user_schema.jsonify(new_user)

    # show the form, it wasn't submitted
    return render_template('registration.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)

