# takes urls from stdin and remove last part of path to fuzz for more dirs
# alternatively giives urls that might be useful to fuzz

import os
import sys
import re
from urllib.parse import urlparse, urlunparse

for url in sys.stdin.readlines():
    url = urlparse(url)
    path = os.path.split(url.path)
    if len(path) >= 1 and re.findall("\.[a-zA-Z\d]+", str(path[-1])):
        path = path[:-1]
    path = os.path.join("/", *path)
    sys.stdout.write(urlunparse(url._replace(path=path, query=""))+"\n")
