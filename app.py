from flask import Flask, render_template, json, request
import user
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('header.html')

@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')

@app.route('/signUp', methods=['POST'])
def signUp():

    # read the posted values from the UI
    _name = request.form['inputName']
    _email = request.form['inputEmail']
    _password = request.form['inputPassword']

    # validate the received values
    if _name and _email and _password:
        u = user.User(_email, _password, "01-01-2001", "F", "5, 11", "100", "2", _name)
        return json.dumps({'html':'noice'})
    else:
        return json.dumps({'html':'whoops'})

@app.route('/showSignin')
def showSignin():
    return render_template('signin.html')

if __name__ == "__main__":
    app.run()
