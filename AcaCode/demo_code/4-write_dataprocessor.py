#%%
with open('demo.txt', 'r') as frp:
    lines = frp.readlines()
    lines = lines[1:]

# Pick all of the names
names = []
for line in lines:
    line = line.replace('\n', '')
    line = line.split()
    names.append(line[0])
# %%
import sys
import os
res = os.popen('ls -1').read()

# %%
# [\w!#$%&'*+/=?^_`{|}~-]+(?:\.[\w!#$%&'*+/=?^_`{|}~-]+)*@(?:[\w](?:[\w-]*[\w])?\.)+[\w](?:[\w-]*[\w])?