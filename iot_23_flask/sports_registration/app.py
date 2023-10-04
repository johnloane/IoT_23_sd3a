from flask import Flask, render_template, request, redirect
import os
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST')
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = os.getenv('MYSQL_DB')

mysql = MySQL(app)


SPORTS = ["Basketball", "Football", "Tennis", "Badminton", "Hockey"]

@app.route('/')
def index():
    return render_template('index.html', sports = SPORTS)


@app.route('/register', methods=['POST'])
def register():
    #Server side validation
    name = request.form.get('name')
    sport = request.form.get('sport')
    if not name:
        return render_template('error.html', message="Missing name")
    if not sport:
        return render_template('error.html', message="Missing sport")
    if not sport in SPORTS:
        return render_template('error.html', message="Invalid sport. Stop hacking my server")
    cursor = mysql.connection.cursor()
    cursor.execute("Select id from registrant where name = %s and sport = %s", 
                   (name, sport))
    result = cursor.fetchall()
    if len(result) != 0:
        cursor.close()
        return render_template('error.html', message="You have already registered")  
    cursor.execute("INSERT INTO registrant (name, sport) VALUES (%s, %s)", 
                   (name, sport)) 
    mysql.connection.commit()
    cursor.close() 
    return redirect('/registrants')


@app.route('/registrants')
def registrants():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM registrant")
    registrants = cursor.fetchall()
    cursor.close()
    return render_template('registrants.html', registrants=registrants)


@app.route('/deregister', methods=['POST'])
def deregister():
    id = request.form.get('id')
    if id:
        cursor = mysql.connection.cursor()
        cursor.execute("DELETE FROM registrant WHERE id = %s", (id))
        mysql.connection.commit()
        cursor.close()
    return redirect('/registrants')