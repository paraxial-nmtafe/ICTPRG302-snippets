# I went over answers to questions 1-5 in the lecture
# So I will save adding answers here for when I have more time to spare
# Short common errors:
# 1. IDLE users: Your file-to-open is not located side-by-side with your Python file
# 2. Your file-to-open is called something different because you were fooled by a file extension
#       tip: On windows you can turn on file extensions to see
#       You can also navigate to the folder in your shell and `ls` to check that the
#       file is called what you think it is
# 3. You have (evil) spaces in your filename that do not match what you told Python
# 4. You are not using IDLE (even though at this stage you should still be using it)
#       (But I will throw you a bone: the file's relative location is relative to
#        Python's runtime location.  Check what `pwd` is in your shell.)

# Let's skip straight to the big activities:

# Word Counter
# The guidance in the worksheet assumes that you are going line by line as you are 
# parsing the file, just in case the file you open is terrabytes in size or something
# That said: the novel text provided will easily fit fully in memory, if you want
# to simplify somewhat.

# We're assuming that you have a word counter function from a few weeks back:
def word_count(string):
    word_counts = {}
    word_list = string.strip().lower().split()
    for word in word_list:
        word_counts[word] = word_counts.get(word, 0) + 1

    return word_counts

# My solution will include my slightly overcomplicated dictionary merge option:
def merge_dictionaries(original, new):
    for key, value in new.items():
        original[key] = original.get(key, 0) + value

    # This method mutates 'original', so I don't need to return it
    # But it's not my personal style, so I'm returning it anyway
    return original

final_counts = {}
with open("carmilla_le_fanu.txt", "r", encoding="utf-8") as file:
    for line in file:
        final_counts = merge_dictionaries(final_counts, word_count(line))

# This next step could have been a list-of-lists,
# but a list of tuples is probably better! We never need to change them.
# Note carefully the reversal of the tuple
# Since sort order is determined by the first element in the collection
# ie: (0, 1) comes before (1, 0)

list_of_counts = []
for word, word_count in final_counts.items():
    list_of_counts.append((word_count, word))

print(sorted(list_of_counts, reverse=True))

#  Hm, I never showed you that `sorted` can take a 
# "reverse" parameter
# You could also have sorted it but then printed it
# backwards by slicing

# Here's an option that you could have taken:
list_of_counts.sort()
print(list_of_counts[::-1])


# Budget Tracker answer later, I am going to bed
