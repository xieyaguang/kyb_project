import sys
sys.path.append(r'F:/project/kyb_project')
from common.desired_caps import appium_desired
import unittest
import time
import logging


class StartEnd(unittest.TestCase):
	def setUp(self):
		logging.info('=====setUp=======')
		self.driver = appium_desired()
		
	def tearDown(self):
		logging.info('=====tearDown=======')
		time.sleep(5)
		self.driver.close_app()
		# self.driver.close_app()
		