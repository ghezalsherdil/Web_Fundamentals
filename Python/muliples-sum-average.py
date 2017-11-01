
#prints all the odd numbers from 1 to 1000.
for x in range(1, 1000):
    if (x % 2 == 1):
        print x

#prints all the multiples of 5 from 5 to 1,000,000.
for g in range(5, 1000000, 5):
    print g

#prints the sum of all the values in the list.
a = [1, 2, 5, 10, 255, 3]
b = sum(a)
print b
# prints the average of the values in the list
print float(sum(a)) / len(a)
