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
