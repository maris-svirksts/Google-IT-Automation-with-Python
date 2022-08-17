#!/usr/bin/env python3

from os import listdir, path, getcwd
from requests import post

description_dir   = getcwd() + "/supplier-data/descriptions/"
description_files = listdir(description_dir)

description_list = []

for file in description_files:
    with open(description_dir + file) as contents:
        description = {'name': contents.readline(), 'weight': int(contents.readline().split()[0]), 'description': contents.readline(), 'image_name': path.splitext(path.basename(file))[0] + '.jpeg'}
        description_list.append(description)

for description in description_list:
    response = post("http://[linux-instance-external-IP]/fruits/", data = description)

    if not response.ok:
        print("Failed with status code {}".format(response.status_code))