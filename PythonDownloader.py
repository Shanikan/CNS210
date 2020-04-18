#!/usr/bin/python

import argparse
import requests
import bs4
from bs4 import BeautifulSoup
import urllib

parser = argparse.ArgumentParser(description="This program parses the Python Downloads Site and from it, downloads a version released on the requested day.")
parser.add_argument('-d', metavar='date', type=str, nargs='+', help="Date of Python Release (Month Day, Year) enclosed in quotes.")
args = parser.parse_args()
usrdate = str(args.d[0])
#TODO: Narrow Down to Look for Just DATE
# Try Searching for Explicit Date/Name
url = "https://www.python.org/downloads/"
versions = []
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
for link in soup.select('.list-row-container li'):
      String = str(link.prettify())
      #print(link)
      if usrdate in String:
        SplinterString = String.split()
        versions.append(SplinterString[6])
print(versions)
userspec = input("Select Version from the above list within quotations: ")
version = str(userspec)
print(version)        

#hardcoding it
gotcha = "https://www.python.org/ftp/python/" + version + "/Python-" + version + ".tar.xz"
filename = "seanulicny-python-" + version + ".tar.xz"
print("Starting Download")
urllib.urlretrieve(gotcha, filename)
print("Download Complete")