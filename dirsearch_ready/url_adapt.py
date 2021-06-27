# takes urls from stdin and remove last part of path to fuzz for more dirs
# alternatively giives urls that might be useful to fuzz

import os
import sys
from urllib.parse import urlparse, urlunparse

for url in sys.stdin.readlines():
    url = urlparse(url)
    path = url.path
    if len(path.split("/"))>=1:
        path = os.path.join("/", *os.path.split(path)[:-1])
    sys.stdout.write(urlunparse(url._replace(path=path, query=""))+"\n")
