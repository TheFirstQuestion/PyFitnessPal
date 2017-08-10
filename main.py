import json
import requests

# Gets JSON from URL
r = requests.get(url='https://api.nal.usda.gov/ndb/V2/reports?ndbno=01009&type=b&format=json&api_key=vR7HEUo0B9sbz8kh40G3xJ5Ch4Ft9Xx7JQ4CCfSU')
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

# Print nutrient name and amount
for i in range(0, 32):
    print()
    print(my_dict["foods"][0]["food"]["nutrients"][i]["name"])
    value = my_dict["foods"][0]["food"]["nutrients"][i]["measures"][choice]["value"]
    total = float(value) * float(amount)
    print(total)
