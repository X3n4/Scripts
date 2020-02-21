#!/bin/bash

# Obtain subdomains passively from spyse.com 
wget https://spyse.com/search/subdomain?q=$1
mkdir Documents/$1
cat subdomain\?q\=$1 | grep data-domain | cut -d "\"" -f4 > Documents/$1/subdomains.txt
rm subdomain\?q\=$1 


# Start Eyewitness on found subdomains
eyewitness -f Documents/$1/subdomains.txt

# Obtain IP-adresses from found subdomains
for url in $(cat Documents/$1/subdomains.txt); do
	 host ${url};
done | grep "has address" | cut -d " " -f4 | sort -u > Documents/$1/ips.txt

