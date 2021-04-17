usernames = {}
for guesses in range(0,3):
    name = input("Please enter your name: ")
    if name == "PJ":
        break
    elif name != "PJ":
        guesses = guesses + 1
        print("****Access denied*** " + str(guesses) + " guesses") 
        continue

while True:
    if name != "PJ":
        print("Access denied you ran out of guesses")
        value = input("Do you want to create an account? ")
        if value == "No":
            print("Good Bye")
            break 
        elif value == "Yes":
            new = input("Enter your name: ")
            usernames[name] = new
            print("New Name Added: " + str(new))
            break
    elif name == "PJ":
        print("Access Granted") 
        break

