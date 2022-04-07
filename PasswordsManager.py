import re

def new_passwd(user_name, user_pass):  
    user_name = input("Please type your username: ").lower()
    user_pass = input("Please choose a strong Password (above 6 characters): ")
    check = re.compile(r'[A-Z]+[a-z]+/d+[!@#\$%^&*\(\)\[\]\\_+]+')
    
    if check.match(user_pass) and len(user_pass) > 6:
        with open('passwords.txt', 'a') as f:
         f.write(user_name + "|" + user_pass + "\n") 
        return "Strong password!"
            
    while check.match(user_pass) != True or len(user_pass) <= 6:
        if check.match(user_pass):
            break
        else:
            return "Weak password!"
            continue
            
        if len(user_pass) > 6:
            break
        else:
            return "Short password!"
            continue
    print(user_name, "Your password saved to the PasswordManager")     
        
def view_passwd():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
                data = line.rstrip()
                user, passw = data.split("|")
                print("User name:", user, "| User password:", passw)


while True:
    action = input("Would you like to add a new password to the PasswordsManager or view existing ones? (Add/View)press 'Q' to quit?: ").lower()
    if action =="q":
        print("Goodbye :)")
        break
    elif action == "add":
        new_passwd(user_name = input(), user_pass = input())
    elif action == "view":
        view_passwd()
    else:
        print("Invalid option")
        break

