# --------------
# Code starts here

# Create the lists 
class_1=['Geoffrey Hinton','Andrew Ng','Sebastian Raschka','Yoshua Bengio']
class_2=['Hilary Mason','Carla Gentry','Corinna Cortes']
# Concatenate both the strings
new_class=class_1+class_2

# Append the list
new_class.append('Peter Warden')
# Print updated list

print(new_class)
# Remove the element from the list
new_class.remove("Carla Gentry")
# Print the list
print(new_class)


# Create the Dictionary
courses={'Math':65,'English':70,'History':80,'French':70,'Science':60}
total=sum(list(courses.values()))
percentage=((total)*100)/500


# Print the percentage

print(percentage)


# Create the Dictionary
mathematics={'Geoffrey Hinton':78, 'Andrew Ng':95, 'Sebastian Raschka':65, 'Yoshua Bengio':50, 
'Hilary Mason':70, 'Corinna Cortes':66, 'Peter Warden':75}

topper=max(mathematics,key=mathematics.get)
# Slice the dict and stores  the all subjects marks in variable
first_name,last_name=topper.split()

# Store the all the subject in one variable `Total`
full_name=last_name+' '+first_name
# Print the total
certificate_name=full_name.upper()
# Insert percentage formula
print(certificate_name)

# Given string


# Create variable first_name 

# Create variable Last_name and store last two element in the list

# Concatenate the string

# print the full_name

# print the name in upper case

# Code ends here


