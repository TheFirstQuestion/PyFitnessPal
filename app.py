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
def showSignin():
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
        # Create user
        u = databaseUser.DatabaseUser(_email, _password, "01-01-2001", "F", "5, 11", 100, 2, _name)
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
                return flask.url_for('showSignIn')
    else:
        return flask.url_for('showSignIn')










if __name__ == "__main__":
    app.run()
