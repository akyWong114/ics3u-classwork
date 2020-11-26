## String Questions! (#1-10)
#hello_name("")
name = input('Please enter your name: ')
print(f"Hello {name}!")

#make_abba
a = input('Please enter a word: ')
b = input('Please enter a second word: ')
print(a + b + b + a)

#make_tags
tag = input("Enter tag: ")
word = input("Enter word: ")
html = "<" + tag + ">" + word + "</" + tag + ">"
html = f"<{tag}>{word}</{tag}>"
html = "<{}>{}</{}>".format(tag, word, tag)
print(html)

#make_out_word (out, word)
word = input("Enter a word: ")
word_two = input("Enter a second word: ") 
print(word[:2] + word_two + word[2:])

#extra_end 
word = input("Enter a word: ")
print(word[-2:] * 3)

#first_two
word = input("Enter a word: ")
if len(word)<=2:
    print(word)    
else:
    print(word[:2])

#first_half
word = input("Enter something with even length: ")
first_half = word[:int(len(word)/2)]
print(first_half)

#without_end
word = input("Enter a word: ")
print(word[1:-1])

#combo_string
a = input("Enter something: ")
b = input("Enter another something: ")
if len(a) < len(b): 
    print(a + b + a)
else:
    print(b + a + b)

#non_start
a = input("Enter something: ")
b = input("Enter another something: ")
print(a[1:]+b[1:]) 

## Workbook Questions! (#34-40, 43, 45, 46
#Exercise 34 - Even or Odd? 
integer = int(input("Enter an integer: "))
if (integer % 2) == 0:
    print("{0} is an Even integer". format(integer))
else: 
    print("{0} is an Odd integer". format(integer))

#Exercise 35 - Dog Years
years = float(input("Enter dog's age in human years: "))
little_years = years * 10.5
big_years = ((years - 2) * 4) + 21
if years <= 2:
    print(f"The dog is {little_years} years old in dog years.")
else: 
    print(f"The dog is {big_years} years old in dog years.")

#Exercise 36 - Vowel or Consonant
letter = input("Input an alphabetical letter: ").lower()
print()
if letter in ('a' 'e' 'i' 'o' 'u'):
    print(f"{letter} is a vowel.")
elif letter == 'y':
    print(f"{letter} sometimes is a vowel and sometimes a consonant")
else:
    print(f"{letter} is not a vowel.")

#Exercise 37 - Name that Shape
n_sides = int(input("Enter the number of sides on the shape (must be 3-10): "))
if n_sides == 3:
    print("It's a triangle!")
elif n_sides == 4:
    print("It's a square!")
elif n_sides == 5:
    print("It's a pentagon!")
elif n_sides == 6:
    print("It's a hexagon!")
elif n_sides == 7:
    print("It's a septagon!")
elif n_sides == 8:
    print("It's an octagon!")
elif n_sides == 9:
    print("It's a nonagon!")
elif n_sides == 10:
    print("It's a decagon!")
    
#Exercise 38 - Month Name to Number of Days
month = input("Enter the name of a month: ").lower()
if month in ('january', 'march', 'may', 'july', 'august', 'october', 'december'):
    print(f"There are 31 days in {month}.")
elif month in ('april', 'june', 'september', 'november'):
    print(f"There are 30 days in {month}.")
elif month == 'february':
    print("There are 28 or 29 days in febuary.")
else:
    print("That is not a month.")

#Exercise 39 - Sound Levels
dB = float(input("Enter the decibel level: "))
if dB ==  130:
    print("Jackhammer")
elif dB == 106:
    print("Gas lawnmower")
elif dB == 70:
    print("Alarm clock")
elif dB == 40:
    print("Quiet room")
elif dB > 130:
    print("Louder than a jackhammer.")
elif dB < 40:
    print("Quieter than a quiet room.")
elif 106 < dB < 130:
    print("In between the noise level of a jackhammer and gas lawnmower.")
