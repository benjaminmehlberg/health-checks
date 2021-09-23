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
timeout 10s mpstat -P ALL 1
/usr/bin/sleep 5

echo "Rolling Process summary"
timeout 10s pidstat 1
/usr/bin/sleep 5

echo "Workload/Performance for block devices (disks)"
timeout 10s iostat -xz 1
/usr/bin/sleep 5

echo "Free memory in megabytes"
free -m
/usr/bin/sleep 5

echo "Network interface workload"
timeout 10s sar -n DEV 1
/usr/bin/sleep 5

echo "TCP workload"
timeout 10s sar -n TCP/ETCP 1
/usr/bin/sleep 5

echo "Live Process summary"
timeout 10s top
/usr/bin/sleep 5
