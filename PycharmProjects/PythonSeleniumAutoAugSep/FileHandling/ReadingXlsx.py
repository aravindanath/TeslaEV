
import openpyxl as op

wb = op.load_workbook("../FileHandling/TestData.xlsx")

# activate demo.xlsx
sheet = wb.active
# get b1 cell value
b1 = sheet['A8']
print("b1 --> ", b1.value)
# get b2 cell value
b2 = sheet['B2']
print("b2 --> ", b2.value)
# get b3 cell value
b3 = sheet.cell(row=3, column=2)
print("b3 --> ", b3.value)

# with open("../FileHandling/TestData.xlsx","r+") as file:
