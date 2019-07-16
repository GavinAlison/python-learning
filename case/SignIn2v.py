import time

from selenium import webdriver


def run():
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36'
    # }
    #
    # res = requests.get(url, headers=headers)
    # #  没有login ，先login在领取
    # tree = etree.HTML(res.text)

    browser = webdriver.Chrome()
    signin_url = 'https://www.v2ex.com/signin'
    browser.get(signin_url)
    time.sleep(3)

    # open chrome tab
    # browser.maximize_window()

    # time.sleep(5)
    # 找到邮箱账号登录框对应的iframe,由于网页中iframe的id是动态的，所以不能用id寻找
    username = browser.find_elements_by_xpath('//div[@id="Wrapper"]//form/table/tbody/tr/td[@align="left"]/input')[0]
    password = browser.find_elements_by_xpath('//div[@id="Wrapper"]//form/table/tbody/tr[2]/td[@align="left"]/input')[0]
    verified_code = browser.find_elements_by_xpath('//div[@id="Wrapper"]//form/table/tbody/tr[3]/td[@align="left"]/div')[0]
    submit = browser.find_elements_by_xpath('//input[@type="submit"]')[0]
    username.clear()
    username.send_keys('GavinAlison')
    password.clear()
    password.send_keys('huang@yong')
    verified_code.send_keys('PZCD')

    # submit.click()
    time.sleep(10)
    


if __name__ == '__main__':
    try:
        run()
    except BaseException as e:
        print(e)
