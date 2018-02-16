# -*- coding: UTF-8 -*-
import requests
import re
import json

def download(url,data=None):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
    }
    try:
        return requests.get(url,params=data,headers=headers)
    except Exception as e:
        print e

def get_song(song_id):

    #百度音乐接口
    url='http://tingapi.ting.baidu.com/v1/restserver/ting?method=baidu.ting.song.play&format=jsonp&callback=jQuery17205500581185420972_1513324047403&songid={}&_=1513324048127'.format(song_id)
    data=download(url).text
    data=re.findall(r'\((.*)\)',data)[0]
    data=json.loads(data)
    return data
    # title=data['songinfo']['title']
    # data=data.get('bitrate',None)

def get_music_ids_by_name(song_name):
    api='http://music.baidu.com/search'
    data={
        'key':song_name
    }
    response=download(api,data=data)
    response.encoding='utf-8'
    html=response.text
    ul=re.findall(r'<ul.*</ul>',html,re.S)[0]
    # print ul
    sids=re.findall(r'sid&quot;:(\d+)',ul,re.S)
    # print len(sids)
    return sids

def get_music_info_by_name(name):
    sids=get_music_ids_by_name(name)
    music_info=[]
    for sid in sids:
        # print sid
        temp=get_song(sid)
        music_info.append(temp)
    return music_info

if __name__=='__main__':
    music_info=get_music_info_by_name('刘德华')
    print music_info











