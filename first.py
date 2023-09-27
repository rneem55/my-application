import re
mystr = "rneem so"

for i in mystr:
    if re.search("(R|r)",i):
        print(i,end="")