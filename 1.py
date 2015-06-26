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
'''