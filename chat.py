intromsg = "Welcome to the sms-bot automated chat. please text the folowing options: "

codewords = ["START", "UPDATE", "DONE", "SELECT", "QUIT"]

def display_codewords(codewords=codewords):
    for number, codewords in enumerate(codewords, start=1):
        print(f"{number}. {codewords}")

def chatting():
    print(intromsg)
    display_codewords()
    while True:
        user_input = input("Enter your choice: ").strip().upper()
        if user_input in codewords:
            print(f"You selected: {user_input}")
            # Add logic for each codeword here
            if user_input == "QUIT":
                print("Exiting chat. Goodbye!")
                break
        else:
            print("Invalid option. Please try again.")

chatting()