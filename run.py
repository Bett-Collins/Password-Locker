from credential import Credential
from user import User

def create_user(user_name,user_password,user_email):
    '''
    Function to create a new account
    '''
    new_user = User(user_name,user_password,user_email)
    return new_user

def save_user(User):
    '''
    Function to save account
    '''
    User.save_user()   

def delete_user(User):
    '''
    Function to delete a account
    '''
    User.delete_user()    


def find_user_by_name(user_name):
    '''
    Function that finds a account by nane and returns the account
    '''
    return find_user_by_name(user_name)    

def user_exist(user_name):
    '''
    Function that check if an account exists with that name and return a Boolean
    '''
    return User.user_exist(user_name)    

def display_user():  
    '''
    Function that returns all the saved accounts
    '''
    return User.display_user()



def create_credential(credential_name,credential_password,user_account,email):
    '''
    Function to create a new account
    '''
    new_credential = Credential(credential_name,credential_password,user_account,email)
    return new_credential

def save_credential(credential):
    '''
    Function to save credential account
    '''
    credential.save_credential()    

def delete_credential(credential):
    '''
    Function to delete credential account
    '''
    credential.delete_credential()    


def find_by_credential_name(name):
    '''
    Function that finds a account by nane and returns the account
    '''
    return  Credential.find_by_credential_name(name)    

def ccredential_exist(name):
    '''
    Function that check if an account exists with that name and return a Boolean
    '''
    return Credential.credential_exist(name)    

def display_credential():
    '''
    Function that returns all the saved accounts
    '''
    return Credential.display_credential()  
 
 

def main():
    print("Hello! Welcome to Password Locker. What is your name?")
    user_name = input()
    print(f"Hello {user_name}, sign up to create an account.")
    print('\n')
    while True:
        print("Use these known short codes to operate :\n SU -> SIGN UP.\n DA -> Display account.\n LN ->LOGIN.\n ex ->exit Password Locker. ")
        short_code = input().lower()
        if short_code == 'su':
            print("Create an Account")
            print("_"*100)
            user_name = input('User name:')
            print ('\n')
            user_name = input('User_name:')
            print ('\n')
            pwd = input('Password: ')
            print ('\n')
            e_address = input('Email address:')
            save_user(create_user(user_name,pwd,e_address)) 
            print ('\n')
            print(f"A New {user_name} Account with the username  {user_name} has been created.")
            print(f"You can now login to your {user_name} account using your password.")
            print ('\n')
        elif short_code == 'da':
             if display_user():
                 print("Here are your account details:")
                 print('\n')
                 for User in display_user():
                     print(f"Account name:{User.user_name}  Username:  Password:{User.user_password}")
                     print('\n')
             else:
                 print('\n')
                 print("Account not found! Sign up to create a new account.")
                 print('\n')
        elif short_code == 'ln':
            print("Enter your password to log in:")
            search_user = input()
            if user_exist(search_user):
                search_user = find_user_by_name(search_user)
                print("\033[1;32;1m   \n")
                print(f"You are now logged in to your {user_name} account :)")
                print("\033[1;37;1m   \n")
                
                while True:
                    print('''
                    Use these short codes:
                    CA -> Create new credential.
                    DC -> Display your details.
                    ex ->Log out your details account.''')
                    short_code = input().lower()
                    if short_code == "ca":
                        print("Create new credential")
                        print('_' * 20)
                        credential_name = input('Credential_name:')
                        print('\n')
                        credential_name = input(f"{credential_name} credential_name:")
                        print('\n')
                        print('*' * 20)
                        pwd = input(f"{credential_name} credential_password:")
                        save_credential(create_credential(credential_name,credential_name,pwd,e_address))
                        print('\n')
                        print(f"A New {credential_name} Account with the username  {credential_name} has been created.")
                        print ('\n')
                    elif short_code == 'dc':
                         if display_credential():
                             print("Here are your details:")
                             print('\n')
                             for Credential in display_credential():
                                 print(f"credential_name:{Credential.credential_name}  Username: {Credential.credential_name} Password:{Credential.credential_password}")
                                 print('\n')
                         else:
                              print('\n')
                              print("You don't seem to have created any account yet")
                              print('\n')
                    elif short_code == "ex":
                        print('\n')
                        print(f"You have logged out of your {credential_name} account")
                        print('\n')
                        break
                        
            else:
                print('\n')
                print("INCORRECT PASSWORD!! PLEASE ENTER CORRECT PASSWORD:")
                print('\n')
                print('\n')
                    
        elif short_code == "ex":
                    print(f"Thank you {user_name} for your time!")
                    break
        else:
                    print("I did not understand. Please use the short codes provided")

if __name__ == '__main__':
    main()


