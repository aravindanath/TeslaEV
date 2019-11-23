# cars = {'bmw': {'model':'550i','year':2016}, 'Benz': {'model':'c-Class','year':2019}}

# cars = {"Audi": {"model":"Q7","Colour":"White","Door":"5"},'bmw': {'model':'550i','year':2016}, 'Benz': {'model':'c-Class','year':2019}}
#
# print(cars["bmw"].keys())
# print(cars["bmw"].values())


students = {"Bharath":{"Hobbies":"Cricket","Address":"RRNagar","Company":"HCL"},"Sudhar":{"Hobbies":"Reading","Address":"Hopeform","Company":"TCS"},"Arvind":{}}
print(students["Bharath"])
print(students["Sudhar"])
print(students["Bharath"]["Hobbies"])
print(students["Sudhar"]["Company"])

students["Arvind"]["Hobbies"]="Cycling"
students["Arvind"]["Company"]="Payu"

print(students)