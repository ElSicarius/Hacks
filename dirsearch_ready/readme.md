# purpose
takes urls from STDIN

prints the same url without the file part

this makes the url fuzz'ready for dirsearch

```bash
cat urls.file | python3.9 ./dirsearch_ready.py
```
