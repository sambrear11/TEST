''' Ask user for their name 
    Store this input as user_name
    Make the first letter of their name capitalized if they did not do so
    ask their age, street name, and house number
    store this information as user_age, user_street_name and user_house_number respectively
    print out their information in a string sentence'''



user_name = input("What is your name: ")
user_name_name = user_name.capitalize()
user_age  = input("What is your age: ")
user_street_name = input("what is your Street name: ")
user_house_number = input("What is your House number: ")

print(f"This is {new_name}. They are {user_age} years old and live at\
 house number {user_house_number} on {user_street_name}.")
