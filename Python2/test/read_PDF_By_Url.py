# -*- coding: UTF-8 -*-
# python爬虫：读取PDF
#
# 下面的代码可以实现用python读取PDF，包括读取本地和网络上的PDF。
#

# -*- encoding:utf-8 -*-
from urllib2 import urlopen
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO

def convert_pdf_to_txt(fp):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()
    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)

    fp.close()
    device.close()
    textstr = retstr.getvalue()
    retstr.close()
    return textstr

url='http://www.cninfo.com.cn/finalpage/2017-10-12/1204030937.PDF'
fp = StringIO(urlopen(url).read())  # for url

# path='chapter1.pdf'
# fp = file(path, 'rb')               # for path

text=convert_pdf_to_txt(fp)
text=text.replace('\n','')
print len(text)
try:
    text=text[0:5000]   #初步分析的字符串
except:
    pass
print text

















