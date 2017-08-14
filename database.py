import sqlite3

conn = sqlite3.connect('pyfitnesspal.db')
print("Opened database successfully")

# Create USERS table
conn.execute('''CREATE TABLE USERS
        (ID             INT        PRIMARY KEY      NOT NULL,
        EMAIL           VARCHAR                     NOT NULL,
        PASSWORD        TEXT                        NOT NULL,
        AGE             INT                         NOT NULL,
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
        UNIT           VARCHAR                      NOT NULL
         );''')



# Add nutrient information
conn.execute("INSERT INTO NUTRIENTS (ID,NAME,UNIT) \
      VALUES (0, 'Water', 'g')");

conn.execute("INSERT INTO NUTRIENTS (ID,NAME,UNIT) \
      VALUES (1, 'Energy', 'calories')");

conn.execute("INSERT INTO NUTRIENTS (ID,NAME,UNIT) \
      VALUES (2, 'Protein', 'g')");

conn.execute("INSERT INTO NUTRIENTS (ID,NAME,UNIT) \
      VALUES (3, 'Total Lipid (fat)', 'g')");

conn.execute("INSERT INTO NUTRIENTS (ID,NAME,UNIT) \
      VALUES (4, 'Carbohydrate', 'g')");

conn.execute("INSERT INTO NUTRIENTS (ID,NAME,UNIT) \
      VALUES (5, 'Fiber', 'g')");

conn.execute("INSERT INTO NUTRIENTS (ID,NAME,UNIT) \
      VALUES (6, 'Sugars', 'g')");

conn.execute("INSERT INTO NUTRIENTS (ID,NAME,UNIT) \
      VALUES (7, 'Calcium', 'mg')");

conn.execute("INSERT INTO NUTRIENTS (ID,NAME,UNIT) \
      VALUES (8, 'Iron', 'mg')");

conn.execute("INSERT INTO NUTRIENTS (ID,NAME,UNIT) \
      VALUES (9, 'Magnesium', 'mg')");

conn.execute("INSERT INTO NUTRIENTS (ID,NAME,UNIT) \
      VALUES (10, 'Phosphorus', 'mg')");

conn.execute("INSERT INTO NUTRIENTS (ID,NAME,UNIT) \
      VALUES (11, 'Potassium', 'mg')");

conn.execute("INSERT INTO NUTRIENTS (ID,NAME,UNIT) \
      VALUES (12, 'Sodium', 'mg')");

conn.execute("INSERT INTO NUTRIENTS (ID,NAME,UNIT) \
      VALUES (13, 'Zinc', 'mg')");

conn.execute("INSERT INTO NUTRIENTS (ID,NAME,UNIT) \
      VALUES (14, 'Vitamin C', 'mg')");

conn.execute("INSERT INTO NUTRIENTS (ID,NAME,UNIT) \
      VALUES (15, 'Thiamin', 'mg')");

conn.execute("INSERT INTO NUTRIENTS (ID,NAME,UNIT) \
      VALUES (16, 'Riboflavin', 'mg')");

conn.execute("INSERT INTO NUTRIENTS (ID,NAME,UNIT) \
      VALUES (17, 'Niacin', 'mg')");

conn.execute("INSERT INTO NUTRIENTS (ID,NAME,UNIT) \
      VALUES (18, 'Vitamin B-6', 'mg')");

conn.execute("INSERT INTO NUTRIENTS (ID,NAME,UNIT) \
      VALUES (19, 'Folate', '&#181;g')");

conn.execute("INSERT INTO NUTRIENTS (ID,NAME,UNIT) \
      VALUES (20, 'Vitamin B-12', '&#181;g')");

conn.execute("INSERT INTO NUTRIENTS (ID,NAME,UNIT) \
      VALUES (21, 'Vitamin A, RAE', '&#181;g')");

conn.execute("INSERT INTO NUTRIENTS (ID,NAME,UNIT) \
      VALUES (22, 'Vitamin A, IU', 'IU')");

conn.execute("INSERT INTO NUTRIENTS (ID,NAME,UNIT) \
      VALUES (23, 'Vitamin E', 'mg')");

conn.execute("INSERT INTO NUTRIENTS (ID,NAME,UNIT) \
      VALUES (24, 'Vitamin D (D2 + D3)', '&#181;g')");

conn.execute("INSERT INTO NUTRIENTS (ID,NAME,UNIT) \
      VALUES (25, 'Vitamin D', 'IU')");

conn.execute("INSERT INTO NUTRIENTS (ID,NAME,UNIT) \
      VALUES (26, 'Vitamin K', '&#181;g')");

conn.execute("INSERT INTO NUTRIENTS (ID,NAME,UNIT) \
      VALUES (27, 'Saturated Fat', 'g')");

conn.execute("INSERT INTO NUTRIENTS (ID,NAME,UNIT) \
      VALUES (28, 'Monounsaturated Fat', 'g')");

conn.execute("INSERT INTO NUTRIENTS (ID,NAME,UNIT) \
      VALUES (29, 'Polyunsaturated Fat', 'g')");

conn.execute("INSERT INTO NUTRIENTS (ID,NAME,UNIT) \
      VALUES (30, 'Trans Fat', 'g')");

conn.execute("INSERT INTO NUTRIENTS (ID,NAME,UNIT) \
      VALUES (31, 'Cholesterol', 'mg')");

conn.execute("INSERT INTO NUTRIENTS (ID,NAME,UNIT) \
      VALUES (32, 'Caffeine', 'mg')");

conn.commit()



print ("Operation completed successfully")
conn.close()
