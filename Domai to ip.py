#Domain to IP
import socket
import pyfiglet
from termcolor import colored
print(colored("          ******* Domain To Ip Convertor******",'red'))
print(colored("           *******   Create by MWWVV  ******",'blue'))
banner = colored(pyfiglet.figlet_format("Domain To Ip"),'green')
print(banner)
domain_name = input("Enter Your target Domain:")
ip = socket.gethostbyname(domain_name)
print(ip)