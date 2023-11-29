#prompt user to input the following details independantly: name, age, House number and street name.
#print a created string saying;" This is(name entered).He is (age enetered0 years old and lives at house(House number entered) on (street name enetered)"), usinf an f string type function

name=input("Enter name: ")
age=input("Enter age:")
house_number=input("Enter house number: ")
street_name=input("Enter street name: ")
print(f"This is {name}. He/she is {age} years old and lives at house number {house_number} on {street_name}.")