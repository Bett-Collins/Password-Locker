from curses.ascii import CR
import unittest # Importing the unittest module
from credential import Credential # Importing the account class


class TestAccount(unittest.TestCase):
    def setUp(self):
       
        self.new_credential = Credential("Collins","20202020","twitter","arapbett@g.com") # create Account object

    
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
      
        
        self.assertEqual(self.new_credential.credential_name,"Colins")
        self.assertEqual(self.new_credential.credential_password,"20202020")
        self.assertEqual(self.new_credential.user_account,"twitter")
        self.assertEqual(self.new_credential.email,"arapbett@g.com")

    def test_save_credential(self):
        '''
        test_save_account test case to test if the account object is saved into
         the account list
        '''
        self.new_credential.save_credential() # saving the new account
        self.assertEqual(len(Credential.credential_list),1)  


    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Credential.credential_list = []    


    def test_save_multiple_credential(self):
            '''
            test_save_multiple_account to check if we can save multiple account
            objects to our account_list
            '''
            self.new_credential.save_credential()
            test_credential = Credential("bett","arap","twitter","arap@g.com") # new account
            test_credential.save_credential()
            self.assertEqual(len(Credential.credential_list),2)

    def test_delete_credential(self):
            '''
            test_delete_account to test if we can remove an account from our account list
            '''
            self.new_credential.save_credential()
            test_credential = Credential("bett","arap","twitter","arap@g.com") # account
            test_credential.delete_credential()

            self.new_credential.delete_credential()# Deleting an account object
            self.assertEqual(len(Credential.credential_list),1)        
     
    def test_find_by_credential_name(self):
        '''
        test to check if we can find an account by account_name and display information
        '''

        self.new_credential.save_credential()
        test_credential = Credential("bett","arap","twitter","arap@g.com") # new account
        test_credential.save_credential()

        found_credential = Credential.find_by_credential_name("Test")

        self.assertEqual(found_credential.email,test_credential.email)    
    def test_account_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the account.
        '''

        self.new_credential.save_credential()
        test_credential = Credential("bett","arap","twitter","arap@g.com") # new account
        test_credential.save_credential()

        credential_exists = Credential.credential_exists("arap")

        self.assertTrue(credential_exists)
    def test_display_credential(self):
        '''
        method that returns a list of all accounts saved
        '''
        showed  = Credential.display_credential()
        self.assertEqual(showed,Credential.credential_list)    

if __name__ == '__main__':
    unittest.main()
    