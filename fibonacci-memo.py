''' Fibonacci recursive sequence code from
http://openbookproject.net/thinkcs/python/english3e/dictionaries.html '''

import time

countcalls = 0 # global variable for expedience
alreadyknown = {0: 0, 1: 1} # keeps track of the computations which haver already been completed

def fibmemo(n):
    ''' pre: n is a small positive integoer
    Post: This function uses the following dedinition
    fib(0) = 0
    fib(1) = 1
    fib(n) = fib(n-1) + fib(n-2)  for n >= 2
    '''

    global countcalls
    global alreadyknown
    countcalls = countcalls + 1

    if n not in alreadyknown:
        new_value = fibmemo(n - 1) + fibmemo(n - 2)
        alreadyknown[n] = new_value
    return alreadyknown[n]

def main():
    '''  The program runs the recursive
    Fibonacci sequence 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 134, ...
    which was devised by Fibonacci (1170-1250), who used this to model
    the breeding of (pairs) of rabbits. '''

    n = int(input("\nEnter a small integer for Fibonacci: "))
    t0 = time.clock()
    result = fibmemo(n)
    t1 = time.clock()

    print("fibmemo({0}) = {1} ran in {2:.2f} seconds".format(n, result, t1-t0))
    print("A total of " + str(countcalls) + " function calls were made.")

main()
