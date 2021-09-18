#!/bin/bash

res=$(cat /sys/class/thermal/thermal_zone0/temp)
echo $res
