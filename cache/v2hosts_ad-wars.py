import re
import os
import requests

url = "https://raw.githubusercontent.com/jdlingyu/ad-wars/master/hosts"
s = requests.get(url).content.decode()
if '127.0.0.1' not in s:
    print("Reflash not success. Read local hosts.")
    with open('ad-wars.dat') as f:
        s = f.read()
else:
    with open('ad-wars.dat', 'w') as f:
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
    os.remove("ad-wars.list")
except:
    pass

with open('ad-wars.list', 'w') as file:
    file.write(out)

print("flash succeed.")
