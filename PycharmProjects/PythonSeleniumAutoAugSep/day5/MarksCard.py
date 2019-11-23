

marks = int(input("Enter your marks:"))

if marks >=0 and marks <35:
    print(" Fail")
elif marks >=35 and marks<50:
    print(" Pass class")
elif marks >= 50 and marks < 60:
    print(" Second class")
elif marks >= 60 and marks < 85:
    print(" First class")
elif marks >= 85 and marks < 100:
    print(" Top class")
else:
    print("Contact Admin")