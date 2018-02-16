# -*- coding: UTF-8 -*-
import urllib2

from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from pdfminer.layout import LAParams
from pdfminer.converter import PDFPageAggregator
#获取文档对象，你把XXXX.pdf换成你自己的文件名即可。
fp=open("XXXX.PDF","rb")
#创建一个与文档相关联的解释器
parser=PDFParser(fp)
#PDF文档对象
doc=PDFDocument(parser)
#链接解释器和文档对象
parser.set_document(doc)
#doc.set_paeser(parser)
#初始化文档
#doc.initialize("")
#创建PDF资源管理器
resource=PDFResourceManager()
#参数分析器
laparam=LAParams()
#创建一个聚合器
device=PDFPageAggregator(resource,laparams=laparam)
#创建PDF页面解释器
interpreter=PDFPageInterpreter(resource,device)
#使用文档对象得到页面集合
for page in PDFPage.create_pages(doc):
  #使用页面解释器来读取
  interpreter.process_page(page)
  #使用聚合器来获取内容
  layout=device.get_result()
  for out in layout:
    if hasattr(out, "get_text"):
      print out.get_text()
















