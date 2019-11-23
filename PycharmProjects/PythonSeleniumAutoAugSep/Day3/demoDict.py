student ={"name":"Sudhakar","Subject":"Python","tool":"pycham"}

print(student.keys())
print(student.values())
print(student)
student["Address"]="Hopefarm"

print(student)

for sud in student.items():
    print(sud)

group = {}
group = student.copy()

group["Exp"]="16"
print(group)