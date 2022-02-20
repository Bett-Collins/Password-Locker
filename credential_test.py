'''
import unittest
import class Credential
'''

from ast import Import
import unittest
from credential import Credentials
import string

class TestCredential(unittest.TestCase):
    
    '''
    Test class will define test case for class Credential behavior
    
    Args:
     TestCase class helps create test classes
    '''
def setUp(self):
    
    '''
    setUp method runs before each test case 
    '''
    
    #Create Credential object
    
    self.new_credential = Credentials('Collins','paypal','Binance')
    
    def tearDown(self):
        '''
        tearDown method clean up after each test case is run
        '''
        Credentials.credential_list = []
        
        
   
    def test__init__(self,credential_name,user_password,credential_password):
        """
        method that defines storage of  user  credentials
        """
        self.user__password = user_password
        self.credential_name =credential_name
        self.credential_password = credential_password
    
    
    def save_credential(self):
        
        """
 the method will enable new storage in credential_list
        """
        Credentials.credential_list.append(self)
   
   
   
   
   
   
   
   
    @classmethod
    
    def verify_user(cls,credential_name,user_password,credential_password):
        
        '''
        the method is used to verify if the user is in th user_list
        '''
    
        non_user = ""
        for credential in credential.credential_list:
            if credential.credential_name == credential_name and credential_password == credential_password):
                non_user == Credentials.credential_name
                return non_user
    
         
         
    