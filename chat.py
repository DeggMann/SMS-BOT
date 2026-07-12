import smsbot
import pandas as pd

intromsg = "Welcome to the sms-bot automated chat. please text one of the folowing words: "

codewords = ["START", "UPDATE", "VIEW", "QUIT"]

def display_codewords(codewords=codewords):
    for number, codewords in enumerate(codewords, start=1):
        print(f"{number}. {codewords}")

def chatting():
    print(intromsg)
    display_codewords()
    while True:
        command = input("Select Option: ").strip().upper()
        match command:
            case "START":
                print("Enter the order details to add a new route.")
                smsbot.start()
            case "UPDATE":
                oid = input("Enter order number to update: ")
                curloc = input("Enter current location: ")
                smsbot.update(oid, curloc)
            case "VIEW":
                print("text 1 to view all orders or 2 to view a specific order")
                file_name = "route_sheet.xlsx"
                df = pd.read_excel(file_name)
                print(df.to_markdown(index=False))
            case "QUIT":
                print("Exiting the chat. Goodbye!")
                break
            case _:
            # The underscore (_) acts as the default / wildcard case
                print("Unknown command!")

chatting()