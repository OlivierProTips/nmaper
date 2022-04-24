#!/usr/bin/env python3

import sys
import subprocess
import re

nmap_parameters = ['nmap', sys.argv[1], '-Pn', '-p-']
nmap_result = subprocess.run(nmap_parameters, stdout=subprocess.PIPE).stdout.decode('utf-8')

print(nmap_result)

regex = r"^\d.*$"

res = re.findall(regex, nmap_result,re.MULTILINE)

ports = []
if res:
    for portline in res:
        ports.append(portline.split("/")[0])

    nmap_parameters.remove('-p-')
    nmap_parameters.extend(['-p', ",".join(ports), '-A', '-oN', 'nmap.txt'])
    nmap_result = subprocess.run(nmap_parameters, stdout=subprocess.PIPE).stdout.decode(('utf-8'))

    print(nmap_result)

    subprocess.run(['code', 'nmap.txt'])