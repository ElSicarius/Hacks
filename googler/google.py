from googlesearch import search
from urllib import error
import argparse

def google_this(what, row, n, offset=0, SafeSearch="off", lang="en", tld="com"):
    """
    -> what: la recherche à effectuer (str)
    -> row: nombre de résultats retournés par requête (int)
    -> n: le nombre de résultats à rapatrier (int)
    -> offset: offset de la recherche (int)
    """
    res = search(what, tld=tld, num=row, start=offset, stop=n, pause=5, lang=lang, safe=SafeSearch, extra_params={'filter': '0'})
    return res

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-s",'--search')
    args = parser.parse_args()
    
    if args.search:
        try:
            for i in google_this(args.search, 500, 500):
                print(i)
        except error.HTTPError:
            print("google cooldown :/")
    else:
        print("not enough args")
