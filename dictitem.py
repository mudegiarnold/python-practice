thisdict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
        }
x = thisdict["model"]
print(x)

x = thisdict.get("model")
print(x)

x = thisdict.keys()
print(x)


car = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
        }
x = car.keys()
print(x) #before the change
car["color"] = "white"
print(x) #after the change


x = thisdict.values()
print(x)


car = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
        }

x = car.values()
print(x) #before the change
car["year"] = 2020
print(x) #after the change
