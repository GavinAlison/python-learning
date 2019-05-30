## 学习IP相关知识
1.  学习什么是IP，为什么会出现IP被封，如何应对IP被封的问题。

2.  抓取西刺代理，并构建自己的代理池。

3.  西刺直通点：https://www.xicidaili.com/ 。


### 1. 为什么会出现IP被封，如何应对IP被封的问题。
网站为了防止被爬取，会有反爬机制，对于同一个IP地址的大量同类型的访问，会封锁IP，过一段时间后，才能继续访问    
现有的反扒策略：
```
0. 检测浏览器header， User-Agent
1. ip 封禁
2. 图片验证码
3. 滑块
4. JS轨迹
5. 证书加密
6. AI识别
```

### 2. 如何应对IP被封

```
1. 建立代理IP, 轮换访问
2. 设置访问时间间隔
3. 可动态设置user agent
4. 禁用cookies
5. 设置延迟下载
6. 使用Google Cache
7. 使用IP地址池（代理IP、VPN等）
8. 使用Crawlera
```
参考： https://desmonday.github.io/2019/03/06/python%E7%88%AC%E8%99%AB%E5%AD%A6%E4%B9%A0-day6-IP%E4%BB%A3%E7%90%86/

### 3. 获取代理IP地址
网站： https://www.xicidaili.com/



参考资料：
>1. https://blog.csdn.net/weixin_43720396/article/details/88218204
>2. https://desmonday.github.io/2019/03/06/python%E7%88%AC%E8%99%AB%E5%AD%A6%E4%B9%A0-day6-IP%E4%BB%A3%E7%90%86/