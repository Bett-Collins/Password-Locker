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
                 self.assertEqual(self.new_user.user_name,"Collins")
                 self.assertEqual(self.new_user.user_password,"Bett")
             
             if __name__ == '__main__':
              unittest.main()
