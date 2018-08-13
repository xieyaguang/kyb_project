import sys
sys.path.append(r'F:/project/kyb_project')
import unittest
from businessView.loginView import LoginView
from common.myunit import StartEnd
import logging
import csv

class  LoginTest(StartEnd):
	csv_file = '../data/login_data.csv'

	def test_login_zxw2017(self):
		logging.info("====start=====")
		l = LoginView(self.driver)
		
		data = l.get_csv_data(self.csv_file,1)
		l.login_action(data[0],data[1])
		l.check_agree_alert()
		self.assertTrue(l.check_login_staus())
		# l.check_login_staus()
		

if __name__ == '__main__':
	unittest.main()
