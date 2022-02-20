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
        
        
    def test_init(self):
        '''
        TestCase test if the object is initialised properly 
        '''
    # self.assertEquals(self.new_credential_name.credential_name, "Collins")
    # self.assertEquals(self.new_credential_password.credential_password, "2030")
    
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
    
         
         
    