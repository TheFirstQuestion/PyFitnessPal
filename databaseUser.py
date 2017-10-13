import database
from crypto import crypto
from random import randint

class DatabaseUser:
    db = database.Database()

    def __init__(self, email, passw, dob, sex, h, w, act, name):
        # Add basic information
        self.setIden()
        self.email = email
        self.password = passw
        self.dob = dob
        self.sex = sex
        self.height = h
        self.weight = w
        self.activity = act
        self.name = name


        DatabaseUser.db.close()


    # Setters
    def setIden(self):
        while True:
            # Pick a random number for the ID
            i = randint(1, 999999999)
            self.__iden = i

            try:
                # Try to insert it
                DatabaseUser.db.conn.execute("INSERT INTO USERS (ID) VALUES (?)", (self.__iden,))
            except database.sqlite3.Error as er:
                # If there's an error, set marker
                print('error')
            else:
                # If it's unique, end the loop
                break



    def setEmail(self, email):
        # Basic check for validity
        if "@" not in email or "." not in email:
            print("incorrect email address")
            self.__email = "xXx"
            return
        try:
            # Try to insert it
            DatabaseUser.db.conn.execute("UPDATE USERS set EMAIL = ? WHERE ID = ?", (email, self.iden))
            self.__email = email
        except database.sqlite3.Error as er:
            # If there's an error, set marker
            DatabaseUser.db.conn.execute("UPDATE USERS set EMAIL = ? WHERE ID = ?", ("xXx", self.iden))
            self.__email = "xXx"
            return

    def setPassword(self, pwd):
        # Basic check for validity
        if len(pwd) < 8:
            print("pick a longer password")
            self.__password = "xXx"
            return
        # Hash the password
        hashed = crypto.hash(pwd)
        try:
            # Try to insert it
            DatabaseUser.db.conn.execute("UPDATE USERS set PASSWORD = ? WHERE ID = ?", (hashed, self.iden))
            self.__password = hashed
        except database.sqlite3.Error as er:
            # If there's an error, set marker
            DatabaseUser.db.conn.execute("UPDATE USERS set PASSWORD = ? WHERE ID = ?", ("xXx", self.iden))
            self.__password = "xXx"
            return

    def setDob(self, dob):
        # Basic check for validity
        if "-" not in dob:
            print("incorrect dob")
            self.__dob = "xXx"
            return
        ####### Probably should do some sort of age check here
        try:
            # Try to insert it
            DatabaseUser.db.conn.execute("UPDATE USERS set DOB = ? WHERE ID = ?", (dob, self.iden))
            self.__dob = dob
        except database.sqlite3.Error as er:
            # If there's an error, set marker
            DatabaseUser.db.conn.execute("UPDATE USERS set DOB = ? WHERE ID = ?", ("xXx", self.iden))
            self.__dob = "xXx"
            return

    def setSex(self, sex):
        # Convert to uppercase
        sex = sex.upper()
        # Basic check for validity
        if sex == "F" or sex == "M" or sex == "X":
            try:
                # Try to insert it
                DatabaseUser.db.conn.execute("UPDATE USERS set SEX = ? WHERE ID = ?", (sex, self.iden))
            except database.sqlite3.Error as er:
                # If there's an error, set marker
                DatabaseUser.db.conn.execute("UPDATE USERS set SEX = ? WHERE ID = ?", ("xXx", self.iden))
                self.__sex = "xXx"
                return
            self.__sex = sex
            return
        # It hasn't returned, so it's wrong
        print("incorrect sex")
        self.__sex = "xXx"

    def setHeight(self, h):
        # Check for the comma
        if "," not in h:
            print("incorrect height")
            self.__height = "xXx"
            return
        # Split into feet and inches
        h = h.split(",")
        # Convert to inches
        heightIn = (int(h[0]) * 12) + int(h[1])
        try:
            # Try to insert it
            DatabaseUser.db.conn.execute("UPDATE USERS set HEIGHT = ? WHERE ID = ?", (heightIn, self.iden))
            self.__height = heightIn
        except database.sqlite3.Error as er:
            # If there's an error, set marker
            DatabaseUser.db.conn.execute("UPDATE USERS set HEIGHT = ? WHERE ID = ?", ("xXx", self.iden))
            self.__height = "xXx"
            return

    def setWeight(self, w):
        """if type(w) != 'int':
            print("incorrect weight--data type")
            self.__weight = "xXx"
            return"""
        # Convert to int
        w = int(w)
        if w < 75 or w > 1000:
            print("incorrect weight--value")
            self.__weight = "xXx"
            return
        try:
            # Try to insert it
            DatabaseUser.db.conn.execute("UPDATE USERS set WEIGHT = ? WHERE ID = ?", (w, self.iden))
            self.__weight = w
        except database.sqlite3.Error as er:
            # If there's an error, set marker
            DatabaseUser.db.conn.execute("UPDATE USERS set WEIGHT = ? WHERE ID = ?", ("xXx", self.iden))
            self.__weight = "xXx"
            return

    def setActivity(self, act):
        # Convert to int
        try:
            act = int(act)
        except:
            print("incorrect activity level")
            self.__activity = "xXx"
            return
        # If it not any of the options
        if act != 1 and act != 2 and act != 3 and act != 4:
            print("incorrect activity level")
            self.__activity = "xXx"
            return
        try:
            # Try to insert it
            DatabaseUser.db.conn.execute("UPDATE USERS set ACTIVITY = ? WHERE ID = ?", (act, self.iden))
            self.__activity = act
        except database.sqlite3.Error as er:
            # If there's an error, set marker
            DatabaseUser.db.conn.execute("UPDATE USERS set ACTIVITY = ? WHERE ID = ?", ("xXx", self.iden))
            self.__activity = "xXx"
            return

    def setName(self, name):
        try:
            # Try to insert it
            DatabaseUser.db.conn.execute("UPDATE USERS set NAME = ? WHERE ID = ?", (name, self.iden))
            self.__name = name
        except database.sqlite3.Error as er:
            # If there's an error, set marker
            DatabaseUser.db.conn.execute("UPDATE USERS set NAME = ? WHERE ID = ?", ("xXx", self.iden))
            self.__name = "xXx"
            return



    # Getters
    def getIden(self):
        return self.__iden

    def getEmail(self):
        return self.__email

    def getPassword(self):
        return self.__password

    def getDob(self):
        return self.__dob

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
    dob = property(fset = setDob, fget = getDob)
    sex = property(fset = setSex, fget = getSex)
    height = property(fset = setHeight, fget = getHeight)
    weight = property(fset = setWeight, fget = getWeight)
    activity = property(fset = setActivity, fget = getActivity)
    name = property(fset = setName, fget = getName)


if __name__ == "__main__":
    self.email = input("enter your email: ")
    self.password = input("enter your password (must be 8 characters or longer): ")
    self.dob = input("enter your date of birth (YYYY-MM-DD): ")
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

    user = User()
