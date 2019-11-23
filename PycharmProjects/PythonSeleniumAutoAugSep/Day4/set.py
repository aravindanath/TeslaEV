list = ["Arvind","Bharath","Sudhakar"]
print(list)
# Set
student = set()
empty = set()

student.add("Arvind")
student.add("Bharath")
student.add("Arvind")

empty =student.copy()
print(student)

student.pop()
print(student)


print(empty)
empty.add("Sudhakar")
print(empty)



# Create a list with repeats

l = [1,1,2,2,3,4,5,6,1,1]

# Cast as set to get unique values

print(set(l))

std = ["Suchitra","iswarya","Arvind","iswarya","Bharath"]

print(std)
print(set(std))

# Set
value ={"Arvind","Rakesk","Arun","Arun"}

print(value)
print(type(value))