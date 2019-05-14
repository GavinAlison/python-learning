# from selenium import webdriver


# browser = webdriver.Chrome()
# browser.get('https://www.baidu.com')

# 结果
#![selenium01](resource/selenium01.jpg)



import time
from selenium import webdriver

browser = webdriver.Chrome()
url = 'http://mail.163.com'
browser.get(url)
time.sleep(3)

# open chrome tab
# browser.maximize_window()

time.sleep(5)
#找到邮箱账号登录框对应的iframe,由于网页中iframe的id是动态的，所以不能用id寻找
browser.switch_to.frame(0)
email = browser.find_element_by_name('email')
email.clear()
email.send_keys('username@163.com')
password = browser.find_element_by_name('password')
password.clear()
password.send_keys('password')
login_em = browser.find_element_by_id('dologin')
login_em.click()
time.sleep(10)

