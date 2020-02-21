#!/bin/bash

wget https://spyse.com/search/subdomain?q=$1
mkdir Documents/$1
cat subdomain\?q\=$1 | grep data-domain | cut -d "\"" -f4 > Documents/$1/subdomeinen.txt
 
