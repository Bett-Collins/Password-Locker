from user import User
from credential import Credentials

def create_user(user_name,user_password):
    
    '''
   Function to create a user account 
  
    Args:
     name: function  to create user account   
    password: the password the user want for the account
        '''
        
    new_user = User(user_name,user_password)
    
    return new_user

def save_users(user):
    
    '''
    Function to save the user's details
    '''
    user.save_user()
    
def check_(name):
    
    '''
     Function that check if user account already exist
    
    Args:
    name: the user account name 
     '''    
     
    return User.user_exist(name)

def user_log_in(name,password):
    
    '''
    Function that enable the user to log-in into their credential account
    '''
    log_in = User.log_in(name, password)
    if log_in != False:
        return User.log_in(name, password)
    
    
def display_user():   
    '''
    This function show saved users

    '''
    return User.display_use()00


def create_credential(credential_name,user_password,credential_password):

    '''
     Function to create credential
    '''

new_credential = Credentials(credential_name):
           return new_credential


 def save_credential(credential):
    
    '''
   Function that saves credential
    
    Args:
        credential: credential that will be saved
        '''
    credential.save_credential()
    
    
    def check_credentials(credential_name):
      '''
    Function that check if the credential exist
    Args:
        name : the credential name
     '''

    return Credential.credential_exist(credential_name)

    def display_credentials(credential_password):
    
     '''
     Function that will display credential
    '''

    return Credential.display_credential(credential_password)

