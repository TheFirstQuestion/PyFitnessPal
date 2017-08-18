import json
import requests
import database

def search():
    # Get food name from user
    query = input("What are you searching for?  ")
    link = "https://api.nal.usda.gov/ndb/search/?format=json&q=" + query + "&sort=r&max=10&offset=0&group=s&api_key=vR7HEUo0B9sbz8kh40G3xJ5Ch4Ft9Xx7JQ4CCfSU&ds=Standard%20Reference"
    # Gets JSON from URL
    r = requests.get(url = link)
    # convert to string
    h = json.dumps(r.json())
    # load to dictionary
    my_dict = json.loads(h)
    # List names
    for i in range(0, 10):
        print( str(i + 1) + " " + " " + my_dict["list"]["item"][i]["name"])
    # Get ndb number of the food they pick
    choice = input("Which type did you eat?  ")
    foodNo = my_dict["list"]["item"][int(choice) - 1]["ndbno"]
    return foodNo


def record(foodNo):
    # Create API request using that number
    link = "https://api.nal.usda.gov/ndb/V2/reports?ndbno=" + foodNo + "&type=b&format=json&api_key=vR7HEUo0B9sbz8kh40G3xJ5Ch4Ft9Xx7JQ4CCfSU"
    # Gets JSON from URL
    r = requests.get(url=link)
    # convert to string
    h = json.dumps(r.json())
    # load to dictionary
    my_dict = json.loads(h)
    # Print name of food
    desc = my_dict["foods"][0]["food"]["desc"]["name"]
    print(desc)
    # Get length of various things
    nutrients = len(my_dict["foods"][0]["food"]["nutrients"])
    measures = len(my_dict["foods"][0]["food"]["nutrients"][0]["measures"])
    # Print measure options
    for i in range(0, measures):
        print(str(i + 1) + " " + " " + str(my_dict["foods"][0]["food"]["nutrients"][0]["measures"][i]["qty"]) + " " +  my_dict["foods"][0]["food"]["nutrients"][0]["measures"][i]["label"])
    # Get choice of meaure
    choice = int(input("What type of " + desc + " did you eat?  "))
    # Get amount eaten, to be used to multiply nutrients
    amount = float(input("How many " + my_dict["foods"][0]["food"]["nutrients"][0]["measures"][choice]["label"] + " did you eat?  "))
    # Get date of eating
    day = input("What day did you eat it? (YYYY-MM-DD): ")
    #### Should verify date
    db = database.Database()
    db.conn.execute("INSERT INTO EATING (USER, FOOD, MEASURE, SERVINGS, DAY) \
      VALUES (1, ?, ?, ?, ?)", (foodNo, choice, amount, day))
    db.close()

    print("record entered")




if __name__ == "__main__":
    record(search())
