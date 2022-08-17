#!/usr/bin/env python3

import os
import shutil # Disk Usage
import psutil # CPU utilization
import socket # Localhost
import emails

def check_disk_usage(disk):
    disk_usage = shutil.disk_usage(disk)
    free = disk_usage.free / disk_usage.total * 100
    return free < 20

def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    return usage > 80

def check_ram_usage():
    usage = psutil.virtual_memory().available / ( 1024 * 1024 )
    return usage < 500

def check_localhost():
    host = socket.gethostbyname('localhost')
    return host != '127.0.0.1'

sender   = "automation@example.com"
receiver = "{}@example.com".format(os.environ.get('USER'))
subject  = ""
body     = "Please check your system and resolve the issue as soon as possible."
flag     = False

if check_disk_usage('/'):
    subject += "Error - Available disk space is less than 20% "
    flag     = True

if check_cpu_usage():
    subject += "Error - CPU usage is over 80% "
    flag     = True

if check_ram_usage():
    subject += "Error - Available memory is less than 500MB "
    flag     = True

if check_localhost():
    subject += "Error - localhost cannot be resolved to 127.0.0.1 "
    flag     = True

if flag:
    message = emails.generate_email(sender, receiver, subject, body, '')
    emails.send_email(message)