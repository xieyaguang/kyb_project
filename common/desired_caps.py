import sys
path='F:/project/kyb_project'
sys.path.append(path)
from appium import webdriver
import logging
import logging.config
import os
import yaml

CON_LOG = '../config/log.conf'
logging.config.fileConfig(CON_LOG)
logging = logging.getLogger()


def appium_desired():
	with open('../config/kyb_caps.yaml','r',encoding='utf-8') as file:
		data = yaml.load(file)
		# print(data)

	desired_caps = {}
	desired_caps['platformName'] = data['platformName']
	desired_caps['platformVerion'] = data['platformVerion']
	desired_caps['deviceName'] = data['deviceName']

	base_dir = os.path.dirname(os.path.dirname(__file__))
	app_path = os.path.join(base_dir,'app',data['appname'])
	# print(app_path)

	desired_caps['app'] = app_path
	desired_caps['noReset'] = data['noReset']
	desired_caps['unicodeKeyboard'] = data['unicodeKeyboard']
	desired_caps['resetKeyboard'] = data['resetKeyboard']
	desired_caps['appPackage'] = data['appPackage']
	desired_caps['appPackage'] = data['appPackage']

	logging.info('start  instll app ....')

	driver = webdriver.Remote('http://'+str(data['ip'])+':'+str(data['port'])+'/wd/hub', desired_caps)

	
	
	return driver

if __name__ == '__main__':
	appium_desired()

	
	# with open('../config/kyb_caps.yaml','r',encoding='utf-8') as file:
	# 	data = yaml.load(file)
	# base_dir = os.path.dirname(os.path.dirname(__file__))
	# app_path = os.path.join(base_dir,'app',data['appname'])
	# print(base_dir)
	# print(app_path)
