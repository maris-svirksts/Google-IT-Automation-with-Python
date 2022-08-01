#!/usr/bin/env python3
import re
import sys
import csv

def parse_log(file):
    error    = {}
    per_user = {}

    regex = r".* ticky: (INFO|ERROR) (.*) \((.*)\)"

    log_file = open(file)

    for line in log_file.readlines():
        result = re.search(regex, line)

        if result is not None:
            if "ERROR" not in line:
                print(result.group(3))
                per_user[result.group(3)] = {
                    "Username": per_user.get(result.group(3), {}).get("Username", result.group(3)),
                    "INFO":     per_user.get(result.group(3), {}).get("INFO", 0) + 1,
                    "ERROR":    per_user.get(result.group(3), {}).get("ERROR", 0)
                }
            else:
                error[result.group(2)]    = error.get(result.group(2), 0) + 1
                per_user[result.group(3)] = {
                    "Username": per_user.get(result.group(3), {}).get("Username", result.group(3)),
                    "INFO":     per_user.get(result.group(3), {}).get("INFO", 0),
                    "ERROR":    per_user.get(result.group(3), {}).get("ERROR", 0) + 1
                }

    log_file.close()

    sort_errors   = sorted(error.items(), key=lambda item: item[1], reverse = True)
    sort_per_user = sorted(per_user.items())

    return sort_errors, sort_per_user

def file_output(errors, per_user):
    with open('user_statistics.csv', 'w') as csvfile:
        csvfile.write("Username,INFO,ERROR\n")
        for line in per_user:
            csvfile.write("{},{},{}\n".format(line[1].get("Username", ""), line[1].get("INFO", 0), line[1].get("ERROR", 0)))

    with open('error_message.csv', 'w') as csvfile:
        result_file = csv.writer(csvfile)
        result_file.writerow(['Error', 'Count'])

        for error in errors:
            result_file.writerow(error)

if __name__ == "__main__":
  #log_file         = sys.argv[1]
  log_file         = "syslog.log"
  errors, per_user = parse_log(log_file)

  file_output( errors, per_user )

  sys.exit(0)
