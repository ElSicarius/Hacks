

import argparse
import sys
import re
from urllib.parse import urlparse

def get_parser():
    """
    Parses the argparse object
    :returns the arguments object
    """
    parser = argparse.ArgumentParser(description='jslinkparser', epilog="")
    # data for getting the tool to work
    parser.add_argument("-f", "--file", default=None,help="Specify a burpjslinkfinder file", dest="infile")
    parser.add_argument("-scope", default=None,help="Specify the scope of your program (domain1.com,domain2.com,...)", dest="scope")
    return parser.parse_args()


if __name__ == "__main__":

    args = get_parser()
    scopes = args.scope
    if not scopes:
        exit("YOU MUST SPECIFY A SCOPE")
    scopes = scopes.split(",")
    with open(args.infile, "r") as file:
        content = file.read().strip()
        file.close()

    if not len(content)>0:
        exit("FILE IS EMPTY")

    first_split = content.split("[+] Valid URL found: ")[1:]

    for group in first_split:
        lines = group.splitlines()
        base_url = lines[0]
        base_url_temp = urlparse(base_url)
        ins = False
        for scope in scopes:
            if re.findall(f"{scope}$", base_url_temp.netloc.split(':')[0]):
                ins = True
        if not ins:
            continue
        sys.stdout.write(base_url+"\n")
        if not len(lines)>1:
            continue
        for line in lines[1:]:
            link = line.split(" - ")[1]
            if link.startswith("./"):
                link = link[1:]
                url = f'{base_url_temp.scheme}://{base_url_temp.netloc}/{"/".join(base_url_temp.path.split("/")[:-1])+link}'
                sys.stdout.write(url+"\n")
            elif link.startswith("/"):
                url = f'{base_url_temp.scheme}://{base_url_temp.netloc}{link}'
                sys.stdout.write(url+"\n")
            elif re.findall("^https?://", link, flags=re.IGNORECASE):
                netloc = urlparse(link).netloc.split(":")[0]
                ins = False
                for scope in scopes:
                    if re.findall(f"{scope}$", netloc):
                        ins = True
                if not ins:
                    continue
                sys.stdout.write(link+"\n")
            else:
                # relative path weird
                first_elm_name = link.split("/")[0]
                reg1 = re.compile(r"/"+first_elm_name+"/", flags=re.IGNORECASE)
                reg2 = re.compile(r"/[a-zA-Z0-9_\-]+?"+first_elm_name+r"[a-zA-Z0-9_\-]+?/",flags=re.IGNORECASE)
                if re.findall(reg1, base_url_temp.path):
                    url = f'{base_url_temp.scheme}://{base_url_temp.netloc}{"/".join(re.split(reg1,base_url_temp.path)[:-1])+link}'
                    sys.stdout.write(url+"\n")
                elif re.findall(reg2, base_url_temp.path):
                    url = f'{base_url_temp.scheme}://{base_url_temp.netloc}{"/".join(re.split(reg2,base_url_temp.path)[:-1])+link}'
                    sys.stdout.write(url+"\n")
                else:
                    link = "/"+link
                    url = f'{base_url_temp.scheme}://{base_url_temp.netloc}/{"/".join(base_url_temp.path.split("/")[:-1])+link}'
                    sys.stdout.write(url+"\n")
                    url = f'{base_url_temp.scheme}://{base_url_temp.netloc}{link}'
                    sys.stdout.write(url+"\n")
