#! python

def validate_user(username, minlen):
    assert type(username) == str, "username must be a string"
    if minlen < 1:
        raise ValueError("minlen must be at least 1")
    return True

filename = ""
try:
  f = open(filename)
except OSError:
  print("An OSError occurred")