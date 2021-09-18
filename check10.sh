#!/bin/bash

echo "To check average load in the last 1, 5, 15 minutes"
uptime
/usr/bin/sleep 5

echo "To check last 10 system messages"
dmesg | tail
/usr/bin/sleep 5

echo "Virtual memory load, r = number of processes waiting for CPU"
timeout 10s vmstat 1
/usr/bin/sleep 5

echo "CPU time breakdowns per CPU"
mpstat -P ALL 1
/usr/bin/sleep 5

echo "Rolling Process summary"
pidstat 1
/usr/bin/sleep 5

echo "Workload/Performance for block devices (disks)"
iostat -xz 1
/usr/bin/sleep 5

echo "Free memory in megabytes"
free -m
/usr/bin/sleep 5

echo "Network interface workload"
sar -n DEV 1
/usr/bin/sleep 5

echo "TCP workload"
sar -n TCP/ETCP 1
/usr/bin/sleep 5

echo "Live Process summary"
top
/usr/bin/sleep 5
