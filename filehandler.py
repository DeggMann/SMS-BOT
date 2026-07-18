import openpyxl

#file_name = "route_sheet.xlsx"

"""workbook = openpyxl.load_workbook(file_name)
sheet = workbook.active

new_route_data = [104, "New York", "Philadelphia", "Washington D.C."]

sheet.append(new_route_data)

workbook.save(file_name)
print("Successfully added the new route data!")"""

def save_data(new_route_data):
    file_name = "route_sheet.xlsx"

    workbook = openpyxl.load_workbook(file_name)
    sheet = workbook.active

    sheet.append(new_route_data)

    workbook.save(file_name)
