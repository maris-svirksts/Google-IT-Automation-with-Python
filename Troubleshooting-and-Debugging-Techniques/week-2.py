#!/usr/bin/env python3

# Qwiklabs Assessment: Performance Tuning in Python Scripts

from multiprocessing import Pool, cpu_count
import subprocess
import os

home_path = os.path.expanduser('~')
src       = home_path + "/data/prod/"
dest      = home_path + "/data/prod_backup/"

if __name__ == "__main__":
    pool = Pool(cpu_count())
    pool.apply(subprocess.call, args=(["rsync", "-arq", src, dest],))