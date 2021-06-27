# purpose
takes urls from STDIN

prints the same url without the file part

this makes the url fuzz'ready for dirsearch

# usage
```bash
cat urls.file | python3.9 ./dirsearch_ready.py
```
# example

```bash
echo "http://test.com:8080/test/test.php?aaaaaa=ssrf" | python3.9 dirsearch_ready.py

outputs:
http://test.com:8080/test?aaaaaa=ssrf
```
