#!usr/bin/env python3.8
import unittest
from user import User 


class User(unittest.TestCase):
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
                   
                   self.assertEqual(len(User.user_list),1)
             
             
             
             def test_save_multiple_users(self):
                self.new_user.save_user()
                test_user = User("Collins","00000")
                test_user.ssave_user()
                self.assertEqual(len(User.user_list), 2)
                     
                 
                if __name__ == '__main__':
                    unittest.main()
