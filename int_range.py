import re

from natsort import natsorted
hosts = "pdcqa129|pdcqa220|pdcqa32|pdcqa36|pdcqa52|pdcqa219|pdcqa221|pdcqa25|pdcqa31|pdcqa119|pdcqa137"
host = (natsorted(hosts.split('|')))
#for i in host:
#    print(i)

inter = """
Eth1/1        eth    25G     pdcqa25-nic1
Eth1/2        eth    25G     pdcqa25-nic2
Eth1/5        eth    25G     pdcqa31-nic1
Eth1/6        eth    25G     pdcqa31-nic2
Eth1/7        eth    25G     pdcqa32-nic1
Eth1/8        eth    25G     pdcqa32-nic2
Eth1/9        eth    25G     pdcqa36-nic1
Eth1/10       eth    25G     pdcqa36-nic2
Eth1/15       eth    25G     pdcqa52-nic1
Eth1/16       eth    25G     pdcqa52-nic2
Eth1/28       eth    25G     pdcqa137-nic1
Eth1/29       eth    25G     pdcqa137-nic2
Eth1/30       eth    25G     pdcqa129-nic1
Eth1/31       eth    25G     pdcqa129-nic2
Eth1/32       eth    25G     pdcqa219-nic1
Eth1/33       eth    25G     pdcqa219-nic2
Eth1/34       eth    25G     pdcqa220-nic1
Eth1/35       eth    25G     pdcqa220-nic2
Eth1/36       eth    25G     pdcqa221-nic1
Eth1/37       eth    25G     pdcqa221-nic2
"""
regex = r"(Eth\S+)"
match_all = re.finditer(regex, inter)
new_int = []
for match_int in match_all:
    new_int.append(match_int.group(1))
print(','.join(new_int))