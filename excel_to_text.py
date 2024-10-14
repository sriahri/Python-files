import xlrd

wb = xlrd.open_workbook("stocks.xls")
sheet = wb.sheet_by_index(0)
number_of_rows = sheet.nrows
number_of_cols = sheet.ncols

file = open('allstocks.txt', 'w')
for i in range(number_of_rows):
    for j in range(number_of_cols):
        if j != number_of_cols - 1:
            file.write(str(sheet.cell_value(i, j)) + ',')
        else:
            file.write(str(sheet.cell_value(i, j)) + '\n')

file.close()