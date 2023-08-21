# ARP-Cache-Poisoning
 **Disclaimer: this is for educational purpose only ; Do not use against any network you don't own.**


#by gilles karougbe

#This Script is written as part of my internship (jully-august 2022) on the topic 'network attacks by layers'

#This  work is supervised by Pr Mohammed SABER ,teacher at ENSAO

# [steps to use the program]

    $ git clone https://github.com/gil01karougbe/ARP-Cache-Poisoning.git

    $ cd ARP-Cache-Poisoning

     $ pip install -r requirements.txt

    $ sudo python3 arp_poison.py -M hacker_mac -V victim_mac victim_ip -R getway_mac getway_ip


# Remarques
Run 

      $ arp-scan -I eth0 192.168.1.0/24

To discover Informations about the network in order to lunch the attack
