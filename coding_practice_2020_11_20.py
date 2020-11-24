favourite_Colour = input("What is your favourite colour: ")
print (f"{favourite_Colour}?! No way, that's my favourite colour too!")
# don't put have spaces between functions: unless it's * = , or 
# use _ like "number_Pack" to divide them

# Think of it this way. input(), print(), int() are all built-in functions in python.
# Like the functions you see in math (But don't use that analogy to compare). 
# In f(x) = x + 2, you insert a value for x to find the answer.
# The above functions is SIMILAR (Not same)because you are entering a certain (value type)value into the parenthesis.

number_Cans_per_Pack = int(input("How many cans per package: "))
number_Pack = int(input("How many packages are there: "))
number_Cans = number_Cans_per_Pack * number_Pack

print(f'There are {number_Cans} in total. ')
# You set number_Cans to be the total # of cans above. So number_Cans = total cans
print("please enter the following in cm")
length = float(input("please enter the length: "))
width = float(input("please enter the width: "))
height = float(input("please enter the height: "))
volume = length * width * height
print(f"The total volume is {volume}mL.")

#question 4

user_mutes = input("do you mute the teacher when you join Google Meet? [Y/N]: ")
# You want to create a Y/N or 1/2 so the code doesn't fail because of poor spelling.
# So if Jimmy ran your code and typed No with a capital N. You code will fail. putting Y/N reduces his options
if user_mutes == "no":
    print("Ok, good")
else:
    print("That's probably not a good idea")
