import re
mystr = "rnrwvdsr"

for i in mystr:
    if re.search("(R|r)",i):
        print(i,end="")
