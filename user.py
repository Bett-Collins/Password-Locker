class User:
    '''
    class will generate instance of user account
    '''
    user_list  =[]
   
    
    def _init_(self,user_name,user_password):
        '''
        we define the property object by using _init_
        '''
        '''
         args:
        user.name: name of  a user
        user_password: password of the user
        '''
        
        self.user.name =user_name
        self.user_password = user_password
        
        def save_user(self):
            '''
            this method will save the user list
            '''
        User.user_list.append(self)
        
        @classmethod
        def find_credential(cls, name):
            
         '''
         this method check if credentials is imported correctly
           
           args:
           name:name of the credential
           
           Return:
           Boolean:True of false if credentail exist
           
           '''
        for credential in  credential.credential_list:
               if credential.credential_name == name:
                   return True