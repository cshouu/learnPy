from openpyxl import Workbook

wb = Workbook()

ws1 = wb.create_sheet("sheet1")
ws2 = wb.create_sheet("sheet2",-1)

ws = wb.active

ws.title = "New title"

print(wb.sheetnames)

ws["A4"] = 4

wb.save("workboot.xlsx")
