import openpyxl
# test code for adding a new route to the route_sheet.xlsx file
file_name = "route_sheet.xlsx"

workbook = openpyxl.load_workbook(file_name)
sheet = workbook.active

"""new_route_data = [104, "New York", "Philadelphia", "Washington D.C."]

sheet.append(new_route_data)

workbook.save(file_name)
print("Successfully added the new route data!")"""

def start():
    order_number = input("Enter order number: ")
    origin = input("Enter origin: ")
    destination = input("Enter destination: ")

    route_data = [order_number, origin, origin, destination, "In Transit"]
    sheet.append(route_data)
    workbook.save(file_name)
    print("Successfully added the new route data!")

def update(order_number, current_location):
    for row in sheet.iter_rows(min_row=2, values_only=False):
        if row[0].value == order_number:
            row[2].value = current_location

            if current_location == row[3].value:
                row[4].value = "Delivered"

            workbook.save(file_name)
            print(f"Successfully updated order {order_number} with current location: {current_location}")
            return
    print(f"Order number {order_number} not found.")


