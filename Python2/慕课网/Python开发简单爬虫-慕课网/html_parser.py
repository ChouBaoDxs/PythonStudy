# -*- coding: UTF-8 -*-
import re
import urlparse

from bs4 import BeautifulSoup

class HtmlParser(object):
    def parse(self, page_url, html_cont):
        # print ('if')
        if page_url is None or html_cont is None:
            return

        # print ('soup')
        soup=BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')

        new_urls=self._get_new_urls(page_url,soup)
        # print ('urls:',new_urls)
        # print ('urls')
        new_data=self._get_new_data(page_url,soup)
        # print ('data:',new_data)
        # print ('data:')
        return new_urls,new_data

    def _get_new_urls(self, page_url, soup):
        new_urls=set()
        #/item/%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%A8%8B%E5%BA%8F%E8%AE%BE%E8%AE%A1%E8%AF%AD%E8%A8%80
        links=soup.find_all('a',href=re.compile(r"/item/"))
        for link in links:
            new_url=link['href']
            new_full_url=urlparse.urljoin(page_url,new_url)    #拼接url
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, page_url, soup):
        res_data={}
        #url
        res_data['url']=page_url

        #<dd class="lemmaWgt-lemmaTitle-title"> <h1>***</h1></dd>
        title_node=soup.find('dd',class_="lemmaWgt-lemmaTitle-title").find("h1")
        res_data['title']=title_node.get_text()

        #<div class=“lemma-summary”>***<div>
        summary_node=soup.find('div',class_="lemma-summary")
        res_data['summary']=summary_node.get_text()

        return res_data
