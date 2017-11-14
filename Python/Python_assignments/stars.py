'''
Assignment: Stars
Write the following functions.

Part I
Create a function called draw_stars() that takes a list of numbers and prints out *.

For example:

x = [4, 6, 1, 3, 5, 7, 25]
Copy
draw_stars(x) should print the following when invoked:

****
******
*
***
*****
*******
*************************
Copy
Part II
Modify the function above. Allow a list containing integers and strings to be passed to the draw_stars() function. When a string is passed, instead of displaying *, display the first letter of the string according to the example below. You may use the .lower() string method for this part.

For example:


draw_stars(x) should print the following in the terminal:

****
ttt
*
mmmmmmm
*****
*******
jjjjjjjjjjj
'''

x = [4, 6, 1, 3, 5, 7, 25]
stars = []
def draw_stars(cat):
    for i in cat: #range(len(x)):
        stars.append("*"* i)

draw_stars(x)
print stars

x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
container = []
def letter(name):
    for i in name:
        if type(i)  == type(1):
            container.append("*" * i)
        else:
            container.append(i[0]*len(i))
letter(x)
print container
