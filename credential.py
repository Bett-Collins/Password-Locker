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
    self.credential_name   = credential_name
    self.user_password   = user_password
    self.credential_password   = credential_password
     
    def save_credential(self):
        
        '''
        this is a methof that will save user's credentials
        '''
        
        Credentials.credential_list.append(self)
    
    
    def delete_credential(self):
        """
        it is a method to delete credentials
        """
        Credentials.credential_list.remove(self)
        
    @classmethod
       
    def get_credential(cls, credential_name):
       
        '''
         
        it is a method that take in the user_password and return the credential of the user
        '''
        for credential in cls.credential_list:
            if credential.credential_name == credential_name:
                return credential
            
            
    @classmethod
    def if_credential_available(cls, credential_name):
        """
        Method that checks if the credential of the user is available and return a boolean
        """
        for credential in cls.credential_list:
            if credential.credential_name == credential_name:
                return True
        return False   