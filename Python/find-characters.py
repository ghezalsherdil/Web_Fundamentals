colors = ['red', 'green', 'pink', 'black', 'brown', 'orange', 'yellow']
letter = set('e')

for word in colors:
    if letter & set(word):
        print word
