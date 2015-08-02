__author__ = 'buihai'

# the index and corresponding value can be retrieved at the same time using enumerate() function
for i, v in enumerate(['tic', 'tac', 'toe']):
    print i, v


# looping over 2 or more sequences at a time
questions = ['name', 'quest', 'favorite color']
answers = ['hai', 'the holy grail', 'blue']

for q, a in zip(questions, answers):
    print 'what is your {0}? It is {1}.'.format(q, a)

# looping in reverse
for q, a in reversed(zip(questions, answers)):
    print 'what is your {0}? It is {1}.'.format(q, a)

# looping in sorted order
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print f


# looping through dictionaries
knights = {'gallahad':'the pure', 'robin':'the brave'}
for k, v in knights.iteritems():
    print k, v

# make a copy when modifying the sequence itself
words = ['cat', 'window', 'defenestrate']
for w in words[:]:
    if len(w) > 6:
        words.insert(0, w)
print words
