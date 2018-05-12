#### All the routes for the application are in app.py
#### Methods called from routes are in helpers.py
#### Backend methods are in backend.py
#############################################################

from flask import *
from backend import backendApp
from helpers import *


app = Flask(__name__)
# For multi-page routes
# https://stackoverflow.com/questions/11994325/how-to-divide-flask-app-into-multiple-py-files
app.register_blueprint(backendApp)

# Needed for session storage
app.secret_key = 'xyz'

@app.route("/")
def main():
    # Check if there is a user in the session, then choose which to redirect to
    currentUser = session.get('currentUser')
    if currentUser:
        return render_template('home.html')
    else:
        return render_template('index.html')

@app.route('/showSignUp', methods=['GET', 'POST'])
def showSignUp():
    return render_template('signup.html')

@app.route('/showSignIn', methods=['GET', 'POST'])
def showSignIn():
    return render_template('signin.html')

@app.route('/showNewUser')
def showNewUser():
    return render_template('newuser.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/nutrition')
def nutrition():
    labels = getNutrientLabels()
    foods = getFoodsEaten()
    # 2D array of nutrients for each food
    allNutrients = []
    for x in foods:
        allNutrients.append(getNutrientsForFood(x[2]))
    return render_template('nutrition.html', labels=labels, nutrients=allNutrients)

@app.route('/add', methods=['POST', 'GET'])
def add():
    return render_template('addFood.html', foods=getAllFoods(), weights=getAllWeights())



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
