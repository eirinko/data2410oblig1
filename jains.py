import sys
#Should look more into unit testing in python.

def jfi(throughputlist):
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

print(jfi(listinput))

if __name__ == "__main__":
    import doctest
    doctest.testmod()