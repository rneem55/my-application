import re
mystr = "rneem"

for i in mystr:
    if re.search("(R|r)",i):
        print(i,end="")
