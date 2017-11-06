'''Assignment: Type List
Write a program that takes a list and prints a message for each element in the list, based on that element's data type.

Your program input will always be a list. For each item in the list, test its data type. If the item is a string, concatenate it onto a new string. If it is a number, add it to a running sum. At the end of your program print the string, the number and an analysis of what the list contains. If it contains only one type, print that type, otherwise, print 'mixed'.

Here are a couple of test cases. Think of some of your own, too. What kind of unexpected input could you get?

#input
l = ['magical unicorns',19,'hello',98.98,'world']
#output
"The list you entered is of mixed type"
"String: magical unicorns hello world"
"Sum: 117.98"
Copy
# input
l = [2,3,1,7,4,12]
#output
"The list you entered is of integer type"
"Sum: 29"
Copy
# input
l = ['magical','unicorns']
#output
"The list you entered is of string type"
"String: magical unicorns"
'''

mixed = ['cats', 10, 'dogs', 'python', 3748,'like']
integer = [5,13,9,888,148]
string = ['I','like','cats','not','dogs']
mixedin = []
name = []

for element in mixed:
    if type(element) == int:
        mixedin.append(element)

insum = sum(integer)

for ing in string:
    if type(ing) == str:
        name.append(ing)

print "The list you entered of of mixed type"
print "String:",mixed[0],mixed[2],mixed[3],mixed[5]
print "Sum",sum(mixedin)


print "The list you entered is of integer type"
print "Sum:",insum

print "The list you entered is of string type"
print "String:",string[0],string[1],string[2],string[3],string[4]
