#!/usr/bin/env python3

from os import listdir
from requests import post

feedback_dir   = "/data/feedback/"
feedback_files = listdir(feedback_dir)

review_list = []

for file in feedback_files:
    with open(feedback_dir + file) as contents:
        review = {'title': contents.readline(), 'name': contents.readline(), 'date': contents.readline(), 'feedback': contents.readline()}
        review_list.append(review)

for review in review_list:
    response = post("http://<corpweb-external-IP>/feedback/", data = review)
    if not response.ok:
        print("Failed with status code {}".format(response.status_code))