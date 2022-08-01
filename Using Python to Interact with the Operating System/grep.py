
#!/usr/bin/env python3
import sys
import subprocess

file = open(sys.argv[1])

lines = file.readlines()

for old_line in lines:
  cleaned_line = old_line.strip()
  new_line = cleaned_line.replace("jane", "jdoe")
  command = "mv {} {}".format(cleaned_line, new_line)
  print(command)
  subprocess.run(command, shell=True)

file.close()
