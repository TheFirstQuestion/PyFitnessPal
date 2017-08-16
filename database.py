import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('pyfitnesspal.db')

    def commit(self):
        self.conn.commit()

    def close(self):
        self.conn.commit()
        self.conn.close()

    def basicInsert(self,text):
        print(text)

    def makeNew(self):
        # Create USERS table
        self.conn.execute('''CREATE TABLE USERS
                (ID             INTEGER        PRIMARY KEY      NOT NULL,
                EMAIL           VARCHAR                     ,
                PASSWORD        TEXT                        ,
                AGE             INT                         ,
                SEX             CHAR(1)                     ,
                HEIGHT          INT                         ,
                WEIGHT          INT                         ,
                ACTIVITY        INT                         ,
                NAME            VARCHAR
                 );''')

        # Create EATING table
        self.conn.execute('''CREATE TABLE EATING
               (ID             INTEGER         PRIMARY KEY      NOT NULL,
                USER           INT                          ,
                FOOD           INT                          ,
                MEASURE        INT                          ,
                SERVINGS       INT                          ,
                DAY            TEXT
                 );''')

        # Create NUTRIENTS table
        self.conn.execute('''CREATE TABLE NUTRIENTS
               (ID             INTEGER         PRIMARY KEY      NOT NULL,
                NAME           VARCHAR                      ,
                UNIT           VARCHAR                      ,
                CAT            VARCHAR
                 );''')

        # Add nutrient information
        self.conn.execute("INSERT INTO NUTRIENTS (ID,NAME,UNIT,CAT) \
              VALUES (0, 'Water', 'g', 'Proximates')");

        self.conn.execute("INSERT INTO NUTRIENTS (ID,NAME,UNIT,CAT) \
              VALUES (1, 'Energy', 'calories', 'Proximates')");

        self.conn.execute("INSERT INTO NUTRIENTS (ID,NAME,UNIT,CAT) \
              VALUES (2, 'Protein', 'g', 'Proximates')");

        self.conn.execute("INSERT INTO NUTRIENTS (ID,NAME,UNIT,CAT) \
              VALUES (3, 'Total Lipid (fat)', 'g', 'Proximates')");

        self.conn.execute("INSERT INTO NUTRIENTS (ID,NAME,UNIT,CAT) \
              VALUES (4, 'Carbohydrate', 'g', 'Proximates')");

        self.conn.execute("INSERT INTO NUTRIENTS (ID,NAME,UNIT,CAT) \
              VALUES (5, 'Fiber', 'g', 'Proximates')");

        self.conn.execute("INSERT INTO NUTRIENTS (ID,NAME,UNIT,CAT) \
              VALUES (6, 'Sugars', 'g', 'Proximates')");

        self.conn.execute("INSERT INTO NUTRIENTS (ID,NAME,UNIT,CAT) \
              VALUES (7, 'Calcium', 'mg', 'Minerals')");

        self.conn.execute("INSERT INTO NUTRIENTS (ID,NAME,UNIT,CAT) \
              VALUES (8, 'Iron', 'mg', 'Minerals')");

        self.conn.execute("INSERT INTO NUTRIENTS (ID,NAME,UNIT,CAT) \
              VALUES (9, 'Magnesium', 'mg', 'Minerals')");

        self.conn.execute("INSERT INTO NUTRIENTS (ID,NAME,UNIT,CAT) \
              VALUES (10, 'Phosphorus', 'mg', 'Minerals')");

        self.conn.execute("INSERT INTO NUTRIENTS (ID,NAME,UNIT,CAT) \
              VALUES (11, 'Potassium', 'mg', 'Minerals')");

        self.conn.execute("INSERT INTO NUTRIENTS (ID,NAME,UNIT,CAT) \
              VALUES (12, 'Sodium', 'mg', 'Minerals')");

        self.conn.execute("INSERT INTO NUTRIENTS (ID,NAME,UNIT,CAT) \
              VALUES (13, 'Zinc', 'mg', 'Minerals')");

        self.conn.execute("INSERT INTO NUTRIENTS (ID,NAME,UNIT,CAT) \
              VALUES (14, 'Vitamin C', 'mg', 'Vitamins')");

        self.conn.execute("INSERT INTO NUTRIENTS (ID,NAME,UNIT,CAT) \
              VALUES (15, 'Thiamin', 'mg', 'Vitamins')");

        self.conn.execute("INSERT INTO NUTRIENTS (ID,NAME,UNIT,CAT) \
              VALUES (16, 'Riboflavin', 'mg', 'Vitamins')");

        self.conn.execute("INSERT INTO NUTRIENTS (ID,NAME,UNIT,CAT) \
              VALUES (17, 'Niacin', 'mg', 'Vitamins')");

        self.conn.execute("INSERT INTO NUTRIENTS (ID,NAME,UNIT,CAT) \
              VALUES (18, 'Vitamin B-6', 'mg', 'Vitamins')");

        self.conn.execute("INSERT INTO NUTRIENTS (ID,NAME,UNIT,CAT) \
              VALUES (19, 'Folate', '&#181;g', 'Vitamins')");

        self.conn.execute("INSERT INTO NUTRIENTS (ID,NAME,UNIT,CAT) \
              VALUES (20, 'Vitamin B-12', '&#181;g', 'Vitamins')");

        self.conn.execute("INSERT INTO NUTRIENTS (ID,NAME,UNIT,CAT) \
              VALUES (21, 'Vitamin A, RAE', '&#181;g', 'Vitamins')");

        self.conn.execute("INSERT INTO NUTRIENTS (ID,NAME,UNIT,CAT) \
              VALUES (22, 'Vitamin A, IU', 'IU', 'Vitamins')");

        self.conn.execute("INSERT INTO NUTRIENTS (ID,NAME,UNIT,CAT) \
              VALUES (23, 'Vitamin E', 'mg', 'Vitamins')");

        self.conn.execute("INSERT INTO NUTRIENTS (ID,NAME,UNIT,CAT) \
              VALUES (24, 'Vitamin D (D2 + D3)', '&#181;g', 'Vitamins')");

        self.conn.execute("INSERT INTO NUTRIENTS (ID,NAME,UNIT,CAT) \
              VALUES (25, 'Vitamin D', 'IU', 'Vitamins')");

        self.conn.execute("INSERT INTO NUTRIENTS (ID,NAME,UNIT,CAT) \
              VALUES (26, 'Vitamin K', '&#181;g', 'Vitamins')");

        self.conn.execute("INSERT INTO NUTRIENTS (ID,NAME,UNIT,CAT) \
              VALUES (27, 'Saturated Fat', 'g', 'Lipids')");

        self.conn.execute("INSERT INTO NUTRIENTS (ID,NAME,UNIT,CAT) \
              VALUES (28, 'Monounsaturated Fat', 'g', 'Lipids')");

        self.conn.execute("INSERT INTO NUTRIENTS (ID,NAME,UNIT,CAT) \
              VALUES (29, 'Polyunsaturated Fat', 'g', 'Lipids')");

        self.conn.execute("INSERT INTO NUTRIENTS (ID,NAME,UNIT,CAT) \
              VALUES (30, 'Trans Fat', 'g', 'Lipids')");

        self.conn.execute("INSERT INTO NUTRIENTS (ID,NAME,UNIT,CAT) \
              VALUES (31, 'Cholesterol', 'mg', 'Lipids')");

        self.conn.execute("INSERT INTO NUTRIENTS (ID,NAME,UNIT,CAT) \
              VALUES (32, 'Caffeine', 'mg', 'Other')");

        self.commit()

    def makeTestUsers(self):
        self.conn.execute("INSERT INTO USERS (EMAIL, PASSWORD, AGE, SEX, HEIGHT, WEIGHT, ACTIVITY, NAME) VALUES ('a', 'aaaa', 1, 'F', 1, 1, 1, 'a')")
        self.conn.execute("INSERT INTO USERS (EMAIL, PASSWORD, AGE, SEX, HEIGHT, WEIGHT, ACTIVITY, NAME) VALUES ('b', 'bbbb', 2, 'M', 2, 2, 2, 'b')")
        self.commit()

    def setUserPassword(em, pwd):
        self.conn = sqlite3.connect('pyfitnesspal.db')
        self.conn.execute("INSERT INTO USERS (ID,EMAIL,PASSWORD, AGE, HEIGHT, WEIGHT, ACTIVITY, NAME) \
              VALUES (1, ?, ?, 0, 0, 0, 0, 's')", (em, pwd));
        self.conn.commit()
        self.conn.close()

    def getUserPassword():
        self.conn = sqlite3.connect('pyfitnesspal.db')
        cursor = self.conn.execute("SELECT PASSWORD FROM USERS")
        for row in cursor:
            return row[0]
        self.conn.commit()
        self.conn.close()



if __name__ == "__main__":
    db = Database()
    db.makeNew()
    db.makeTestUsers()
