import re
import os
import requests

url = "https://cdn.jsdelivr.net/gh/neoFelhz/neohosts@gh-pages/full/hosts"
s = requests.get(url).content.decode()
if '0.0.0.0' not in s:
    print("Reflash not success. Read local hosts.")
    with open('neoFull.dat') as f:
        s = f.read()
else:
    with open('neoFull.dat', 'w') as f:
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
    os.remove("neoHostFull.list")
except:
    pass

with open('neoHostFull.list', 'w') as file:
    file.write("DOMAIN,"+out)

print("neoHostFull flash succeed.")
