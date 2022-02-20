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
    
    self.new_credential = Credentials('Facebook','arapbett','bett@Collins')
    
    def tearDown(self):
        '''
        tearDown method clean up after each test case is run
        '''
        Credentials.credential_list = []
        
        def test_init_(self):
            
          """
        Test case to check if a new Credentials have been initiated properly 
        """
        self.assertEqual(self.new_credential.credential_name,'facebook')
        self.assertEqual(self.new_credential.user_password,'arapbett')
        self.assertEqual(self.new_credential.credential_password,'bett@collins')
       
   
   
    
    def save_credential_test(self):
        """
        test case to test if the crential object is saved into the credentials list.
        """
        self.new_credential.save_credential()
        self.assertEqual(len(Credentials.credential_list),1)
        
        
        
    def test_find_credential(self):
        """
        test to check if we can find a credential entry by account name and display the details of the credential
        """
        
        self.new_credential.find_credential()
        Credential_name = Credentials('facebook')
        Credential_name.find_credential()
        self.assertEqual(Credential_name.credential_list)

    def test_get_credential(self):
        """
        Test case tests whether saved user credentials are displayed
        """
        self.assertEqual(Credentials.find_credentials(), Credentials.user_credential_list)