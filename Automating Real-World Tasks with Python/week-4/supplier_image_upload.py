#!/usr/bin/env python3

import requests
from os import listdir, path, getcwd
from multiprocessing import Pool, cpu_count

url        = "http://localhost/upload/"
files_path = getcwd() + "/supplier-data/images/"
files      = listdir(files_path)
pool       = Pool(cpu_count())

def upload_file(file):
    file = files_path + file

    if path.isfile(file) and file.endswith('.jpeg'):
        with open(file, 'rb') as opened:
            r = requests.post(url, files={'file': opened})

for file in files:
    upload_file(file)
