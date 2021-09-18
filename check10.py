#!/usr/bin/env python3
import subprocess
import time
import os

intervall = "10s"
freq = "1"
checks = {
    "uptime": ["To check average load in the last 1, 5, 15 minutes", "uptime"],
    "dmesg": ["To check last 10 system messages", "dmesg"],
    "vmstat": ["Virtual memory load, r = number of processes waiting for CPU", "vmstat", freq],
    "mpstat": ["CPU time breakdowns per CPU", "mpstat", "-P", "ALL", freq],
    "pidstat": ["Rolling Process summary", "pidstat", freq],
    "iostat": ["Workload/Performance for block devices (disks)", "iostat", "-xz", freq],
    "free": ["Free memory in megabytes", "free", "-m"],
    "sar DEV": ["Network interface workload", "sar", "-n", "DEV", freq],
    "sar TCP": ["TCP workload", "sar", "-n", "TCP", freq],
    "top": ["Live Process summary", "atop"]
    }

for name, check in checks.items():
    print("----------------------------------------", "\n", name)
    print(check[0], "\n")
    lst = ["timeout", intervall, *check[1:]]
    print(lst)
    subprocess.run(lst, shell=False)
    choice = input("Enter 'q' to quit or press <Enter> to continue >>")
    if choice.lower() == 'q':
        break
