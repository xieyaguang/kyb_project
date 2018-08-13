import sys
sys.path.append(r'F:/project/kyb_project')
from common.common_fun import Common,By,NoSuchElementException
import logging,logging.config
from common.desired_caps import appium_desired

class LoginView(Common):
	#登页面元素
	username_type = (By.ID,'com.tal.kaoyan:id/login_email_edittext')
	password_type = (By.ID,'com.tal.kaoyan:id/login_password_edittext')
	loginBtn = (By.ID,'com.tal.kaoyan:id/login_login_btn')
	# 个人中心下线警告提醒alert
	tip_commit = (By.ID,'com.tal.kaoyan:id/tip_commit')
	#隐私条款
	tv_agree = (By.ID,'com.tal.kaoyan:id/tv_agree')
	
	#我的按钮
	button_mysefl = (By.ID,'com.tal.kaoyan:id/mainactivity_button_mysefl')
	# 登录用户名
	username = (By.ID,'com.tal.kaoyan:id/activity_usercenter_username')

	# 退出
	RightButton = (By.ID,'com.tal.kaoyan:id/myapptitle_RightButton_textview')
	setting_logout = (By.ID,'com.tal.kaoyan:id/setting_logout_text')

	
	
	def login_action(self,username,password):
		self.check_updateBtn()
		self.check_skipBtnm()

		logging.info('====login_action====')
		logging.info('username is: %s' %username)
		self.driver.find_element(*self.username_type).send_keys(username)
		logging.info('password is： %s' %password)
		self.driver.find_element(*self.password_type).send_keys(password)
		logging.info('click loginBtn')
		self.driver.find_element(*self.loginBtn).click()
		logging.info('login finished!!!')

	def check_account_alert(self):
		logging.info('===============')
		try:
			element = self.driver.find_element(*self.tip_commit)
		except NoSuchElementException:
			logging.info('No alert....')
			pass
		else:
			logging.info('Close alert....')
			element.click()

	def check_agree_alert(self):
		logging.info('=====check_agree_alert=======')
		self.check_account_alert()
		try:
			element = self.driver.find_element(*self.tv_agree)
		except NoSuchElementException:
			logging.info('No tv_agree_alert')
			pass
		finally:
			logging.info('click tv_agree_alert')
			element.click()

	def check_login_staus(self):
		logging.info('==========check_loginStatus===========')
		self.check_marked_ad()
		# self.check_account_alert()
		try:
			self.driver.find_element(*self.button_mysefl).click()
			self.driver.find_element(*self.button_mysefl).click()
			
			self.driver.find_element(*self.username)
			
		except NoSuchElementException:
			logging.error('====login_error====')
			self.get_screen_shot('login_error')
			return False
		else:
			logging.info('login success!!!')
			self.logout_action()
			return True

	def logout_action(self):
		logging.info('===logout_action=====')
		self.driver.find_element(*self.RightButton).click()
		self.driver.find_element(*self.setting_logout).click()
		self.driver.find_element(*self.tip_commit).click()

		
if __name__ == '__main__':
	driver = appium_desired()
	l = LoginView(driver)
	l.login_action('18721102132','aaa111222')
	l.check_agree_alert()
	l.check_login_staus()
