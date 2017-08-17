import database
from crypto import crypto
from random import randint

class User:
    def __init__(self):
        self.db = database.Database()
        self.db.makeNew()
        self.db.makeTestUsers()


        # Add basic information
        self.setIden()
        self.email = input("enter your email: ")
        self.password = input("enter your password (must be 8 characters or longer): ")
        self.age = input("enter your age: ")
        self.sex = input("enter your sex (F, M, or X): ")
        self.height = input("enter your height (ft, in): ")
        self.weight = input("enter your weight (lbs): ")
        self.activity = input("""enter your activity level
        1: little
        2: more
        3: even more
        4: lots
        enter here:  """)
        self.name = input("enter your name: ")

        # Make sure all fields are filled
        fields = self.db.conn.execute("SELECT * FROM USERS WHERE ID = (?)", (self.iden,))
        if 



        print("user created")
        #self.verifyPassword()
        self.db.close()

    def verifyPassword(self):
        testPass = input("check password: ")
        print(crypto.verify(testPass, self.password))


    # Setters
    def setIden(self):
        while True:
            # Pick a random number for the ID
            i = randint(1, 999999999)
            self.__iden = i

            try:
                # Try to insert it
                self.db.conn.execute("INSERT INTO USERS (ID) VALUES (?)", (self.__iden,))
            except database.sqlite3.Error as er:
                # If there's an error, say so
                print('error')
            else:
                # If it's unique, end the loop
                break



    def setEmail(self, email):
        # Basic check for validity
        if "@" not in email or "." not in email:
            print("incorrect email address")
            return
        try:
            # Try to insert it
            self.db.conn.execute("UPDATE USERS set EMAIL = ? WHERE ID = ?", (email, self.iden))
        except database.sqlite3.Error as er:
            # If there's an error, say so
            print("error")
            return
        self.__email = email



    def setPassword(self, pwd):
        # Basic check for validity
        if len(pwd) < 8:
            print("pick a longer password")
            return
        # Hash the password
        hashed = crypto.hash(pwd)
        try:
            # Try to insert it
            self.db.conn.execute("UPDATE USERS set PASSWORD = ? WHERE ID = ?", (hashed, self.iden))
        except database.sqlite3.Error as er:
            # If there's an error, say so
            print("error")
            return
        self.__password = hashed


    def setAge(self, age):
        # Convert to int
        age = int(age)
        # Basic check for validity
        if age < 12 or age > 130:
            print("incorrect age")
            return
        try:
            # Try to insert it
            self.db.conn.execute("UPDATE USERS set AGE = ? WHERE ID = ?", (age, self.iden))
        except database.sqlite3.Error as er:
            # If there's an error, say so
            print("error")
            return
        self.__age = age

    def setSex(self, sex):
        # Convert to uppercase
        sex = sex.upper()
        # Basic check for validity
        if sex == "F" or sex == "M" or sex == "X":
            try:
                # Try to insert it
                self.db.conn.execute("UPDATE USERS set SEX = ? WHERE ID = ?", (sex, self.iden))
            except database.sqlite3.Error as er:
                # If there's an error, say so
                print("error")
                return
            self.__sex = sex
            return
        # It hasn't returned, so it's wrong
        print("incorrect sex")

    def setHeight(self, h):
        # Check for the comma
        if "," not in h:
            print("incorrect height")
            return
        # Split into feet and inches
        h = h.split(",")
        # Convert to inches
        heightIn = (int(h[0]) * 12) + int(h[1])
        try:
            # Try to insert it
            self.db.conn.execute("UPDATE USERS set HEIGHT = ? WHERE ID = ?", (heightIn, self.iden))
        except database.sqlite3.Error as er:
            # If there's an error, say so
            print("error")
            return
        self.__height = heightIn

    def setWeight(self, w):
        if type(w) != 'int':
            print("incorrect weight")
            return
        # Convert to int
        w = int(w)
        if w < 75 or w > 1000:
            print("incorrect weight")
            return
        try:
            # Try to insert it
            self.db.conn.execute("UPDATE USERS set WEIGHT = ? WHERE ID = ?", (w, self.iden))
        except database.sqlite3.Error as er:
            # If there's an error, say so
            print("error")
            return
        self.__weight = w

    def setActivity(self, act):
        # Convert to int
        act = int(act)
        # If it not any of the options
        if act != 1 and act != 2 and act != 3 and act != 4:
            print("incorrect activity level")
            return
        try:
            # Try to insert it
            self.db.conn.execute("UPDATE USERS set ACTIVITY = ? WHERE ID = ?", (act, self.iden))
        except database.sqlite3.Error as er:
            # If there's an error, say so
            print("error")
            return
        self.__activity = act

    def setName(self, name):
        try:
            # Try to insert it
            self.db.conn.execute("UPDATE USERS set NAME = ? WHERE ID = ?", (name, self.iden))
        except database.sqlite3.Error as er:
            # If there's an error, say so
            print("error")
            return
        self.__name = name


    # Getters
    def getIden(self):
        return self.__iden

    def getEmail(self):
        return self.__email

    def getPassword(self):
        return self.__password

    def getAge(self):
        return self.__age

    def getSex(self):
        return self.__sex

    def getHeight(self):
        return self.__height

    def getWeight(self):
        return self.__height

    def getActivity(self):
        return self.__activity

    def getName(self):
        return self.__name



    # Properties
    iden = property(fget = getIden)
    email = property(fset = setEmail, fget = getEmail)
    password = property(fset = setPassword, fget = getPassword)
    age = property(fset = setAge, fget = getAge)
    sex = property(fset = setSex, fget = getSex)
    height = property(fset = setHeight, fget = getHeight)
    weight = property(fset = setWeight, fget = getWeight)
    activity = property(fset = setActivity, fget = getActivity)
    name = property(fset = setName, fget = getName)


if __name__ == "__main__":
    user = User()
