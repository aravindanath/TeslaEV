"""
With the "With" statement, you get better syntax and exceptions handling.

"The with statement simplifies exception handling by encapsulating common
preparation and cleanup tasks."

In addition, it will automatically close the file. The with statement provides
a way for ensuring that a clean-up is always used.

"""


# Without the with statement, we would write something like this:


file = open("newFile.txt")

data = file.read()

print(data)

file.close()  # It's important to close the file when you're done with it


# Opening a file using with is as simple as: with open(filename) as file:


with open("newFile.txt") as file: # Use file to refer to the file object

   data = file.read()



with open('output.txt', 'w') as file:  # Use file to refer to the file object

    file.write('Hi there!')

