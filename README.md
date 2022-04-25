# NMAPER

Goal of this script is to automatize the namp commands I always use.

## Use case

Here are the nmap commands I do:

* `nmap IP`
* `nmap -p PORT1,PORT2,... -A -oN nmap.txt IP`

## Usage

`nmaper IP [OPTIONS]`

## Options

`ALL` can be added after the IP to add `-p-` to the first nmap command

## Install

1. Copy nmaper.py in /opt and make it executable
```bash
sudo cp nmaper.py /opt
sudo chmod +x /opt/nmaper.py
```

2. Create a nmaper file in /usr/local/bin with the following content:
```bash
#!/bin/bash

/opt/nmaper.py "$@"
```

3. Make nmaper file executable
```bash
sudo chmod +x /usr/local/bin/nmaper
```
