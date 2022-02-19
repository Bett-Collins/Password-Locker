class User:
    '''
    class will generate instance of user account
    '''
    user_list  =[]
   
    
    def _init_(self,user_name,user_password):
        '''
        we define the property object by using _init_
        '''
        
        self.user.name =user_name
        self.user_password = user_password
        '''
        args:
        user.name: name of  a user
        user_password: password of the user
        '''