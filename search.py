#!/usr/bin/env python

import requests
from urllib.parse import urljoin
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from bs4 import BeautifulSoup

baseURL = "http://10.46.225.216/flag2/"
targetFile = "flag2.txt"

todoLinks = [baseURL]
doneLinks = []
bigCount = 0

# Use a session for throttling
session = requests.Session()
retry = Retry(connect=3, backoff_factor=0.5)
adapter = HTTPAdapter(max_retries=retry)

while len(todoLinks) > 0:
    bigCount += 1
    print("Searching (%d): %s" % (bigCount, todoLinks[0]))
    response = session.get(todoLinks[0])
    soup = BeautifulSoup(response.content, "html.parser")
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
