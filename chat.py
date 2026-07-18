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
                smsbot.start()
            case "UPDATE":
                smsbot.update()
            case "VIEW":
                smsbot.view()
            case "QUIT":
                print("Exiting the chat. Goodbye!")
                break
            case _:
                print("Unknown command!")

chatting()