import re
regex = r'172.[1-2][0-9].\d+.\d+'
result = []
def bin_ip(ip):
    octets = [int(o) for o in ip.split(".")]
    return ("{:08b}"*4).format(*octets)
with open('acl-pdc.txt') as f:
    for line in f:
        match = re.search(regex, line)
        if match:
            result.append(match.group())
s = (sorted(result, key=bin_ip))
for i in s:
    print(i)