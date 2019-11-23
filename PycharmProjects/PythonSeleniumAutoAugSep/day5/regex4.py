import re


strVar = "Sat,Hat,mat,pat"

allStr = re.findall("[Shmp]at",strVar)

for i in allStr:
    print(i)