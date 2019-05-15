from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(executable_path='D:\workspace\python-learning\scrapy\geckodriver.exe')
url = 'https://www.python.org'
driver.get(url)
assert 'Python' in driver.title
el = driver.find_element_by_name('q')
el.clear()
el.send_keys('pycon')
el.send_keys(Keys.RETURN)
assert 'No results found.' not in driver.page_source
driver.close()
