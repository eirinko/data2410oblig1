import sys

'''
    Description: jfi(throughputlist) takes a list of throughput values for connections
    and calculates the Jains Fairness Index (JFI). 
    Documentation for Task 1.1 is given in the README.md file. Code for task 1.2 is given below.
'''

def jfi(throughputlist):
    #Some unit tests
    """
    >>> jfi([10,10,10])
    1.0
    >>> jfi(['bla',10,10])
    bla is not an integer and will not be added
    1.0
    >>> jfi([5,10])
    0.9
    """
    
    numerator = 0
    denominator = 0
    n = 0
    
    for i in range(0,len(throughputlist)):
        #Added a try/except in case of empty lines or lines not containing numbers
        try:
            number = int(throughputlist[i])
            numerator += number
            denominator += number*number
            n+=1
        except:
            #In case the list contains elements that can't be converted into integer.
            print(f"{throughputlist[i]} is not an integer and will not be added")
    return (numerator**2)/(n*denominator)

#Try to use the function jfi(throughputlist) with the given input
try:
    #Taking the input that comes after the name of the file that gets run.
    text = sys.argv[1] 
    
    with open(text) as f:
        #Removes new line characters and adds info to a list.
        lines = [line.rstrip() for line in f]
    result = jfi(lines)
    
    print(f'Jains Fairness index is: {result}')
    
except:
    #Error message in case the user forgets to provide input. 
    print("Either you forgot to provide a file as input in the terminal or your file is empty.")

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    