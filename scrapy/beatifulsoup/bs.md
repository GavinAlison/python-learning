# bs4的BeatifulSoup 插件用法说明

参考： 
1. https://cuiqingcai.com/1319.html
2. https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html


## 1. 对html字符进行解析
```
from bs import BeatifulSoup as bs
html = '''
<html>
<head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
</body>
</html>
'''
soup = bs(html, 'lxml')
```

## 2. 解析之后的类型
-   Tag
-   NavigableString
-   BeautifulSoup
-   Comment

Tag
```
print(soup.title)
# 可以取tag.name和其他属性attrs
print(soup.a.name)
# 取出所有属性
print(soup.a.attrs)
# 取出单个属性
print(soup.a['class'])
```

NavigableString
```
print(soup.p.string)
```

BeautifulSoup
```
type(soup.name)
```

Comment
```
soup.a.string
```
## 