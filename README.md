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