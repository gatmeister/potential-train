import xlrd
import xlsxwriter

#read the excel file
loc = ("raw.xlsx")
row = 0
col = 0

wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 
sheet.cell_value(0, 0) 

#create the excel file
workbook = xlsxwriter.Workbook('output.xlsx')
worksheet = workbook.add_worksheet()

for i in range(sheet.nrows):
    rawData = sheet.cell_value(i, 0)

    worksheet.write(row, col, rawData)
    row +=1

workbook.close()
    



