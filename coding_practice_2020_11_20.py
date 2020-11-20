#question 1 

print("What is your favourite colour: ")
favourite_Colour = input ()
print (favourite_Colour, "?! No way, that's my favourite colour too! ")

#question 2
number_Cans_per_Pack = int(input("How many cans per package: "))
number_Pack = int(input("How many packages are there: "))

number_Cans = number_Cans_per_Pack * number_Pack

print(f'There are {number_Cans} in a pack. ')

print ("please enter the following in cm")
print("please enter the length of the length: ")
length = float (input())
print ("please enter the width: ")

#question 3
width = float (input())
print ("please enter the height: ")

height = float (input())
volume = length * width * height
print ("The total volume is", volume, "mL.")

#question 4

user_mutes = input ("do you mute the teacher when you join Google Meet")
if user_mutes == "no":
    print("Ok, good")
else:
    print("That's probably not a good idea")
