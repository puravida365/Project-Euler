#!/usr/bin/python

''' 
Problem 1 - Multiples of 3 and 5
Project Eurler .net
Josué Mora
'''

def getMultiples(l):
    for n in range(1,1000):
        if (n%3 == 0) or (n%5 == 0):
            l.append(n)

def addMultiples(l):
    total = sum(l)
    print (total)

def main():

    l =[]
    getMultiples(l)
    addMultiples(l)
    

if __name__ == "__main__":
    main()

'''
$python 1.py
233168

https://projecteuler.net/thread=1;page=9#last
Other users solutions:

With Python:
sum([x for x in range(1000) if x%3==0 or x%5==0])

With Javascript:
let range = x => x? [...range(x-1), x-1] : [];  // range(x) returns an array of nums from 0 to x-1
let solution = range(1000)                      // numbers from 0 to 999
    .filter(x => !(x%3 && x%5))                 // keep only multiples of 3 or 5
    .reduce((c, n) => c + n);                   // sum it up

'''

