#  =========  The print() function =========
# You may want your program to display or output information to the user.
# The most common way to view program output is to use the print function.
# To use print, we enter the print command followed by one or more arguments.
#the following input comands will get the user's name and age and display them as a sentence in the end after all variables are stored.
name = input("Enter your name: ") #the variable 'name' will be stored as box string after the user inputs it.
age = input("Enter your age: ")   #the variable 'age' will be stored as a box string after the user inputs it.
print(name, age)                  # both strings will be displayed accordingly for the user to see utilizing the print function.
print("{} is {} years old!".format(name, age)) #the variables displayed accordingly as a sentence.
print ("Hello World!")