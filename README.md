Oblig 1:
Task 1. 


jains.py accepts arguments from the terminal. The list received from the terminal contains the name of the file and then all the other inputs, but all are strings. The function inside jains.py calculates the JFI, and prints the information to the terminal. 

Task 2. 
Added a file called throughput_values.txt to the directory. Had to change the code to receive and open a file and process the information in that file into a list. 

Function jfi(throughputlist) calculates the Jains Fairness index based on the input list. If the list contains information that’s not a number it will not be added (have used try: except). Also added a ZeroDivisionError in case the list doesn’t contain any numbers. 

Added a try:except for getting input from the terminal and calling the jfi-function. If no input file is provided an error text will be displayed. 

Task 3.


Task 4.
See results and discussion in ping-s374940.txt.

Task 5.
See results and discussion in traceroute-s374940.txt.