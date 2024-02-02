import sys
#Should look more into unit testing in python.
#Should have error handling
#Look at what happens if no arguments are passed. Should give feedback? 



def jfi(throughputlist):
    if len(throughputlist)<2:
        raise Exception("You need to add arguments after calling the jains.py")
    """
    >>> jfi(['bla',10,10,10])
    1.0
    >>> jfi([0,10,10,10])
    1.0
    """
    numerator = 0
    denominator = 0
    for i in range(1,len(throughputlist)):
        number = int(throughputlist[i])
        numerator += number
        denominator += number*number
    return (numerator**2)/((len(throughputlist)-1)*denominator)

listinput = sys.argv
result = jfi(listinput)
print(f'Jains Fairness index is: {result}')

if __name__ == "__main__":
    import doctest
    doctest.testmod()