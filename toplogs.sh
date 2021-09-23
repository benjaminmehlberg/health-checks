#!/bin/bash

line="---------------------------------------------------->"

echo "Starting at: $(date)"

# Print the most frequent entries in all logfiles
echo "Checking all log files"
for logfile in /var/log/*log; do
	echo "Processing: $logfile"
	cut -d " " -f 4- $logfile | sort | uniq -c | sort -nr | head
	echo $line
	/usr/bin/sleep 0.5
done


# Print actual running processes in /run
echo "Printing all running processes."
for file in /run/*; do
	if [ -f $file ]; then
        echo "Processing: $file"
        head $file
        echo $line
    fi
done
