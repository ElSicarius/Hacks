

import sys
import uuid


for line in sys.stdin.readlines():
    line = line.strip()
    method, url, _, *params = line.split(" ")
    query_params = [p.replace(",","")+f"={str(uuid.uuid4().hex)[:5]}" for p in params]
    for p in query_params:
        sys.stdout.write(url.replace(r"%s", p)+"\n")
    
