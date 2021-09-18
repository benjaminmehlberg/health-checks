#!/bin/bash

echo $$
echo $#
echo $@
echo $0

line="---------------------------------------------------->"

echo "Starting at: $(date)"

echo "Checking all log files"
for logfile in /var/log/*log; do
	echo "Processing: $logfile"
	cut -d " " -f 4- $logfile | sort | uniq -c | sort -nr | head
	echo $line
done


# print actual running processes in /run
echo "Printing all running processes."
for file in /run/*; do
	if [ -f $file ]; then
        echo "Processing: $file"
        head $file
        echo $line
    fi
done
