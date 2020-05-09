#!/usr/bin/python

import sys
import argparse
import requests
#The Following became a Bruh Moment after I spent an ungodly amount of time with beautiful soup.
#Literally https://xkcd.com/353/
import wikipedia
import urllib
import random

# Argparse Setup

parser = argparse.ArgumentParser(description="This program exists as a sort of programming flashcard for acronyms and other terminology, by pulling the summary from Wikipedia.")
parser.add_argument('-p', metavar='protocol', type=str, nargs='+', help="The requested protocol or acronym to be looked up. Inputting 'random' in place of a protocol will result in a randomized protocol from a list. Acronyms should be listed in full capitalization, eg 'TCP'.")
args = parser.parse_args()
try:
  usrinput = str(args.p[0])
except:
  print("Use the arugment -h to show the help prompts.")
  sys.exit()

# Hardcoding certain acronyms that have multiple non-computer related uses to the correct ones
def acronymcorrector(protocol):
  if protocol == "TCP":
    return "Transmission Control Protocol"
  elif protocol == "RIP":
    return "Routing Information Protocol"
  elif protocol == "RTP":
    return "Real-time Transport Protocol"
  elif protocol == "SIP":
    return "Session Initiation Protocol"    
  elif protocol == "RSVP":
    return "Resource Reservation Protocol"
  elif protocol == "POP":
    return "Post Office Protocol"
  elif protocol == "NTP":
    return "Network Time Protocol"
  elif protocol == "MGCP":
    return "Media Gateway Control Protocol"
  elif protocol == "UDP":
    return "User Datagram Protocol"
  elif protocol == "NDP":
    return "Neighbor Discovery Protocol"
  elif protocol == "ARP":
    return "Address Resolution Protocol"
  elif protocol == "MAC":
    return "Medium access control"
  #elif protocol == "":
    #protocol = ""
  else:
    return protocol


def wikipuller(page):
  protpage = wikipedia.page(title=page, auto_suggest=True)
  protsum = protpage.summary
  url = protpage.url
  print(protsum)
  print("")
  print("For more, go to "+ url)


if usrinput == "random":
  PickOne = True
else:
  PickOne = False
  propprot = acronymcorrector(usrinput)
  wikipuller(propprot)


randomprot = [
  "TCP",
  "FTP",
  "UDP",
  "DNS",
  "MAC",
  "UDP",
  "ARP",
  "NDP",
  "MGCP",
  "NTP",
  "POP",
  "RSVP",
  "SIP",
  "RTP",
  "RIP",
  "DCCP",
  "SCTP",
  "SSH",
  "SNMP",
  "RTSP",
  "NNTP",
  "MQTT",
  "LDAP",
  "IMAP",
  "HTTP",
  "HTTPS",
  "DHCP",
  "BGP",
  "XMPP",
  "OSPF",
  "L2TP",
  "PPP",

  ]


if PickOne == True:
  RNG = random.sample(randomprot, 1)
  RNGesus = RNG[0]
  Flashcard = "Flashcard"
  Description = "Description"
  flashmode = input("Random Protocol Selected, select flashcard mode or Random Description ['Flashcard', 'Description']: ")
  propprot = acronymcorrector(RNGesus)
  if flashmode == "Flashcard":
        print("Press Enter to proceed with the description of the following protocol:")
        print(RNGesus)
        try:
          input("")
        except:
          1==1
        wikipuller(propprot)
  elif flashmode == "Description":
        wikipuller(propprot)
        print("The described protocol is: " + RNGesus)

