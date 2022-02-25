class Credential:
    """
    Class that generates new instances of users.
    """
    credential_list = [] 

    def __init__(self,credential_name,credential_password,user_account,email):
       
       
        self.credential_name = credential_name
        self.credential_password = credential_password
        self.user_account = user_account
        self.email = email
    

    def save_credential(self):

        '''
        save_account method saves account objects into account_list
        '''

        Credential.credential_list.append(self)


    def delete_credential(self):

        '''
        delete_account method deletes a saved account from the account_list
        '''

        Credential.credential_list.remove(self)    
    @classmethod
    def find_by_credential_name(cls,credential_name):
        for Credential in cls.credential_list:
            if Credential.credential_name == credential_name:
                return Credential  
    

    @classmethod
    def credential_exist(cls,credential_name):
        '''
        Method that checks if a account exists from the account list.
        Args:
            name: Acc name to search if it exists
        Returns :
            Boolean: True or false depending if the account exists
        '''
        for Credential in cls.credential_list:
            if  Credential.credential_password == credential_name:
                    return Credential

        return False
    @classmethod
    def display_credential(cls):
        '''
        method that returns the account list
        '''
        return cls.credential_list
        