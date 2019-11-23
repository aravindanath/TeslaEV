# List empty
list = ["Arvind","Naina","Umesh","Bharath","Priya"]

print(list)
print("No of values: ",len(list))
print(type(list))
list.append("Shybindh")
print(list)
print(list.index("Shybindh"))
list.insert(0,"Shybindh")
print(list)

list.sort()
print(list)

list.sort(reverse=True)
print(list)
list.pop()
print(list)
list.remove("Priya")
print(list)
print(list[3])

score = []

print(score)
score.append(99)
print(score)
score.append("Ninty")
print(score)

