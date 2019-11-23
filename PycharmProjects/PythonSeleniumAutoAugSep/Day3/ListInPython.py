
#         0 , 1,2,3
nl = ['Bharath',"Sudhakar","Suchitra","Suchitra"]

print("Total no of val",len(nl))
print(nl[::-1])
print(type(nl))

print(nl)
nl.append("Arvind")
print(nl)
co = nl.count("Arvind")
print(co)
nl.sort()
print(nl)
nl.sort(reverse=True)
print(nl)
print(nl.pop())

print(nl.remove("Sudhakar"))
print(nl)
nl.insert(0,"Iswarya")
print(nl)

nl.clear()
print(nl)