elif 70 < dB < 106:
    print("In between the noise level of a gas lawnmower and an alarm clock.")
elif 40 < dB < 70:
    print("In between the noise level of an alarm clock and a quiet room.")

#Exercise 40
print("Enter the lengths of the triangle sides: ")
x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))

if x == y and x == z:
    print("equilateral triangle")
elif x == y or y == z or z == x:
    print("isosceles triangle")
else:
    print("scalene triangle")  

# Exercise 41 - Note to Frequency
# I don't get what you are trying to do here. The question wants you to take the notes CDEFGAB from the user and display it's frequency for different octaves.
def get_frequency(note, A4 = 440):
# Avoid using captial letters when naming functions (You can search up the naming scheme online)
    notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
# I don't think the question cared about sharps
    octave = int(note[2]) if len(note) == 3   else int(note[1])
    key_number = notes.index(note[1]);

    if key_number < 3 :
        key_number = key_number + 12 + ((octave - 1) * 12) + 1
    else: 
        key_number = key_number + ((octave - 1) * 12) + 1
    return A4 * 2** ((key_number - 49) / 12)

#Exercise 43 - Faces on Money
banknote = int(input("Enter the denomination of the individual bank note amount: $"))
if banknote == 1:
    print("George Washington")
elif banknote == 2:
    print("Thomas Jefferson")
elif banknote == 5:
    print("Abraham Lincoln")
elif banknote == 10:
    print("Alexander Hamilton")
elif banknote == 20:
    print("Andrew Jackson")
elif banknote == 50:
    print("Ulysses S. Grant")
elif banknote == 100:
    print("Benjamin Franklin")
else:
    print("NO such note exists")

#Exercise 45: What Colour is that Square?
while True:
    oddset = ['a', 'c', 'e', 'g']
    evenset = ['b', 'd', 'f', 'h']
    odd_numbers = [1, 3, 5, 7]
    even_numbers = [2, 4, 6, 8]
    letter = input("Enter the letter:")
    while True:

# try and except is specifically for debugging. You can replace this with a if statement. 
    if letter.lower() in oddset and number in odd_numbers:
        print("It's a black square!")
    elif letter.lower() in evenset and number in odd_numbers:
        print("It's a white square!")
    elif letter.lower() in evenset and number in even_numbers:
        print("It's a black square!")
    elif letter.lower() in oddset and number in even_numbers:
        print("It's a white sqaure!")
    else:
        print("You must enter a letter.")
# while True:
#     oddset = ['a', 'c', 'e', 'g']
#     evenset = ['b', 'd', 'f', 'h']
#     odd_numbers = [1, 3, 5, 7]
#     even_numbers = [2, 4, 6, 8]
#     letter = input("Enter the letter:")
#     number = int(input("Enter the number: "))
    
#     if letter.lower() in oddset and number in odd_numbers:
#         print("It's a black square!")
#     elif letter.lower() in evenset and number in odd_numbers:
#         print("It's a white square!")
#     elif letter.lower() in evenset and number in even_numbers:
#         print("It's a black square!")
#     elif letter.lower() in oddset and number in even_numbers:
#         print("It's a white sqaure!")
#     else:
#         print("You must enter a letter.")

#Exercise 46 - Season from Month and Day
month = input("Please enter the month: ").lower()
day = int(input("Enter a day: "))

if month in ('january', 'febuary', 'march'):
    season = 'winter'
elif month in ('april', 'may', 'june'):
    season = 'spring'
elif month in ('july', 'august', 'september'):
    season = 'summer'
else: 
    season = 'autumn'
# Leave a space for formatting (or it will look like a single if statement)
if month == 'march' and day > 19:
    season == 'spring'
elif month == 'june' and day > 20:
    season = 'summer'
elif month == 'september' and day > 21:
    season = 'autumn'
elif month == 'december' and day > 20:
    season = 'winter'

# You don't need to have parenthesis for if statemnets (redundent)
print(f"The season is {season}.")
