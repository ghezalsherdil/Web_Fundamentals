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
