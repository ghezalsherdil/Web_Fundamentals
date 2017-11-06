'''Assignment: Find Characters
Write a program that takes a list of strings and a string containing a single character, and prints a new list of all the strings containing that character.

Here's an example:

# input
word_list = ['hello','world','my','name','is','Anna']
char = 'o'
# output
new_list = ['hello','world']
Copy
Hint: how many loops will you need to complete this task?
'''

colors = ['red', 'green', 'pink', 'black', 'brown', 'orange', 'yellow']
letter = set('e')

for word in colors:
    if letter & set(word):
        print word
