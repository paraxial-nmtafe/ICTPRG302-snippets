# 1: Odd or even
# Floats? Try evaluating this in the console: (12.0 % 2) == True
number = float(input("Enter a number: "))
is_even = (number % 2) == 0

if is_even:
    print("It's even")
else:
    print("It's odd")

# 2: Largest of three numbers
number_one = float(input("Enter a number: "))
number_two = float(input("Enter another number: "))
number_three = float(input("Enter yet another a number: "))

# Is this the best way to solve this? 
# Absolutely not: it is a way to practice thinking about if-statements
if number_one > number_two:
    if number_one > number_three:
        print(number_one)
    else:
        print(number_three)
else: 
    if number_two > number_three:
        print(number_two)
    else:
        print(number_three) 

# 3: Grade Calculator
raw_score = float(input("What was your score? (0-100) "))

if raw_score >= 90 and raw_score <= 100:
    print("A")
elif raw_score >= 80 and raw_score < 90:
    print("B")
elif raw_score >= 70 and raw_score < 80:
    print("C")
elif raw_score >= 60 and raw_score < 70:
    print("D")
else:
    # You could also have put another elif for >= 0, < 60,
    # and treat the "default case" as an error
    print("F")


# 4: Password checker
your_secret_password = "hunter2"
raw_input = input("What's the password? ")

if raw_input == your_secret_password:
     print("Access granted")
else:
     print("Access denied")

# FOR LOOP SOLUTIONS ================================
# In week 3, we'll cover while loops, and you can rewrite
# these using whiles.

# 5: Count from 1 to 10
# Look at how I'm handling this off-by-one:
print("One to ten")
for counter in range(1, 11):
    print(counter)

# 6: Count from 10 to 1
print("Ten to one")
for counter in range(10, 0, -1):
    print(counter)

# 7: Print even numbers from 1 to 20:
# You could use an if-statement, but that can come later
# Let's control a range:
print("Evens from 1 to 20")
for counter in range(2, 21, 2):
    print(counter)

# 8: Sum of first 10 numbers
# This one takes an accumulator:
accumulator = 0
for number in range(1,11):
    # remember that this is the short way to write accumulator = accumulator + number
    accumulator += number

# 9 Multiplication table
# The way to solve this is to first think about how you would solve it ONCE
# Write the print statement you need for "2 x 1 = 1"
# Then decide where you need to include the variable for your table.
# And then decide "which part needs to change each loop" -- that will be your loop counter (number, in this case)
# Finally put it inside a for-loop, and trust Python to do the rest.

times_table = int(input("Which times-table would you like to display? "))
print(f"The {times_table} times-table")
for number in range(1, 13):
    print(f"{times_table} x {number} = {times_table * number}")

# 10 Factorial Calculator
# First you should know what a factorial is.  
# 4 factorial is 4*3*2*1.  6 factorial is 6*5*4*3*2*1.
# (Aside: there will be an interesting way of rewriting this next week.)
base = int(input("What base number should we use? "))
result = 1 # Recall that 1 * anything is itself, so it's a safe starting number.
for number in range(base, 0, -1):
    result = result * number

print(f"{base} factorial is {result}")

# 11: Print all characters in a string line by line:
# This one is straight out of the lecture slides, but it's nice to make a variable-length program with some user input.
answer = input("What word or sentence do you want made vertical? ")
for each_letter in answer:
    print(each_letter)

# 12: Draw a triangle
# This can be done a few ways, but it's easier if you remember that Python can make repeating strings by multiplying them.
height = int(input("What height should your triangle be? "))

for row in range(0, height):
    print("*" * (row + 1))


