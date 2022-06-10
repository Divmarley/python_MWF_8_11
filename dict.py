from turtle import update


person = {
   "name" :"kofi",
   "age": 30, 
   "color":"black"
}

# del person
# to print the variable 
# print(person) 

# to check data type
# print(type(person))


# to check lenght of the variable 
# print(len(person))

# items in a dict are ordered


# accessing items in a Dictionary
# print(person["age"])
# print(person["name"])
# print(person["color"])


# Changeable
# Dictionaries are changeable,
#  meaning that we can change, add or remove items after the dictionary has been created.

# how to change an item in s dictionary

# person["color"] = "green"
# print(person) 

# how to change an item in s dictionary with a method

# update()
# person.update({"school":"opl"})
# person.update({"named":"kwame"})

# print(person)


# Adding Items into a Dictionary 
# person["add"] = "me"

# print(person)



# Removing Items into a Dictionary 

# pop()

# person.pop("name")
# person.pop("age")
# person.pop("color")

# print(person)

# del person["age"]
# del person["color"]
# del person["name"]


# person.popitem()
# person.popitem()
# person.popitem() 
#


# person.clear()
# print(person)



# update()
# clear()
# pop()
# popitem()


# Method	        Description
# clear()	        Removes all the elements from the dictionary
# copy()	        Returns a copy of the dictionary
# fromkeys()	    Returns a dictionary with the specified keys and value
# get()	            Returns the value of the specified key
# items()	        Returns a list containing a tuple for each key value pair
# keys()	        Returns a list containing the dictionary's keys
# pop()	        Removes the element with the specified key
# popitem()	    Removes the last inserted key-value pair
# setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	    Updates the dictionary with the specified key-value pairs
# values()	    Returns a list of all the values in the dictionary




kk =person.keys()
# print( kk)


kk =person.values()
print( kk)