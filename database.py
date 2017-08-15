import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('pyfitnesspal.db')

    def basicStop(self):
        self.conn.commit()
        self.conn.close()

    def basicInsert(self,text):
        print(text)

    def main(self):
        # Create USERS table
        conn.execute('''CREATE TABLE USERS
                (ID             INT        PRIMARY KEY      NOT NULL,
                EMAIL           VARCHAR                     NOT NULL,
                PASSWORD        TEXT                        NOT NULL,
                AGE             INT                         NOT NULL,
                SEX             CHAR(1)                     NOT NULL,
                HEIGHT          INT                         NOT NULL,
                WEIGHT          INT                         NOT NULL,
                ACTIVITY        INT                         NOT NULL,
                NAME            VARCHAR                     NOT NULL
                 );''')

        # Create EATING table
        conn.execute('''CREATE TABLE EATING
               (ID             INT         PRIMARY KEY      NOT NULL,
                USER           INT                          NOT NULL,
                FOOD           INT                          NOT NULL,
                MEASURE        INT                          NOT NULL,
                SERVINGS       INT                          NOT NULL,
                DAY            TEXT                         NOT NULL
                 );''')

        # Create NUTRIENTS table
        conn.execute('''CREATE TABLE NUTRIENTS
               (ID             INT         PRIMARY KEY      NOT NULL,
                NAME           VARCHAR                      NOT NULL,
                UNIT           VARCHAR                      NOT NULL,
                CAT          VARCHAR                      NOT NULL
                 );''')

        # Add nutrient information
        conn.execute("INSERT INTO NUTRIENTS (ID,NAME,UNIT,CAT) \
              VALUES (0, 'Water', 'g', 'Proximates')");

        conn.execute("INSERT INTO NUTRIENTS (ID,NAME,UNIT,CAT) \
              VALUES (1, 'Energy', 'calories', 'Proximates')");

        conn.execute("INSERT INTO NUTRIENTS (ID,NAME,UNIT,CAT) \
              VALUES (2, 'Protein', 'g', 'Proximates')");

        conn.execute("INSERT INTO NUTRIENTS (ID,NAME,UNIT,CAT) \
              VALUES (3, 'Total Lipid (fat)', 'g', 'Proximates')");

        conn.execute("INSERT INTO NUTRIENTS (ID,NAME,UNIT,CAT) \
              VALUES (4, 'Carbohydrate', 'g', 'Proximates')");

        conn.execute("INSERT INTO NUTRIENTS (ID,NAME,UNIT,CAT) \
              VALUES (5, 'Fiber', 'g', 'Proximates')");

        conn.execute("INSERT INTO NUTRIENTS (ID,NAME,UNIT,CAT) \
              VALUES (6, 'Sugars', 'g', 'Proximates')");

        conn.execute("INSERT INTO NUTRIENTS (ID,NAME,UNIT,CAT) \
              VALUES (7, 'Calcium', 'mg', 'Minerals')");

        conn.execute("INSERT INTO NUTRIENTS (ID,NAME,UNIT,CAT) \
              VALUES (8, 'Iron', 'mg', 'Minerals')");

        conn.execute("INSERT INTO NUTRIENTS (ID,NAME,UNIT,CAT) \
              VALUES (9, 'Magnesium', 'mg', 'Minerals')");

        conn.execute("INSERT INTO NUTRIENTS (ID,NAME,UNIT,CAT) \
              VALUES (10, 'Phosphorus', 'mg', 'Minerals')");

        conn.execute("INSERT INTO NUTRIENTS (ID,NAME,UNIT,CAT) \
              VALUES (11, 'Potassium', 'mg', 'Minerals')");

        conn.execute("INSERT INTO NUTRIENTS (ID,NAME,UNIT,CAT) \
              VALUES (12, 'Sodium', 'mg', 'Minerals')");

        conn.execute("INSERT INTO NUTRIENTS (ID,NAME,UNIT,CAT) \
              VALUES (13, 'Zinc', 'mg', 'Minerals')");

        conn.execute("INSERT INTO NUTRIENTS (ID,NAME,UNIT,CAT) \
              VALUES (14, 'Vitamin C', 'mg', 'Vitamins')");

        conn.execute("INSERT INTO NUTRIENTS (ID,NAME,UNIT,CAT) \
              VALUES (15, 'Thiamin', 'mg', 'Vitamins')");

        conn.execute("INSERT INTO NUTRIENTS (ID,NAME,UNIT,CAT) \
              VALUES (16, 'Riboflavin', 'mg', 'Vitamins')");

        conn.execute("INSERT INTO NUTRIENTS (ID,NAME,UNIT,CAT) \
              VALUES (17, 'Niacin', 'mg', 'Vitamins')");

        conn.execute("INSERT INTO NUTRIENTS (ID,NAME,UNIT,CAT) \
              VALUES (18, 'Vitamin B-6', 'mg', 'Vitamins')");

        conn.execute("INSERT INTO NUTRIENTS (ID,NAME,UNIT,CAT) \
              VALUES (19, 'Folate', '&#181;g', 'Vitamins')");

        conn.execute("INSERT INTO NUTRIENTS (ID,NAME,UNIT,CAT) \
              VALUES (20, 'Vitamin B-12', '&#181;g', 'Vitamins')");

        conn.execute("INSERT INTO NUTRIENTS (ID,NAME,UNIT,CAT) \
              VALUES (21, 'Vitamin A, RAE', '&#181;g', 'Vitamins')");

        conn.execute("INSERT INTO NUTRIENTS (ID,NAME,UNIT,CAT) \
              VALUES (22, 'Vitamin A, IU', 'IU', 'Vitamins')");

        conn.execute("INSERT INTO NUTRIENTS (ID,NAME,UNIT,CAT) \
              VALUES (23, 'Vitamin E', 'mg', 'Vitamins')");

        conn.execute("INSERT INTO NUTRIENTS (ID,NAME,UNIT,CAT) \
              VALUES (24, 'Vitamin D (D2 + D3)', '&#181;g', 'Vitamins')");

        conn.execute("INSERT INTO NUTRIENTS (ID,NAME,UNIT,CAT) \
              VALUES (25, 'Vitamin D', 'IU', 'Vitamins')");

        conn.execute("INSERT INTO NUTRIENTS (ID,NAME,UNIT,CAT) \
              VALUES (26, 'Vitamin K', '&#181;g', 'Vitamins')");

        conn.execute("INSERT INTO NUTRIENTS (ID,NAME,UNIT,CAT) \
              VALUES (27, 'Saturated Fat', 'g', 'Lipids')");

        conn.execute("INSERT INTO NUTRIENTS (ID,NAME,UNIT,CAT) \
              VALUES (28, 'Monounsaturated Fat', 'g', 'Lipids')");

        conn.execute("INSERT INTO NUTRIENTS (ID,NAME,UNIT,CAT) \
              VALUES (29, 'Polyunsaturated Fat', 'g', 'Lipids')");

        conn.execute("INSERT INTO NUTRIENTS (ID,NAME,UNIT,CAT) \
              VALUES (30, 'Trans Fat', 'g', 'Lipids')");

        conn.execute("INSERT INTO NUTRIENTS (ID,NAME,UNIT,CAT) \
              VALUES (31, 'Cholesterol', 'mg', 'Lipids')");

        conn.execute("INSERT INTO NUTRIENTS (ID,NAME,UNIT,CAT) \
              VALUES (32, 'Caffeine', 'mg', 'Other')");

        basicStop()

    def setUserPassword(em, pwd):
        conn = sqlite3.connect('pyfitnesspal.db')
        conn.execute("INSERT INTO USERS (ID,EMAIL,PASSWORD, AGE, HEIGHT, WEIGHT, ACTIVITY, NAME) \
              VALUES (1, ?, ?, 0, 0, 0, 0, 's')", (em, pwd));
        conn.commit()
        conn.close()

    def getUserPassword():
        conn = sqlite3.connect('pyfitnesspal.db')
        cursor = conn.execute("SELECT PASSWORD FROM USERS")
        for row in cursor:
            return row[0]
        conn.commit()
        conn.close()



if __name__ == "__main__":
    main()
