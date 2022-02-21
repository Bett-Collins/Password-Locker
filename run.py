from user import User
from credential import Credentials

def create_user(name,password):
    
    '''
   Function to create a user account 
  
    Args:
     name: functio  to create user account   
    password: the password the user want for the account
        '''
        
    new_user = User(name,password)
    
    return new_user
