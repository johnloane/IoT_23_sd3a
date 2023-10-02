from flask import Flask, render_template, request 

app = Flask(__name__)

SPORTS = ["Basketball", "Football", "Tennis", "Badminton", "Hockey"]
REGISTRANTS = {}

@app.route('/')
def index():
    return render_template('index.html', sports = SPORTS)


@app.route('/register', methods=['POST'])
def register():
    #Server side validation
    name = request.form.get('name')
    sport = request.form.get('sport')
    if not name or not sport in SPORTS:
        return render_template('failure.html')
    REGISTRANTS[name] = sport
    return render_template('registrants.html', registrants=REGISTRANTS)