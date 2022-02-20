#!usr/bin/env python3.8
import unittest
from user import User 


class TestUser(unittest.TestCase):
     def setUp(self):
         '''
         setUp method enable test to be executed before each test
         '''
         
         self.new_user = User("Collins","Bett")
         
         def teardown(self):
             
             '''
             teardown method enable test to be executed after each test
             '''
             User.user_list = []
             
             def test_init(self):
                 
                 '''
                 test is used to see if the object has been initialized correctly
                 '''
                 self.assertEquals(self.new_user.user_name,"Collins")
                 self.assertEquals(self.new_user.user_password,"Bett")
                 
                 
             def test_save_user(self):
                   
                   '''
                  find user using username 
                   ''' 
                   self.assertEqual(len(User.user_list),1)
             
             
             
             def test_save_multiple_users(self):
                 
                 '''
                 find multiple users using saved user
                 '''
                 
                 self.new_user.save_user()
                 test_user = User("Collins","00000")
                 test_user.save_user()
                 self.assertEqual(len(User.user_list), 2)
                
                
             def test_delete_user(self):
                 
                 '''
                 deleting user's details
                 '''
                
             self.new_user.save_user()
             test_user = User("Collins","00000")
             test_user.save_user()
             self.new_user.delete_user()
             self.assertEqual(len(User.user_list), 1)   
                 
if __name__ == '__main__':
    unittest.main()
