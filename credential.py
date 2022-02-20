from user import User

class Credentials:
    '''
    this class will enable the generation of instance classes
    '''
    credential_list = []
  
def _init_ (self,credential_name,user_password,credential_password):
      
    '''
    _init_ method will define the properties of the User objects
     
     args:
     self.user_password   = user_password
     self.credential_name   = credential_name
     self.credential_password   = credential_password
     
     '''
    self.user_password   = user_password
    self.credential_name   = credential_name
    self.credential_password   = credential_password
     
    def save_credential(self):
        
        '''
        this is a methof that will save user's credentials
        '''
        
        Credentials.credential_list.append(self)
        
    @classmethod 
       
    def generate_password(cls):
        
        '''
        it is a method used to generate password
        '''
        