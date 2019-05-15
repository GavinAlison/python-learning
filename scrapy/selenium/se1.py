from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

driver = webdriver.Remote(
	command_executor='http://PC-Huangyong.posbao.net:4444',
	desired_capabilities=DesiredCapabilities.CHROME)
driver = webdriver.Remote(
	command_executor='http://PC-Huangyong.posbao.net:4444',
	desired_capabilities=DesiredCapabilities.FIREFOX)
driver = webdriver.Remote(
   command_executor=' http://PC-Huangyong.posbao.net:4444',
   desired_capabilities=DesiredCapabilities.HTMLUNITWITHJS)


driver = webdriver.Remote(
   command_executor='http://PC-Huangyong.posbao.net:4444',
   desired_capabilities={'browserName': 'htmlunit',
                         'version': '2',
                        'javascriptEnabled': True})
driver.get("https://www.google.com")
driver.close()