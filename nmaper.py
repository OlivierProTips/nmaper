#!/usr/bin/env python3

import sys
import subprocess
import re

usage = """
nmaper IP [OPTIONS]

OPTIONS:
    ALL: add -p- to nmap
"""

if len(sys.argv) == 1:
    print(usage)
    sys.exit(1)

TARGET = sys.argv[1]
nmap_parameters = ['nmap', TARGET, '-Pn', '--min-rate=5000', '--open']
ALL_PORTS = '-p-'
FILENAME = "nmap.txt"

OPTIONS = {
    "ALL": [ALL_PORTS]
}

for arg in sys.argv[2:]:
    if arg in OPTIONS:
        nmap_parameters.extend(OPTIONS.get(arg))

nmap_result = subprocess.run(nmap_parameters, stdout=subprocess.PIPE).stdout.decode('utf-8')

print(nmap_result)

regex = r"^\d.*$"

res = re.findall(regex, nmap_result,re.MULTILINE)

ports = []
if res:
    for portline in res:
        ports.append(portline.split("/")[0])
    if ALL_PORTS in nmap_parameters:
        nmap_parameters.remove(ALL_PORTS)
        FILENAME = "nmap_all.txt"
        
    nmap_parameters.extend(['-p', ",".join(ports), '-sC', '-sV', '-oN', FILENAME])
    nmap_result = subprocess.run(nmap_parameters, stdout=subprocess.PIPE).stdout.decode(('utf-8'))

    print(nmap_result)

    # subprocess.run(['code', FILENAME])
