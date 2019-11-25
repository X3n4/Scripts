#!/bin/bash

for url in $(cat $1); do
         host ${url};
done | grep "has address" | cut -d " " -f4 | sort -u
