from flask import Flask, render_template, json, request
import user
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

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
        u = user.User("x@eoioei.com", "jdjdjdjdjd", "01-01-2001", "F", "5, 11", "100", "2", "oiwjeoir")
        return json.dumps({'html':'noice'})
    else:
        return json.dumps({'html':'whoops'})

if __name__ == "__main__":
    app.run()
