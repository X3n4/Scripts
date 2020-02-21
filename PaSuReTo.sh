#!/bin/bash

# Start script, accompanied by domain to scan. 

wget https://spyse.com/search/subdomain?q=$1
mkdir ~/$1
cat subdomain\?q\=$1 | grep data-domain | cut -d "\"" -f4 > ~/$1/subdomains.txt
 
