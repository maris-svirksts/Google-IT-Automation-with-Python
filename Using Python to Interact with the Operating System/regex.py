#!python
#import re

#log ="1231321[23432]456456"
#regex = r"\[(\d+)\]"
#result = re.search(regex, log)
#print(result[1])

# grep thon /usr/share/dict/words

#result = re.search(r"aza", "plaza")
#print(result)

#re.search(r"p.ng", "Pangaea", re.IGNORECASE)

#result = re.search(r"^(\w*), (\w*)$", "Lovelace, Ada")
#result[0] == "Lovelace, Ada"
#result[1] == "Lovelace"
#result[2] == "Ada"
#print("{} {}".format(result[2], result[1])) # Ada Lovelace
#print(re.findall(r"\b[a-zA-Z]{5}\b", "A scary ghost appeared")) #get full words.

import re
def transform_record(record):
  new_record = re.sub(r",([0-9]\-)+,]", '+1-' + r'\1', record)
  return new_record

print(transform_record("Sabrina Green,802-867-5309,System Administrator")) 
# Sabrina Green,+1-802-867-5309,System Administrator

print(transform_record("Eli Jones,684-3481127,IT specialist")) 
# Eli Jones,+1-684-3481127,IT specialist

print(transform_record("Melody Daniels,846-687-7436,Programmer")) 
# Melody Daniels,+1-846-687-7436,Programmer

print(transform_record("Charlie Rivera,698-746-3357,Web Developer")) 
# Charlie Rivera,+1-698-746-3357,Web Developer

