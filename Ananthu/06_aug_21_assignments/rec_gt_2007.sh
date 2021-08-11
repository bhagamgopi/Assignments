#!/bin/bash

lines=`cat aids.csv| wc -l`

cat aids.csv | tail -n $(( lines-1 )) |  while read line

do
	year=`echo $line | cut -d"," -f2 | tr -d '"'`
	if [[ $year -gt 2007  ]]
	then
		echo $line
	fi
done
