import re

from flask import Flask, render_template, request, url_for, session
from flask_mysqldb import MySQL
from werkzeug.utils import redirect

app = Flask(__name__)
app.secret_key = "secret key"

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Shiva@1995'
app.config['MYSQL_DB'] = 'tracker'

mysql = MySQL(app)


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        cur = mysql.connection.cursor()
        cur.execute(
            "CREATE TABLE IF NOT EXISTS MyUsers (Name VARCHAR(40),Email VARCHAR(40) UNIQUE, Username VARCHAR(40), Password VARCHAR(40))")
        cur.execute('SELECT * FROM MyUsers WHERE username = % s', (username,))
        myuser = cur.fetchone()
        cur.execute('SELECT * FROM MyUsers WHERE email = % s', (email,))
        myuser1 = cur.fetchone()
        if myuser:
            msg = 'Account already exists !'
        elif myuser1:
            msg = 'Email Already exist!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address !'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers !'
        elif not username or not password or not email:
            msg = 'Please fill out the form !'
        else:
            cur.execute("INSERT INTO MyUsers(Name, Email, Username, Password) VALUES (%s, %s, %s, %s);",(name, email, username, password))
            mysql.connection.commit()
            cur.close()
            msg = 'You have successfully registered !'
            msgs = True
            return render_template("index.html", msg=msg , msgs =msgs)
        msgs = True
        return render_template('signup.html', msg =msg, msgs = msgs )

    return render_template("index.html")


@app.route("/signup")
def signup():
    return render_template("signup.html")


@app.route("/loggedin", methods=['GET', 'POST'])
def loggedin():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM MyUsers WHERE username = % s AND password = % s", (username, password))
        myuser = cur.fetchone()
        if myuser:
            session['loggedin'] = True
            # session[id] = myuser['id']
            # session[username] = myuser['username']
            username = request.form['username']
            msg = 'Logged in successfully !'
            msgs = True
            return render_template('loggedin.html', msg=msg, msgs=msgs, username=username)
        else:
            msg = 'Incorrect username / password !'
    msgs = True
    return render_template('index.html', msg=msg, msgs=msgs)


@app.route('/logout', methods = ['GET','POST'])
def logout():
    session.pop('loggedin', None)
    msg = 'you have logged out!!!'
    lmsgs = True
    return render_template('index.html', msg=msg, lmsgs=lmsgs)


if __name__ == "__main__":
    app.run(debug=True)
