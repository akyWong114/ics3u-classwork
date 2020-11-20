print ("What is your favourite colour: ")
favouriteColour = input ()
print ( favouriteColour, "!? No way, that's my favourite colour too! ")

numberCansperPack = int(input("How many cans per package: "))
numberPack = int(input("How many packages are there: "))

numberCans = numberCansperPack * numberPack

print(f'There are {numberCans} in a pack. ')

print ("please enter the following in Litres")
print("please enter the length of the length: ")
length = float (input())
print ("please enter the width: ")
width = float (input())
print ("please enter the height: ")
height = float (input())
volume = length * width * height
print ("The total volume is", volume, "litres")
