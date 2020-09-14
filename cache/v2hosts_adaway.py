import re
import os
import requests

url = "https://adaway.org/hosts.txt"
s = requests.get(url).content.decode()
if '127.0.0.1' not in s:
    print("Reflash not success. Read local hosts.")
    with open('adaway.dat') as f:
        s = f.read()
else:
    with open('adaway.dat', 'w') as f:
        f.write(s)

list = re.findall("127.0.0.1 \S*\n", s)

out = ""
for s in list:
    s = s[10:]
    out += "DOMAIN,"+s

# add list
# with open('addlist.txt', 'r') as file:
#     out += file.read()

try:
    os.remove("adaway.list")
except:
    pass

with open('adaway.list', 'w') as file:
    file.write(out)

print("flash succeed.")
