'''Assignment: Compare Lists
Write a program that compares two lists and prints a message depending on if the inputs are identical or not.

Your program should be able to accept and compare two lists: list_one and list_two. If both lists are identical print "The lists are the same". If they are not identical print "The lists are not the same." Try the following test cases for lists one and two:

list_one = [1,2,5,6,2]
list_two = [1,2,5,6,2]
Copy
list_one = [1,2,5,6,5]
list_two = [1,2,5,6,5,3]
Copy
list_one = [1,2,5,6,5,16]
list_two = [1,2,5,6,5]
Copy
list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','cream']
'''

list_a = [1,2,5,6,2]
list_b = [1,2,5,6,2]
list_c = [23,34,2,145,77]
list_d = [23,34,2,145,77,23,987]
list_e = ['cats', 'cake', 'vacation', 'coding', 'ice cream']
list_f = ['cats', 'cake', 'vacation', 'coding', 'yoga']

if set(list_a) == set(list_b):
    print "The lists are the same"
else:
    print  "The lists are not the same."


if set(list_b) == set(list_c):
    print "The lists are the same"
else:
    print  "The lists are not the same."

if set(list_d) == set(list_f):
    print "The lists are the same."
else:
    print "the lists are not the same"
