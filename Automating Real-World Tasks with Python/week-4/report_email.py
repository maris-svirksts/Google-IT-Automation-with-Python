#!/usr/bin/env python3

import reports
import os
import datetime
import emails

todays_date      = datetime.date.today().strftime("%B %d, %Y")
attachment       = '/tmp/processed.pdf'
title            = "Processed Update on {}".format(todays_date)
description_list = []

description_dir   = os.getcwd() + "/supplier-data/descriptions/"
description_files = os.listdir(description_dir)

for file in description_files:
    with open(description_dir + file) as contents:
        description = "<br/>name: {}<br/>weight: {}<br/>".format(contents.readline(), contents.readline())
        description_list.append(description)

description = "".join(description_list)

if __name__ == "__main__":
    reports.generate_report(attachment, title, description)

    sender     = "automation@example.com"
    receiver   = "{}@example.com".format(os.environ.get('USER'))
    subject    = "Upload Completed - Online Fruit Store"
    body       = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    attachment = '/tmp/processed.pdf'

    message = emails.generate_email(sender, receiver, subject, body, attachment)
    emails.send_email(message)