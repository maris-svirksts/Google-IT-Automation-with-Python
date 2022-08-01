#! python
import os
import datetime

if os.path.exists("novel.txt"):
    os.remove("novel.txt")

if os.path.exists("old.txt") and not os.path.exists("new.txt"):
    os.rename("old.txt", "new.txt")
    os.path.getsize("new.txt")
    timestamp = os.path.getmtime("new.txt")
    datetime.datetime.fromtimestamp(timestamp)
    datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')
    os.path.abspath("new.txt")

print(os.getcwd())

#os.mkdir("new_dir")
#os.chdir("new_dir")
#os.rmdir("new_dir")
#os.listdir("new_dir")

dir = "website"
for name in os.listdir(dir):
    fullname = os.path.join(dir, name)
    if os.path.isdir(fullname):
        print("{} is a directory".format(fullname))
    else:
        print("{} is a file ".format(fullname))