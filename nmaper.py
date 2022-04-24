#!/usr/bin/env python3

import sys
import subprocess
import re

nmap_result = subprocess.run(['nmap', '-p-', sys.argv[1]], stdout=subprocess.PIPE)

print(nmap_result.stdout.decode('utf-8'))

regex = r"^\d.*$"

res = re.findall(regex, nmap_result.stdout.decode('utf-8'),re.MULTILINE)

ports = []
if res:
    for portline in res:
        ports.append(portline.split("/")[0])

print(",".join(ports))

full_nmap_result = subprocess.run(['nmap', '-p', ",".join(ports), "-A", sys.argv[1], '-oN', 'nmap.txt'], stdout=subprocess.PIPE)

print(full_nmap_result.stdout.decode(('utf-8')))

subprocess.run(['code', 'nmap.txt'])