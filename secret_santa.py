import random
import sys

def shuffle_rtn(*items):
    a = [x for x in items]
    random.shuffle(a)
    return a

def circle(*items):
    return [(items[i], items[i+1]) for i in range(len(items)-1)] + [(items[-1], items[0])]

if __name__ == "__main__":
    for x in circle(*shuffle_rtn(*sys.argv[1:])): print(x)
