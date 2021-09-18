#!/bin/bash

# Recursive function to crawl through the filesystem
function iterate {
	for file in *; do
        if [ -d $file ]; then
            echo "Directory: "; echo $file
            cd $file
            iterate
        elif [ -f $file ]; then
            echo "File: "; echo $file
        else
            echo "Fin"
        fi
    done
    /bin/sleep 2
    pwd
    cd ..
    iterate
}

cd /home/pi/programs/files/filesystem

cwd="$(pwd)"
echo $cwd

for file in $(find * | grep .*.csv); do
    echo "----------------------------"
    echo $file
    for line in $(cat $file); do
        if [ -n $(echo $line | grep .*@.*) ]; then
            echo $line
        fi
    done
done

