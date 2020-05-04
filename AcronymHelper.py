import sys
import argparse
import requests
from bs4 import BeautifulSoup
import urllib

# Argparse Setup

parser = argparse.ArgumentParser(description="This program exists as a sort of programming flashcard for acronyms and other terminology, by pulling the summary from Wikipedia.")
parser.add_argument('-p', metavar='date', type=str, nargs='+', help="The requested protocol or acronym to be looked up.")
args = parser.parse_args()
try:
  protocol = str(args.p[0])
except:
  print("Use the arugment -h to show the help prompts.")
  sys.exit()

# Hardcoding certain acronyms that have multiple non-computer related uses to the correct ones
if protocol == "TCP":
    protocol = "Transmission_Control_Protocol"


url = "https://en.wikipedia.org/wiki/" + protocol
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
for link in soup.find('p').getText():
    String = link
    print(String)