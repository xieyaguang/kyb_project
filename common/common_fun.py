import sys
sys.path.append(r'F:/project/kyb_project')
from baseView.baseView import BaseView
from common.desired_caps import appium_desired
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import logging
import logging.config
import time
from appium import webdriver
import os
import csv

class Common(BaseView):
	cancel_upgradeBtn = (By.ID,'android:id/button2')
	skipBtnm = (By.ID,'com.tal.kaoyan:id/tv_skip')

	# 登录弹窗
	wemedia_cacel = (By.ID,'com.tal.kaoyan:id/view_wemedia_cacel')
	

	def check_updateBtn(self):
		logging.info("===========check_updateBtn===========")
		
		try:
			elemtnt = self.find_element(*self.cancel_upgradeBtn)
		except NoSuchElementException :
			logging.info('cancel_upgradeBtn element is not found!')
		else:
			logging.info('check_updateBtn')
			elemtnt.click()

	def check_skipBtnm(self):
		logging.info("===========skipBtnm===========")

		try:
			elemtnt = self.find_element(*self.skipBtnm)
		except NoSuchElementException :
			logging.info('skipBtn element is not found!')
		else:
			logging.info('skipBtnm')
			elemtnt.click()

	def get_screen_size(self):
		x = self.get_window_size()['width']
		y = self.get_window_size()['height']
		print(x,y)
		return (x,y)

	def swip_left(self):
		logging.info('======swip_left========')
		L = self.get_screen_size()
		
		x1 = int(L[0] * 0.95)
		x2 = int(L[0] * 0.25)
		y1 = int(L[1] * 0.5)
		self.swipe(x1,y1,x2,y1,1000)

	def get_time(self):
		self.now = time.strftime('%Y-%m-%d %H_%M_%S')
		return self.now

	def get_screen_shot(self,module):
		time = self.get_time()
		img_file = os.path.dirname(os.path.dirname(__file__))+'/screenshots/%s_%s.png'%(module,time)
		logging.info('get %s screenshot' % module)
		self.driver.get_screenshot_as_file(img_file)

	def check_marked_ad(self):
		logging.info('======check_marked_ad=======')
		try:
			element=self.find_element(*self.wemedia_cacel)
		except NoSuchElementException:
			logging.info('No wemedia_cacel')
			pass
		else:
			logging.info('close wemedia_cacel')
			element.click()
			
	def get_csv_data(self,csv_file,line):
		with open(csv_file,'r',encoding='utf-8-sig') as file:
			reader = csv.reader(file)
			for index,row in enumerate(reader,1):
				if index == line:
					return row



if __name__ == '__main__':
	driver=appium_desired()
	# c = Common(driver)
	# c.check_updateBtn()
	# c.check_skipBtnm()
	# # c.swip_left()
	# # c.swip_left()
	# c.get_screen_shot('start app')