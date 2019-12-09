x=int(input("Enter the gross Income:"))
y=int(input("Enter the percentage of State tax: "))
z=int(input("Enter the percentage of Central tax: "))
totaltax=y+z
a=(totaltax/100)*x
netincome=x-a
print("The Net income is:" + str(netincome))

