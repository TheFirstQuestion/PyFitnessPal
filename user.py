import database
from crypto import crypto
from random import randint

class User:
    db = database.Database()
    
    def __init__(self, iden):

        # Get this user from the database
        users = User.db.conn.execute("SELECT * FROM USERS WHERE ID IS (?)", (iden,))

        self.setIden(iden)
        for user in users:
            self.email = user[1]
            self.password = user[2]
            self.dob = user[3]
            self.sex = user[4]
            self.height = user[5]
            self.weight = user[6]
            self.activity = user[7]
            self.name = user[8]

        User.db.close()


    # Static method to verify passwords
    @staticmethod
    def verifyPassword(testPass, realPass):
        return crypto.verify(testPass, realPass)


    # Setters
    def setIden(self, iden):
        self.__iden = iden

    def setEmail(self, email):
        self.__email = email

    def setPassword(self, pwd):
        self.__password = pwd

    def setDob(self, dob):
        self.__dob = dob

    def setSex(self, sex):
        self.__sex = sex

    def setHeight(self, h):
        self.__height = h

    def setWeight(self, w):
        self.__weight = w

    def setActivity(self, act):
        self.__activity = act

    def setName(self, name):
        self.__name = name



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
        return self.__weight

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
    user = User(1)
    l = dir(user)
    d = user.__dict__
    # Print attributes and values of the object
    print(d)
