


from lxml import etree
text  = '''
<div>
    <ul>
         <li class="item-0"><a href="https://ask.hellobi.com/link1.html">first item</a></li>
         <li class="item-1"><a href="https://ask.hellobi.com/link2.html">second item</a></li>
         <li class="item-inactive"><a href="https://ask.hellobi.com/link3.html">third item</a></li>
         <li class="item-1"><a href="https://ask.hellobi.com/link4.html">fourth item</a></li>
         <li class="item-0"><a href="https://ask.hellobi.com/link5.html">fifth item</a>
     </ul>
 </div>
'''

html = etree.HTML(text)
# result =etree.tostring(html)
# print(result.decode('utf-8'))
print(type(html))
lis = html.xpath('//li')
print(dir(lis))


#  xpath :  / 是获取直接子节点，// 是获取子孙节点。
#  /@class:  获取class 属性，
#  ..  : 获取父路径
#  parent:: 来获取父节点
#  属性匹配，   /li[@class]
#  文本获取      //li/text()   获取节点内部文本
#  属性获取     @ 符号
#  属性多值匹配    contains
# html.xpath('//li[contains(@class, "li")]/a/text()')
#  多属性匹配      使用运算符 and 来连接
# html.xpath('//li[contains(@class, "li") and @name="item"]/a/text()')
# 按序选择   利用中括号传入索引的方法获取特定次序的节点
# html.xpath('//li[1]/a/text()')
# html.xpath('//li[last()]/a/text()')
# html.xpath('//li[position()<3]/a/text()')
# html.xpath('//li[last()-2]/a/text()')
# 节点轴选择
# result = html.xpath('//li[1]/ancestor::*')
# result = html.xpath('//li[1]/ancestor::div')
# result = html.xpath('//li[1]/attribute::*')
# result = html.xpath('//li[1]/child::a[@href="https://ask.hellobi.com/link1.html"]')
# result = html.xpath('//li[1]/descendant::span')
# result = html.xpath('//li[1]/following::*[2]')
# result = html.xpath('//li[1]/following-sibling::*')

