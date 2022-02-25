import unittest

from user import User # Importing the unittest module



class Testdetails(unittest.TestCase):
    def setUp(self):
       
        self.new_user = User("Colins","20202020","arapbett@g.com") # create Account object

    
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.user_name,"Collins")
        self.assertEqual(self.new_user.password,"20202020")
        self.assertEqual(self.new_user.email,"arapbett@g.com")

    def test_save_user(self):
        '''
        test_save_account test case to test if the account object is saved into
         the account list
        '''
        self.new_user.save_user() # saving the new account
        self.assertEqual(len(User.user_list),1)  


    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            User.user_list = []    


    def test_save_multiple_user(self):
            '''
            test_save_multiple_account to check if we can save multiple account
            objects to our account_list
            '''
            self.new_user.save_user()
            test_user = User("bett","arap""arap@.com") # new account
            test_user.save_user()
            self.assertEqual(len(User.user_list),2)


    def test_delete_user(self):
            '''
            test_delete_account to test if we can remove an account from our account list
            '''
            self.new_user.save_user()
            test_user = User("bett","arap""arap@.com") # account
            test_user.save_user()

            self.new_user.delete_user()# Deleting an account object
            self.assertEqual(len(User.user_list),1) 

    def test_find_user_by_name(self):
        '''
        test to check if we can find an account by account_name and display information
        '''

        self.new_user.save_user()
        test_user = User("bett","arap""arap@.com") # new account
        test_user.save_user()

        found_user = User.find_user_by_name("bett")

        self.assertEqual(found_user.user_email,test_user.user_email)  



    def test_user_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the account.
        '''

        self.new_user.save_user()
        test_user = User("bett","arap""arap@.com") # new account
        test_user.save_user()

        user_exists = User.user_exist("arap")
        self.assertTrue(user_exists)    
        
                       


if __name__ == '__main__':
    unittest.main()
    