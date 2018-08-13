import unittest
import logging
import time
from BSTestRunner import BSTestRunner

test_dir = '../test_case'
report_dir = '../reports'

discover = unittest.defaultTestLoader.discover(test_dir,pattern='test_login.py')

now = time.strftime("%Y-%m-%d %H_%M_%S")
report_name = report_dir + '/' + 'test_report.html'

with open(report_name, 'wb') as f:
    runner = BSTestRunner(stream=f, title="Kyb Test Report", description="kyb Andriod app Test Report")
    logging.info("start run testcase...")
    runner.run(discover)