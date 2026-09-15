# 1 Greet the user
name = input("Hi, what's your name? ")
print(f"Hi {name}, nice to meet you.")

# 2 Ask the user for two numbers and print their sum
number_one = input("Please enter a number: ")
number_two = input("Please enter another number: ")

# Here, I do the conversion from string to float, and 
# reassign back to the variables.
number_one = float(number_one)
number_two = float(number_two)

print(f"The sum of the two numbers is {number_one + number_two}")

# 3 Ask the user for two numbers and subtract them
# This time I convert "inline"
# You will learn over time what is 'readable' and what is 'unreadable'.
number_one = float(input("Please enter a number: "))
number_two = float(input("Please enter another number: "))

print(f"The difference of the two numbers is {number_one - number_two}")

# 4 Ask the user for two numbers and multiply them
number_one = float(input("Please enter a number: "))
number_two = float(input("Please enter another number: "))

print(f"The multiplication of the two numbers is {number_one * number_two}")

# 5 Ask the user for two numbers and divide them
number_one = float(input("Please enter a number: "))
number_two = float(input("Please enter another number: "))

# Here I use `/`, since I want real division.
# Try entering '0' as your second number to crash your program for fun.
print(f"The division of the two numbers is {number_one / number_two}")

# 6 Calculate area of a rectangle
# This one is, of course, identical to the multiplication question.
# The key here is to think about variable naming.
height = float(input("Please enter the height: "))
width = float(input("Please enter the width: "))
area = height * width

print(f"The area of the rectangle is {area}")

# 7 Convert Celsius to Fahrenheit
# This variable name is a little wordy.  
# I'd also accept "temperature_c" or "celsius"
temperature_in_celsius = float(input("What is the temperature in degrees celsius? "))
temperature_in_fahrenheit = (temperature_in_celsius * 9 / 5) + 32
# String interpolation is nicer, but let's see some concatenation again.
# Note that I have to convert a number to string if I want to concatenate.
print("That is " + str(temperature_in_fahrenheit) + " degrees Fahrenheit.")

# 8 Simple interest calculator
# (Yes, this is just multiplication.  Later, when we cover loops, you might try
# calculating complex interest :) )
# (The assumption is that rate is a positive number between 0 and 100)
principal = float(input("What is the amount borrowed? "))
rate = float(input("What is the percentage interest rate? "))
time = float(input("How long is the loan, in years? "))
print(f"The interest on this loan is {(principal * rate * time)/100}")

# 9 Calculate the square of a number
number = float(input("What is the number to square? "))
squared = number ** 2
print(str(number) + " squared is " + str(squared))

# 10 Swap two variables.
# I like to imagine swapping two things between my left and right hands, 
# but I have a basket to put things and each hand can only hold one thing.
left_hand = "left"
right_hand = "right"
print("left_hand:", left_hand, ", right_hand:", right_hand)
basket = left_hand
left_hand = right_hand
right_hand = basket
print("After swap:")
print("left_hand:", left_hand, ", right_hand:", right_hand)

# 11 Calculate the cube of a number
number = float(input("What is the number to cube? "))
cubed = number ** 3
print(str(number) + " cubed is " + str(cubed))

# 12 Calculate the cube of a number
number_one = float(input("Please enter a number: "))
number_two = float(input("Please enter another number: "))
number_three = float(input("Please enter yet another number: "))
average = (number_one + number_two + number_three) / 3 # Note well: brackets

print(f"The average is {average}")
