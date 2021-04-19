

usernames = {'ID: 1' : 'PJ'}


for guesses in range(0,3):
    user = input("Sign in or Create an Account: ")
    
    
    if user == 'Sign in':
        name = input("Please enter your name: ")
        if name in usernames.values():
            
            break
        elif name not in usernames.values():
            guesses = guesses + 1
            print("****Access denied*** " + str(guesses) + " guesses") 
            print('Incorrect Name')
            
            
    elif user == 'Create an Account':
        name = input("Please enter your name: ")
        usernames[name] = name
        print("New Name Added: " + str(name))
        break



while True:
    if name not in usernames.values():
        break 
    if name in usernames.values():
        print('Access granted')
        break
    user = input('Do you want to sign in?: ')
    if user == 'Yes':
        name == input('Please enter your name: ')
        if name in usernames.values():
            print('Access Granted') 
            break
print("Access denied you ran out of guesses")        
           
