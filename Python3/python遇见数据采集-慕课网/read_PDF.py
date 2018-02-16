# -*- coding: UTF-8 -*-
from urllib.request import urlopen

from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams
from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice

# 读取网页打开的pdf
# from urllib.request import urlopen
# 获取文档对象
# fp=urlopen("http://www.cninfo.com.cn/finalpage/2017-09-26/1204001374.PDF")
# 后面步骤都差不多

# 获取文档对象
fp = open("财经信息源整理.pdf", "rb")
'''
w   以写方式打开
a   以追加模式打开(从EOF开始，必要时创建新文件)
r+  以读写模式打开
w+  以读写模式打开，参见w
a+  以读写模式打开，参见a
rb  以二进制读模式打开
wb  以二进制写模式打开，参见w
ab  以二进制追加模式打开，参见a
rb+ 以二进制读写模式打开，参见r+
wb+ 以二进制读写模式打开，参见w+
ab+ 以二进制读写模式打开，参见a+
'''
# 创建一个与文档关联的解释器
parser = PDFParser(fp)

# PDF文档的对象
doc = PDFDocument()

# 连接解释器和文档对象
parser.set_document(doc)
doc.set_parser(parser)

# 初始化文档
doc.initialize("")  # 比如文档打开密码

# 创建PDF资源管理器
resource = PDFResourceManager()

# 创建一个参数分析器
laparam = LAParams()

# 创建一个聚合器
device = PDFPageAggregator(resource, laparams=laparam)

# 创建一个页面解释器
interpreter = PDFPageInterpreter(resource, device)

# 使用文档对象得到页面的集合
for page in doc.get_pages():
    # 使用页面解释器来读取
    interpreter.process_page(page)

    # 使用聚合器来获得内容
    layout = device.get_result()

    for out in layout:
        if hasattr(out, "get_text"):  # 判断读取到的东西是否有get_text属性
            print(out.get_text())
