#!/usr/bin/env python3
"""
A script to perform mutliple system health checks
"""
import shutil
import psutil
import os
import sys
import subprocess
import re


def disk_usage():
    """Return True, if the current free disk space is lower 3GB"""

    return shutil.disk_usage("/").free / (2**30) < 3


def reboot_pending():
    """Return True if a reboot is pending"""

    return os.path.exists("/run/crond.reboot")


def free_memory():
    """Return True, if the current RAM is less than 20%"""

    return psutil.virtual_memory().free * 5 < psutil.virtual_memory().total


def cpu_usage():
    """Return True, if CPU usage ration is above 1"""

    res = subprocess.run(["uptime"], capture_output=True).stdout.decode()
    val = float(re.search(r".+: ([0-9].[0-9]{2}),.+", res).group(1))
    return val > 1


def localhost_present():
    """Check for localhost"""

    res = subprocess.run(["grep", "127.0.0.1", "/etc/hosts"])
    return res.returncode != 0

def cpu_temperature():
    """Display the current CPU temperature"""

    res = int(subprocess.run(["cat", "/sys/class/thermal/thermal_zone0/temp"], capture_output=True).stdout.decode().strip())
    return res < 80000

def main():

    checks = [
        ("Disk free more than 3 GB", disk_usage(), "Disk full."),
        ("Reboot pending", reboot_pending(), "Reboot pending!"),
        ("Virtual memory more than 1/5 total", free_memory(), "Low virtual memory."),
        ("CPU usage under ratio 1", cpu_usage(), "High CPU saturation."),
        ("CPU temperature", cpu_temperature, "Temperature")
    ]

    everything_ok = True
    
    for name, check, msg in checks:
        print(f"Checking: {name}")
        if check:
            print(msg)
            everything_ok = False

    if not everything_ok:
        print("Warning!")
        sys.exit(1)
    else:
        print("Everything ok.")
        sys.exit(0)

main()
