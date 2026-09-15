# The first two parts of this worksheet are just to make sure that you're 
# comfortable working with lists and dictionaries -- try not to overthink 
# it all too much!

# 1
fruits = ["pear", "mango", "passionfruit"]
print(fruits)

# 2
# Make sure that you remember that lists are zero-indexed: that is: they start
# at zero.  This is true of many (but sadly not all) languages.
print(fruits[1]) # This is the *second* item, "mango"

# 3 
fruits.append("lime")
print(fruits)
# You cannot just print(fruits.append("lime")), here, though it is tempting.
# Append is a "mutator": that is: it changes (or mutates) fruits, but does not 
# return anything itself.

# 4
fruits[0] = "apple"
print(fruits)

# 5
if "apple" in fruits:
    print("Huzzah, an apple")
else:
    print("No apples: you will be accosted by doctors")

# 6
# This gives us a little more control over the printing process.  
for fruit in fruits:
    print(fruit)

# 7
# It's early days: it's good to practice using "accumulators"
# This is just a variable that can "accumulate" some process you run in a loop.
# In this case it starts at zero and we're going to increment it once per loop
# It's a good way of counting things.
length = 0

for fruit in fruits:
    length += 1

print(length)

# I also suggested using a function, to practice functions
# It's nice when functions do not have 'side-effects' like printing.
# For any given input (argument), it has a predictable output (return)
def list_length(a_list):
    length = 0
    for item in a_list:
        length += 1
    return length

fruit_length = list_length(fruits)
print(fruit_length)

# 8
# This one is like the counter, in that you need an out-of-scope variable 
# to keep track of the longest fruit.
longest_fruit = ""

for fruit in fruits:
    if len(fruit) > len(longest_fruit):
        longest_fruit = fruit

print(longest_fruit)
# This one might be a bit weird to reason about -- either try stepping through
# this code in your mind, fruit by fruit; or, for interactivity, practice using
# breakpoint() before the loop, 's'tepping down into the loop to investigate
# the values of fruit & longest_fruit

# 9
# Again, you're going to have to make a second list here as a kind of accumulator
# there's no escaping it - you must have two lists at the end:
fruit_lengths = []
for fruit in fruits:
    fruit_lengths.append(len(fruit))

print(fruits)
print(fruit_lengths)

# =============================================================================

# 10
grades = {
    "genis": 99,
    "lloyd": 43,
    "colette": 65
}

print(grades)

# 11
print(grades["colette"])

# 12
grades["presea"] = 87

# 13
grades["lloyd"] = 50
print(grades)

# 14
# Actually, you can also just do `if "alice" in grades`, since Python will assume
# that you mean the keys (kind of).
if "alice" in grades.keys():
    print("Hello Alice!")
else:
    print("She doesn't go here")

# 15
for student in grades.keys():
    print(student)

# 16
for score in grades.values():
    print(score)

# 17
for student, score in grades.items():
    print(f"{student} got a score of {score}.")

# 18 
# Here we go, it's another accumulator
total_score = 0
for score in grades.values():
    total_score += score

# len(a_dictionary) feels weird, but it's counting the number of keys!
average = total_score / len(grades)
print(f"The average score is {average}")

# Overcomplicated diversion:
# There's probably a cool way of calculating a rolling average, like this,
# but I wasn't really expecting you to work out a rolling average.
count = 0
rolling_average = 0

for score in grades.values():
    working_amount = (rolling_average * count) + score
    count += 1
    rolling_average = working_amount / count

print(f"The final from the rolling average is {rolling_average}")

# 19
for student, score in grades.items():
    if score > 80:
        print(f"{student} scored {score}, which is over 80")

# 20
# I'm going to decide parameters, first of all.
# I think that "THat" and "that" should be counted as the same word
# But "that!" and "that" can be separate.

word_counts = {}
user_input = input("Enter a string, and I'll count the words! ")
word_list = user_input.lower().split() # Notice the lower!
# I could have done 160 & 161 on one line but it's a little easier to read this way.

for word in word_list:
    word_counts[word] = word_counts.get(word, 0) + 1

print(word_counts)


