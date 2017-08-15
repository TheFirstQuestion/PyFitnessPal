import database

class User:
    def __init__(self):
        self.db = database.Database()
        email = input("enter your email: ")
        pwd = input("enter your password: ")
        age = input("enter your age: ")
        sex = input("enter your sex: ")
        h = input("enter your height: ")
        w = input("enter your weight: ")
        act = input("enter your activity level: ")
        name = input("enter your name: ")
        self.db.conn.execute("INSERT INTO USERS (EMAIL, PASSWORD, AGE, SEX, HEIGHT, WEIGHT, ACTIVITY, NAME) \
              VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (email, pwd, age, sex, h, w, act, name));

    """def setId(id):

    def setEmail(email):

    def setPassword(pwd):

    def setAge(age):

    def setSex(sex):

    def setHeight(h):

    def setWeight(w):

    def setActivity(act):

    def setName(name):"""


user = User()
