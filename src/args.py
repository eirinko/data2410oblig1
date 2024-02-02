import sys
import argparse

parser = argparse.ArgumentParser(description='simple args')

parser.add_argument('-s' , '--server', action='store_true')
parser.add_argument('-c' , '--client', action='store_true')
parser.add_argument('-p', '--port', type=int, default=8088)
parser.add_argument('-i', '--ip', type=str, default="10.0.0.2")

args = parser.parse_args()

#Setting up to test if the IP address is in the correct format
test_ip = args.ip.split(".")
notinrange = False
for number in test_ip:
    if int(number) not in range (0,255):
        notinrange = True

#Check for the range of the port
if args.port not in range(1024,65535):
    print("Invalid port. It must be within the range [1024,65535]")
#Check for the format of the IP address. 
#If it doesn't contain 4 numbers or the numbers are out of range you get a error message.
elif len(test_ip)!=4 or notinrange:
    print("Invalid IP. It must in this format: 10.1.2.3")
else:
    if args.server and args.client:
        print("You cannot use both at the same time")
    elif args.server:
        print(f"The server is running with IP address = {args.ip} and port address = {args.port}")
    elif args.client:
        print(f"The client is running with IP address = {args.ip} and port address = {args.port}")
    else:
        print("You should run either in server or client mode")
