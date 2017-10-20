import flask
import user
import database
import USDADatabase
import databaseUser
import json


app = flask.Flask(__name__)
# Needed for session storage
app.secret_key = 'xyz'


# Simple routes

@app.route("/")
def main():
    # Check if there is a user in the session, then choose which to redirect to
    currentUser = flask.session.get('currentUser')
    if currentUser:
        return flask.render_template('home.html')
    else:
        return flask.render_template('index.html')

@app.route('/showSignUp', methods=['GET', 'POST'])
def showSignUp():
    return flask.render_template('signup.html')

@app.route('/showSignIn', methods=['GET', 'POST'])
def showSignIn():
    return flask.render_template('signin.html')

@app.route('/showNewUser')
def showNewUser():
    return flask.render_template('newuser.html')

@app.route('/home')
def home():
    return flask.render_template('home.html')

@app.route('/nutrition')
def nutrition():
    return flask.render_template('nutrition.html')

@app.route('/add', methods=['POST', 'GET'])
def add():
    USDA = USDADatabase.USDADatabase()
    # Get foods from the DB
    cursor = USDA.conn.cursor()
    cursor.execute("SELECT * FROM FOOD_DES")
    data = cursor.fetchall()

    return flask.render_template('addFood.html', foods=data)




# Backend processing routes

@app.route('/signUp', methods=['POST', 'GET'])
def signUp():
    # Read the posted values from the UI
    _name = flask.request.form['inputName']
    _email = flask.request.form['inputEmail']
    _password = flask.request.form['inputPassword']

    # Validate the received values
    if _name and _email and _password:
        #TODO: add checks for email uniqueness and password length (currently fails)

        # Create user
        newUser = databaseUser.DatabaseUser(_email, _password, "00-00-1800", "Z", "0, 0", 000, 0, _name)
        # Store in session
        flask.session['newUser'] = newUser.__dict__

        # Send URL for setup page
        return flask.url_for('showNewUser')
    else:
        return flask.url_for('showSignUp')




@app.route('/signIn', methods=['POST', 'GET'])
def signIn():
    # Read the posted values from the UI
    _email = flask.request.form['inputEmail']
    _password = flask.request.form['inputPassword']

    # Validate the received values
    if _email and _password:
        # Check login
        db = database.Database()
        possibleUser = db.conn.execute("SELECT * FROM USERS WHERE EMAIL IS (?)", (_email,))
        for x in possibleUser:
            if user.User.verifyPassword(_password, x[2]):
                # Create user
                currentUser = user.User(x[0])
                flask.session['currentUser'] = currentUser.__dict__
                # Send URL for home
                return flask.url_for('home')
            else:
                print("incorrent password")
                return flask.url_for('showSignIn')
    else:
        print("values not good")
        return flask.url_for('showSignIn')




@app.route('/finishReg', methods=['POST', 'GET'])
def finishReg():
    # Read the posted values from the UI
    _dob = flask.request.form['inputDob']
    _sex = flask.request.form['inputSex']
    _height = flask.request.form['inputHeight']
    _weight = flask.request.form['inputWeight']
    _activity = flask.request.form['inputAct']

    # Validate the received values
    if _dob and _sex and _height and _weight and _activity:
        # Create user
        db = database.Database()
        newUser = flask.session.get('newUser')
        passwordHashed = newUser['_DatabaseUser__password']

        # Update fields
        db.conn.execute("UPDATE USERS set PASSWORD = ?, DOB = ?, SEX = ?, HEIGHT = ?, WEIGHT = ?, ACTIVITY = ? WHERE ID IS ?", (passwordHashed, _dob, _sex, _height, _weight, _activity, newUser['_DatabaseUser__iden']))
        db.conn.commit()

        possibleUser = db.conn.execute("SELECT * FROM USERS WHERE ID IS (?)", (newUser['_DatabaseUser__iden'],))
        for x in possibleUser:
            # Create user
            currentUser = user.User(x[0])
            flask.session['currentUser'] = currentUser.__dict__
            # Send URL for home
            return flask.url_for('home')
    else:
        return flask.url_for('showNewUser')




@app.route('/addFood', methods=['POST', 'GET'])
def addFood():
    _food = flask.request.form['food']
    # Add the food as eaten...

    
    return flask.url_for('add')





if __name__ == "__main__":
    app.run()
