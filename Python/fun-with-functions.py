def odd_even():
    for i in range(1,2001):
        if i % 2 == 0:
            print "Number is", i , "This is an even number"
        else:
            print "Number is", i , "This is an odd number"

print odd_even()


def multiply(arr,num):
    for x in range(len(arr)):
        arr[x] *= num
    return arr
a = [2,30,5,45,155]
b = multiply(a,5)
print b
