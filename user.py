import database
from random import randint

class User:
    def __init__(self):
        self.db = database.Database()
        self.db.makeNew()
        self.db.makeTestUsers()


        self.setIden()


        #email = input("enter your email: ")
        #pwd = input("enter your password: ")
        #age = input("enter your age: ")
        #sex = input("enter your sex: ")
        #h = input("enter your height: ")
        #w = input("enter your weight: ")
        #act = input("enter your activity level: ")
        #name = input("enter your name: ")
        #self.db.conn.execute("INSERT INTO USERS (EMAIL, PASSWORD, AGE, SEX, HEIGHT, WEIGHT, ACTIVITY, NAME) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (email, pwd, age, sex, h, w, act, name))

        #self.setEmail(email)
        #setPassword(pwd)
        #setAge(age)
        #setSex(sex)
        #setHeight(h)
        #setWeight(w)
        #setActivity(act)
        #setName(name)
        #p = "aaaa"
        # Set ID property to what's in database
        #self.setId(self.getId(p), p)

        self.db.close()


    # Setters
    def setIden(self):
        i = randint(2, 999999999)
        cursor = self.conn.execute("SELECT ID FROM USERS")
        do:
            self.__iden = i
            self.db.conn.execute("INSERT INTO USERS (ID) VALUES (?)", (self.__iden,))
        while (row[0] == i)


    #def setEmail(self, email):
        #self.db.conn.execute("UPDATE USERS set EMAIL = ? WHERE ID = ?", (email, self.id(self.password)))
        #self.__email = email

    #def setPassword(self, pwd):


    #def setAge(self, age):

    #def setSex(self, sex):

    #def setHeight(self, h):

    #def setWeight(self, w):

    #def setActivity(self, act):

    #def setName(self, name):


    # Getters
    def getIden(self):
        return self.__iden

    #def getEmail(self):
        #return self.__email

    #def getPassword(self):

    #def getAge(self):

    #def getSex(self):

    #def getHeight(self):

    #def getWeight(self):

    #def getActivity(self):

    #def getName(self):



    # Properties
    iden = property(fget = getIden)
    #email = property(fset = setEmail, fget = setEmail)


if __name__ == "__main__":
    user = User()
