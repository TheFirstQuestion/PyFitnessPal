#### All the routes for the application are in app.py
#### Methods called from routes are in helpers.py
#### Backend methods are in backend.py
#############################################################

from flask import *
from helpers import *

# To be imported into app.py
backendApp = Blueprint('backendApp', __name__, template_folder='templates', static_folder='static')


@backendApp.route('/signUp', methods=['POST', 'GET'])
def signUp():
    # Read the posted values from the UI
    _name = request.form['inputName']
    _email = request.form['inputEmail']
    _password = request.form['inputPassword']

    # Validate the received values
    if _name and _email and _password:
        # Create user with placeholder values
        addUserToDatabase(_email, _password, "00-00-1800", "Z", "0, 0", 000, 0, _name)
        # Send URL for setup page
        return url_for('showNewUser')
    else:
        return url_for('showSignUp')




@backendApp.route('/signIn', methods=['POST', 'GET'])
def signIn():
    # Read the posted values from the UI
    _email = request.form['inputEmail']
    _password = request.form['inputPassword']

    # Validate the received values
    if _email and _password:
        # Check login
        db = database.Database()
        possibleUser = db.conn.execute("SELECT * FROM USERS WHERE EMAIL IS (?)", (_email,))
        for x in possibleUser:
            if user.User.verifyPassword(_password, x[2]):
                # Create user
                currentUser = user.User(x[0])
                session['currentUser'] = currentUser.__dict__
                # Send URL for home
                return url_for('home')
            else:
                print("incorrent password")
                return url_for('showSignIn')
    else:
        print("values not good")
        return url_for('showSignIn')




@backendApp.route('/finishReg', methods=['POST', 'GET'])
def finishReg():
    # Read the posted values from the UI
    _dob = request.form['inputDob']
    _sex = request.form['inputSex']
    _height = request.form['inputHeight']
    _weight = request.form['inputWeight']
    _activity = request.form['inputAct']

    # Validate the received values
    if _dob and _sex and _height and _weight and _activity:
        # Create user
        db = database.Database()
        newUser = session.get('newUser')
        passwordHashed = newUser['_DatabaseUser__password']

        # Update fields
        db.conn.execute("UPDATE USERS set PASSWORD = ?, DOB = ?, SEX = ?, HEIGHT = ?, WEIGHT = ?, ACTIVITY = ? WHERE ID IS ?", (passwordHashed, _dob, _sex, _height, _weight, _activity, newUser['_DatabaseUser__iden']))
        db.conn.commit()

        possibleUser = db.conn.execute("SELECT * FROM USERS WHERE ID IS (?)", (newUser['_DatabaseUser__iden'],))
        for x in possibleUser:
            # Create user
            currentUser = user.User(x[0])
            session['currentUser'] = currentUser.__dict__
            # Send URL for home
            return url_for('home')
    else:
        return url_for('showNewUser')




@backendApp.route('/addFood', methods=['POST', 'GET'])
def addFood():
    _food = request.form['food']
    _measure = request.form['measure']
    _servings = request.form['servings']

    USDA = USDADatabase.USDADatabase()
    # Get food from the DB
    cursor = USDA.conn.cursor()
    cursor.execute("SELECT * FROM FOOD_DES WHERE Long_Desc IS ?", (_food,))
    foodFull = cursor.fetchall()

    foodID = int(foodFull[0][0])

    # Get measures from the DB
    cursor.execute("SELECT * FROM WEIGHT")
    measureFull = cursor.fetchall()

    selectedMeasure = 0;

    for i in range(0, len(measureFull)):
        if measureFull[i][4] == _measure:
            selectedMeasure = measureFull[i]
            break

    print(selectedMeasure)

    # Add event to the DB
    userID = int(session.get('currentUser')["_User__iden"])
    measure = int(float(selectedMeasure[4]))
    servings = int(_servings)
    day = now.strftime("%m-%d-%Y")

    db = database.Database()
    db.conn.execute("INSERT INTO EATING (USER, FOOD, MEASURE, SERVINGS, DAY) VALUES (?, ?, ?, ?, ?)", (userID, foodID, measure, servings, day))
    db.commit()

    return url_for('add')
