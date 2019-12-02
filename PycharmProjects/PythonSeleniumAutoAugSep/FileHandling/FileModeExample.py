"""
“ r “, for reading.
“ w “, for writing.
“ a “, for appending.
“ r+ “, for both reading and writing

"""


file = open("../FileHandling/testdata.txt","r+")
print(file.read())
file.close()

with open("../FileHandling/testdata.txt","a") as file:
    file.newlines
    file.write("Appending the file")
    file.write("\n")

