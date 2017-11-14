print "Hello World"
x = "Hello World"
print (x)
'''print (y)'''
#Note that the comma is outside the closing quotation mark of the string. Print inserts a space between elements separated by a comma.
name = "Zen"
print "My name is", name
#The second is by concatenating the contents into a new string, with the help of +.
name = "Zen"
print "My name is " + name
#Lastly, you can use curly brackets - {} - and the string .format() method to inject variables into your string - this is known as string interpolation.
first_name = "Zen"
last_name = "Coder"
print "My name is {} {}".format(first_name, last_name)

hw = "hello %s" % 'world'
print hw
# the output would be:
# hello world

x = "Hello World"
print x.upper()
#<list>.append(<new_element>)
#Appends a new item onto the end of the given list. You can pass any data type into this function.
x = [1,2,3,4,5]
x.append(99)
print x


x = [99,4,2,5,-3];
print x[:]
#the output would be [99,4,2,5,-3]
print x[1:]
#the output would be [4,2,5,-3];
print x[:4]
#the output would be [99,4,2,5]
print x[2:4]
#the output would be [2,5];

#len(sequence): Returns the number of items in a sequence.
my_list = [1, 'Zen', 'hi']
print len(my_list)
# output
3
#Conditinal Expressions
age = 15
if age >= 18:
  print 'Legal age'
else:
  print 'You are so young!'
#The if and if-else statements in Python are straightforward and are very much like the if statements in other languages. The only difference with Python's if statement is, when you have another condition, you write it using elif.
#elif is just like else if or elsif from other languages.
if age >= 18:
  print 'Legal age'
elif age == 17:
  print 'You are seventeen.'
else:
  print 'You are so young!'


for count in range(0, 5):
    print "looping -", count

my_list = [4,'dog', 99, ['list', 'inside', 'another'], 'hello', 'world']
for element in my_list:
        print element
