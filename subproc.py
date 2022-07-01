#! python
import os
import subprocess

subprocess.run(["ls"])
subprocess.run(["date"])

result = subprocess.run(["host", "8.8.8.8"], capture_output=True)
print(result.returncode) #0
print(result.stdout) #b'8.8.8.8.in-addr.arpa domain name pointer dns.google.\n'
print(result.stdout.decode().split()) # ['8.8.8.8.in-addr.arpa', 'omain', 'name', 'pointer', 'dns.google.']

my_env = os.environ.copy()
my_env["PATH"] = os.pathsep.join(["/opt/myapp/", my_env["PATH"]])

result = subprocess.run(["myapp"], env=my_env)

usernames = {}
name = "Good_user"
usernames[name] = usernames.get(name, 0) + 1