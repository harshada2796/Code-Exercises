"""
Queens have always hated each other. Traditionally when queens were placed on a chessboard a queen gets jealous of another if:

They are both in the same row.
They are both in the same column.
They can see each other diagonally i.e lie in a line inclined 45 degrees or 135 degrees to the base of board.
But now the hatred has increased and the new condition is that no three of them should lie in any straight line (this line need not be aligned 45 degrees or 135 degrees to the base of chess board).
"""
result = [] # this serves mainly as an index to avoid iteration
#space = None
cache = dict()
def cross_lines(r,N,drop):
    for y, x in enumerate(result):
        for z, x2 in enumerate(result[(y+1):]):
            y2 = z + y + 1
            dx = x2 - x
            dy = y2 - y
            n = (r - y) * dx / float(dy)
            if n - int(n) == 0 and x + n >= 0 and x + n < N:
                drop.add(x + int(n))

def insert(r,N):
    """ insert a queen into row r of board b """ 
    drop = set(result)
    #cross out diagonals intersection
    for y, x in enumerate(result):
        c = x + (y -r)
        if c < N and c >=0:
            drop.add(c)
        c = x - (y -r)
        if c >= 0 and c < N: 
            drop.add(c)

    #cross out lines intersections
    cross_lines(r,N,drop)
    #get possible columns
    for c in (x for x in space if x not in drop):
        result.append(c)
        if r < (N-1):
            if(insert(r + 1, N)):
                return True
            else:
                result.pop()
        else:
            return True
    return False

        
def print_result():
    """ print result """ 
    print ' '.join(str(n + 1) for n in result)

import sys
from prime_sieve import get_primes
if __name__ == "__main__":
    N = int(sys.argv[1])#int(raw_input(''))
    global space
    space = range (N)
    global primes
    primes = get_primes(N)
   
    if(insert(0,N)):
        print_result()
        #print_verbose(b)
