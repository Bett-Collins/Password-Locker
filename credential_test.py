'''
import unittest
import class Credential
'''

import unittest
from credential import Credentials

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