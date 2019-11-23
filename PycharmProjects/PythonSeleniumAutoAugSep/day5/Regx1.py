import re
# Regular expression

NameAge = """Ravi is 32 and Ram is 22 
             Sonu is 20 and Avik is 27"""

ages = re.findall(r'\d{1,3}',NameAge)
names = re.findall(r'[A-Z][a-z]*',NameAge)

print(ages)
print(names)

emptyDict= {}

x = 0

for eachName in names:
    # Key = Value
    emptyDict[eachName] = ages[x]
    # x= x+1
    x=+1
print(emptyDict)

