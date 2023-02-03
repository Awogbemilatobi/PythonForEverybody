"""prints all the links in an html page"""
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('a') # list of anchor tags
for tag in tags: # will go through a list of the anchor tags in the document
    print(tag.get("href", None)) #pull out href. i.e lines inside double quotes
