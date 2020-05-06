#!/usr/bin/python

import sys
import argparse
import requests
from bs4 import BeautifulSoup
import urllib
import random

# Argparse Setup

parser = argparse.ArgumentParser(description="This program exists as a sort of programming flashcard for acronyms and other terminology, by pulling the summary from Wikipedia.")
parser.add_argument('-p', metavar='protocol', type=str, nargs='+', help="The requested protocol or acronym to be looked up. Inputting 'random' in place of a protocol will result in a randomized protocol from a list. Acronyms should be listed in full capitalization, eg 'TCP'. Protocols should be formated with underscores '_' replacing spaces.")
args = parser.parse_args()
try:
  usrinput = str(args.p[0])
except:
  print("Use the arugment -h to show the help prompts.")
  sys.exit()

# Hardcoding certain acronyms that have multiple non-computer related uses to the correct ones
def acronymcorrector(protocol):
  if protocol == "TCP":
    return "Transmission_Control_Protocol"
  elif protocol == "RIP":
    return "Routing_Information_Protocol"
  elif protocol == "RTP":
    return "Real-time_Transport_Protocol"
  elif protocol == "SIP":
    return "Session_Initiation_Protocol"    
  elif protocol == "RSVP":
    return "Resource_Reservation_Protocol"
  elif protocol == "POP":
    return "Post_Office_Protocol"
  elif protocol == "NTP":
    return "Network_Time_Protocol"
  elif protocol == "MGCP":
    return "Media_Gateway_Control_Protocol"
  elif protocol == "UDP":
    protocol = "User_Datagram_Protocol"
  elif protocol == "NDP":
    return "Neighbor_Discovery_Protocol"
  elif protocol == "ARP":
    return "Address_Resolution_Protocol"
  elif protocol == "MAC":
    return "Medium_access_control"
  #elif protocol == "":
        #protocol = ""
  else:
        return protocol

if usrinput == "random":
        PickOne = True
else:
  urladdendum = acronymcorrector(usrinput)

url = "https://en.wikipedia.org/wiki/" + urladdendum
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
for link in soup.find('p').getText():
    String = link
    #The following code is bullshit.
    print String,