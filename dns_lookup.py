#This module would accept an IPV4 address and resolve the DNS

import argparse
import socket
from python_hosts import Hosts, HostsEntry


# parser=argparse.ArgumentParser()
# parser.add_argument('number',help="Returns the square of the given number",type=int,default=0,nargs='?')
# # parser.add_argument('-v','--verbose',help='Provides a verbose desc.',type=int,required=True,choices=[0,1])
# parser.add_argument('-v','--verbose',help="Provides a verobse desc. Add extra V for extra verbose",action='count',default=0)
# args=parser.parse_args()
# if args.verbose==0:
#     print(f"The option selected was 0 now we are squaring the number \t {args.number**2}")
# elif args.verbose==1:
#     print(f"The option selected was 1, we are multiplying the number -> {args.number} * 10 = {args.number*10}")
# elif args.verbose>=2:
#     print(f"Extra verbose was selected {args.number**2}")

# # print(args.number**2)
# #We can use 
# # match and case

def inputValidation(address):
    try:
        a,b,c,d=map(int,address.split("."))
        if(a>=0 and a<256 and b>=0 and b<256 and c>=0 and c<256 and d>=0 and d<256):
            return True
        else:
            return False
    except ValueError:
        return False

def is_private_ip(address):
    a,b,c,d=map(int,address.split("."))
    return (
        a==10 or
        (a==172 and b>=16 and b<=31) or
        (a==192 and b==168)
    )


def get_domain_by_ip(ip_address):
    try:
        hostname=socket.gethostbyaddr(ip_address)[0] #This works by using the PTR Records
        return hostname
    except socket.herror:
        return "Hostname not found"
    
def host_file_contents(ip_address):
    host=Hosts()

    #Itterate through all entries in the Host file
    for entry in host.entries:
        if entry.entry_type in ['ipv4','ipv6']:
            print(f"IP: {entry.address}, Names: {entry.names}")
        elif entry.entry_type == 'comment':
            print(f"Comment: {entry.comment}")



parser=argparse.ArgumentParser()
parser.add_argument("-a","--address",help="Enter the IPV4 address.",required=True)

args=parser.parse_args()
if inputValidation(args.address):
    if is_private_ip(args.address):
        print("Private IP address")
        host_file_contents()
    else:
        print(get_domain_by_ip(args.address))
else:
    print("Invalid IPV4 address")


