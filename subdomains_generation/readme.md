# purpose

creates subdomains based on templates

this is usefull in bugbounty when companies use the same patterns to create subdomains

example template in templates/example


```bash
python3.9 generation.py <templatename> <app name>

Usefull example:

python3.9 generation.py example login | subjack 
```
# example with template example

for an app like "login" this will generate things like:

- login.example.com
- secure.dev1.login.example.com
- dev1.login.example.com
