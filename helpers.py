#### All the routes for the application are in app.py
#### Methods called from routes are in helpers.py
#### Backend methods are in backend.py
#############################################################

import database
import USDADatabase
import databaseUser

# Globals
USDA = USDADatabase.USDADatabase()
USDAcursor = USDA.conn.cursor()
PFP = database.Database()
PFPcursor = PFP.conn.cursor()

########################### USDA Database ########################
def getNutrientLabels():
    USDAcursor.execute("SELECT * FROM NUTR_DEF")
    return USDAcursor.fetchall()


def getNutrientsForFood(thisFood):
    USDAcursor.execute("SELECT * FROM NUT_DATA WHERE NDB_No IS (?)", (thisFood,))
    return USDAcursor.fetchall()

def getAllFoods():
    USDAcursor.execute("SELECT * FROM FOOD_DES")
    return USDAcursor.fetchall()

def getAllWeights():
    USDAcursor.execute("SELECT * FROM WEIGHT")
    data2 = USDAcursor.fetchall()



########################### PFP Database ########################

def getFoodsEaten():
    userID = int(session.get('currentUser')["_User__iden"])
    PFPcursor.execute("SELECT * FROM EATING WHERE USER IS (?)", (userID,))
    return PFPcursor.fetchall()

def addUserToDatabase(a, b, c, d, e, f, g, h):
    # Create user with placeholder values
    newUser = databaseUser.DatabaseUser(a, b, c, d, e, f, g, h)
    # Store in session
    session['newUser'] = newUser.__dict__
