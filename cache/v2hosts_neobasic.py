import re
import os
import requests

url = "https://cdn.jsdelivr.net/gh/neoFelhz/neohosts@gh-pages/basic/hosts"
s = requests.get(url).content.decode()
if '127.0.0.1' not in s:
    print("Reflash not success. Read local hosts.")
    with open('neoBasic.dat') as f:
        s = f.read()
else:
    with open('neoBasic.dat', 'w') as f:
        f.write(s)

list = re.findall(":: \S*\n", s)

out = ""
for s in list:
    s = s[3:]
    out += "DOMAIN,"+s

# add list
# with open('addlist.txt', 'r') as file:
#     out += file.read()

try:
    os.remove("neoHostBasic.list")
except:
    pass

with open('neoHostBasic.list', 'w') as file:
    file.write(out)

print("neoHostBasic flash succeed.")
