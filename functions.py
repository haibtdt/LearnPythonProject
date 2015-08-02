__author__ = 'buihai'

initial_list = []
def f(a, L=[]):
    L.append(a)
    return L
initial_value = 7
def s(a, acc = initial_value):
    acc = acc + a
    return acc

def p(a, L=None):
    if L == None:
        L = []
    L.append(a)
    return L
def play (song, repeat=1):
  for play_count in range(repeat):
     print 'playing ', song, '...'

def cheeseshop(kind, *arguments, **keywords):
    print arguments
    print '-'*40
    print keywords

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper='Michael Palin',
           client="John Cleese",
           sketch="Cheese Shop Sketch")