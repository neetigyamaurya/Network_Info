#This module would accept an IPV4 address and resolve the DNS

import argparse
import socket
from python_hosts import Hosts


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
    except (socket.herror, socket.gaierror):
        return "Hostname not found"
    
def host_file_contents(ip_address):
    host=Hosts()

    #Itterate through all entries in the Host file
    for entry in host.entries:
        if entry.entry_type in ['ipv4','ipv6']:
            if ip_address == entry.address:
                return entry.names
    return None

def domain_validation(domain_name):
    try:
        return socket.gethostbyname(domain_name)
    except socket.gaierror:
        return "Invalid domain name"


def cross_validation(domain_name):
    ip_address=domain_validation(domain_name)
    if ip_address == "Invalid domain name":
        print(ip_address)
        return
    print(f"{domain_name} -> {ip_address} -> {get_domain_by_ip(ip_address)}")


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("-a","--address",help="Enter the IPV4 address.")
    parser.add_argument("-d","--domain",help="Enter an domain name to get the IP")
    parser.add_argument("-c","--cross_validation",help="Cross Validates and IP with Domain")

    args=parser.parse_args()
    if args.domain:
        print(domain_validation(args.domain))
    elif args.cross_validation:
        cross_validation(args.cross_validation)
    if args.address and inputValidation(args.address):
        if is_private_ip(args.address):
            print("Private IP address")
        else:
            print(get_domain_by_ip(args.address))
            hosts_entry=host_file_contents(args.address)
            if hosts_entry:
                print(hosts_entry)
    elif args.address:
        print("Invalid IPV4 address")


if __name__ == "__main__":
    main()


