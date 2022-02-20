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
    
    self.new_credential = Credentials('Collins','arapbett','bettcollins')
    
    def tearDown(self):
        '''
        tearDown method clean up after each test case is run
        '''
        Credentials.credential_list = []
        
        def test_init_(self):
            
          """
        Test case to check if a new Credentials have been initiated properly 
        """
        self.assertEqual(self.new_credential.credential_name,'Collins')
        self.assertEqual(self.new_credential.user_password,'2030')
        self.assertEqual(self.new_credential.credential_password,'bettcollins')
       
   
   
    
    def save_credential_test(self):
        """
        test case to test if the crential object is saved into the credentials list.
        """
        self.new_credential.credential_name()
        self.assertEqual(len(Credentials.credential_list),1)
        
        
        
    def test_find_credential(self):
        """
        test to check if we can find a credential entry by account name and display the details of the credential
        """
        self.new_credential_name.credential_name()
        test_credential_name = Credentials("Collins","arapbett","bettcollins")
        test_credential_name.save_credential_name()
        test_credential_name = Credentials.find_credential("Collins")
        self.assertEqual(the_credential_name.credential_name)
        
  