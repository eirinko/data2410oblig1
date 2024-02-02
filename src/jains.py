import sys

def jfi(throughputlist):
    #Some unit tests
    """
    >>> jfi(['bla',10,10,10])
    1.0
    >>> jfi([0,10,10,10])
    1.0
    """
    numerator = 0
    denominator = 0
    n = 0

    for i in range(1,len(throughputlist)):
        #Added a try/except in case of empty lines or lines not containing numbers
        try:
            number = int(throughputlist[i])
            numerator += number
            denominator += number*number
            n+=1
        except:
            print(f"{throughputlist[i]} is not a value and will not be added")
    if (n == 0 or denominator == 0):
        raise ZeroDivisionError
    return (numerator**2)/(n*denominator)

try:
    text = sys.argv[1] #Taking the input that comes after the name of the file.
    with open(text) as f:
        #Removes new line characters and adds info to a list.
        lines = [line.rstrip() for line in f]
    result = jfi(lines)
    print(f'Jains Fairness index is: {result}')
except:
    print("Either you forgot to provide a file as input in the terminal or your file is empty.")

if __name__ == "__main__":
    import doctest
    doctest.testmod()