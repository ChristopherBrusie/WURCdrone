#!/bin/sh

mavproxy.py --master=/dev/serial0 --baudrate 921600 --out=udp:192.168.1.126:14550 --out=udp:127.0.0.1:14550 --out=udp:192.168.1.134:14550