import database
import requests
import json
from decimal import *

class Report:
    def __init__(self):
        self.db = database.Database()

        # Will be user ID
        meals = self.db.conn.execute("SELECT * FROM EATING WHERE USER = (?)", (1,))
        nutrients = self.db.conn.execute("SELECT * FROM NUTRIENTS")

        runningTotal = [Decimal(0.0)] * 33
        for food in meals:
            # Create API request using that number
            link = "https://api.nal.usda.gov/ndb/V2/reports?ndbno=" + str(food[2]) + "&type=b&format=json&api_key=vR7HEUo0B9sbz8kh40G3xJ5Ch4Ft9Xx7JQ4CCfSU"
            # Gets JSON from URL
            r = requests.get(url=link)
            # convert to string
            h = json.dumps(r.json())
            # load to dictionary
            my_dict = json.loads(h)
            for i in range(0, 32):
                # Add servings times meaure nutrients
                runningTotal[i] = runningTotal[i] + Decimal(my_dict["foods"][0]["food"]["nutrients"][i]["measures"][food[3]]["value"]) * Decimal(food[4])

            c = 0
            for j in nutrients:
                # Print nutrient name
                print(j[1])
                # Print nutrient value
                print(runningTotal[c])
                # Increase counter
                c = c + 1








if __name__ == "__main__":
    r = Report()
