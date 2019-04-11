#!/usr/bin/env python

from urllib2 import urlopen
from urlparse import urljoin
from bs4 import BeautifulSoup

baseURL = "http://127.0.0.1/"
targetFile = "target.txt"

todoLinks = [baseURL]
doneLinks = []
bigCount = 0

while len(todoLinks) > 0:
    bigCount += 1
    print("Searching (%d): %s" % (bigCount, todoLinks[0]))
    soup = BeautifulSoup(urlopen(todoLinks[0]))
    parsedLinks = soup.find_all('a', href=True)

    counter = 0
    for a in parsedLinks:
        href = a.get("href", None)

        # Skip the first 4 links
        if counter <= 4:
            counter += 1
            continue

        # Is the link the target file?
        if a.text == targetFile:
            print("Found file at: %s" % (todoLinks[0] + href))
            exit(0)

        # Add the link to check
        todoLinks.append(todoLinks[0] + href)

    # Remove the current link from the todos
    del todoLinks[0]

print("File not found =[");
exit(0)