import sys
sys.path.append(r'F:/project/kyb_project')
from businessView.registerView import RegisterView
from common.myunit import StartEnd
import logging
import unittest
import random

class RegisterTest(StartEnd):
	
	def test_user_register(self):
		
		logging.info('===RegisterTest====')
		r = RegisterView(self.driver)

		username = 'zxw2018' + 'FLY' + str(random.randint(1000, 9000))
		password = 'zxw' + str(random.randint(1000, 9000))
		email = '51zxw' + str(random.randint(1000, 9000)) + '@163.com'
		self.assertTrue(r.registerView_action(username, password, email))

 
if __name__ == '__main__':
	unittest.main()