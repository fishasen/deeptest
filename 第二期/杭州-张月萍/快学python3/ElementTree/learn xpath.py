# -*- coding: utf-8 -*-
# __author__ = 'Carina'


try:
    # 若想加快速度，可以使用C语言编译的API xml.etree.cElementTree
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET


if __name__ == "__main__":
    print("Element Tree XPath特性支持示例")

    # 加载XML文件
    tree = ET.parse('D:\deeptest\第二期\杭州-张月萍\快学python3\data_demo.xml')

    # 获取根节点，并打印节点文本：data
    root = tree.getroot()

    # 选择当前节点, 返回的是当前节点对象列表
    print("选择当前节点")
    data = root.findall(".")
    for d in data:
        print(d.tag)

    # 选择所有country节点
    print("选择所有country节点方法一")
    countrys = root.findall(".//country")
    for country in countrys:
        print(country.tag, " ", country.attrib["name"])

    print("选择所有country节点方法二")
    countrys = root.findall("country")
    for country in countrys:
        print(country.tag, " ", country.attrib["name"])

    print("选择name属性为Panama的country节点")
    countrys = root.findall(".//*[@name='Panama']")
    for country in countrys:
        print(country.tag, " ", country.attrib["name"])

    # name属性为Panama的country下的year节点
    print("name属性为Panama的country下的year节点")
    years = root.findall(".//country[@name='Panama']/year")
    for year in years:
        print(year.text)

    # 通过索引来选择country节点，选择第一个country节点
    # 注意索引从1开始
    print("通过索引来选择country节点，选择第一个country节点")
    country = root.findall(".//country[1]")
    for c in country:
        print(c.tag, " ", c.attrib["name"])

    # 通过子节点的文本内容来选择节点
    # 选择子节点gdppc且其文本为59900 的country节点
    # 请注意这返回的是gdppc的父节点
    print("通过子节点的文本内容来选择节点")
    gdppc = root.findall(".//*[gdppc='59900']")
    for gd in gdppc:
        print(gd.tag)
