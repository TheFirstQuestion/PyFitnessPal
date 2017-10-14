import flask
import user
import database
import databaseUser


app = flask.Flask(__name__)
# Needed for session storage
app.secret_key = 'xyz'


# Simple routes

@app.route("/")
def main():
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

        # Delete user from database (we'll make a new one with correct fields later)
        db = database.Database()
        db.conn.execute("DELETE FROM USERS WHERE EMAIL IS (?)", (_email,))
        db.commit()

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
        makeNewUser = databaseUser.DatabaseUser(newUser['_DatabaseUser__email'], "xXxXxXxXxXxXx", _dob, _sex, _height, _weight, _activity, newUser['_DatabaseUser__name'])

        # Set password, without rehashing it
        db.conn.execute("UPDATE USERS set PASSWORD = ? WHERE EMAIL IS ?", (passwordHashed, newUser['_DatabaseUser__email']))
        db.conn.commit()

        possibleUser = db.conn.execute("SELECT * FROM USERS WHERE EMAIL IS (?)", (newUser['_DatabaseUser__email'],))
        for x in possibleUser:
            # Create user
            currentUser = user.User(x[0])
            flask.session['currentUser'] = currentUser.__dict__
            # Send URL for home
            return flask.url_for('home')
    else:
        return flask.url_for('showNewUser')








if __name__ == "__main__":
    app.run()
