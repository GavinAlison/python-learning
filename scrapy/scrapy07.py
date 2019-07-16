#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/16 21:36
# @Author  : alison
# @File    : scrapy07.py


from selenium import webdriver
import time
from lxml import etree


class scrapy07(object):
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36'}
        self.login_url = 'https://auth.dxy.cn/accounts/login?service=http://www.dxy.cn/bbs/index.html'

    def get_login(self):
        browser = webdriver.Chrome()
        browser.get(self.login_url)
        time.sleep(3)
        # 切换登录页面
        el = browser.find_element_by_id('j_loginTab1')
        # el2 = browser.find_element_by_name('loginType')
        # el3 = browser.find_element_by_class_name('login-wp')
        # el4 = browser.find_element_by_tag_name('div')
        el5 = browser.find_element_by_xpath('//div[@id="j_loginTab1"]')
        # div_els = browser.find_elements_by_tag_name('div')
        browser.execute_script('document.querySelector("#j_loginTab1").style.display="none"')
        time.sleep(1)
        browser.execute_script('document.querySelector("#j_loginTab2").style.display="block"')
        time.sleep(1)
        # login
        username = browser.find_element_by_name('username')
        username.clear()
        username.send_keys('username')
        password = browser.find_element_by_name('password')
        password.clear()
        password.send_keys('password')
        browser.find_element_by_xpath('//div[@class="form__button"]/button').click()
        #  先睡会，然后登录之后再次请求就可以不用登录了
        time.sleep(10)

        #  获取cookies
        cookies = browser.get_cookies()
        # print(cookies)
        # print('------------------')
        # for i in cookies:
        #     print(i)
        cookie_dict = {i['name']: i['value'] for i in cookies}
        # print(cookie_dict)

        # 浏览指定论坛
        browser.get('http://www.dxy.cn/bbs/thread/626626#626626')
        html = browser.page_source
        tree = etree.HTML(html)
        names = tree.xpath('//div[@class="auth"]/a/text()')
        create_times = tree.xpath('//div[@class="post-info"]/span/text()')
        del create_times[1]
        del create_times[1]
        contents = tree.xpath('//td[@class="postbody"]')
        result = []
        with open('scrapy_content.csv', 'w+', encoding='utf-8') as f:
            for i in range(0, len(names)):
                if names[i].strip() == 'dxy_3n8hnhf2':
                    #     自己就回复一下子
                    #  这块有点击验证，先打卡再说
                    break
                dictTmp = {'name': names[i].strip(), 'create_time': create_times[i].strip(),
                           'content': contents[i].xpath('string(.)').strip()}
                print(dictTmp)
                print('*' * 80 + "\n")
                f.writelines([names[i].strip(), create_times[i].strip(), contents[i].xpath('string(.)').strip()])
                f.write('\n')
                f.writelines('*' * 80)
                f.write('\n')
        # return browser


if __name__ == '__main__':
    sprider = scrapy07()
    br = sprider.get_login()
    # sprider.
