# -*- coding: UTF-8 -*-
# import bs4  #没有安装beautifulsoup4时会报错，只需要alt+回车，直接安装就好
# print bs4
from bs4 import BeautifulSoup
import re

html_doc = """<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=Edge,chrome=1">
        <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=0">
        <title>OLED概念股有哪些？OLED概念龙头股及OLED上市公司最新消息_云财经</title>
        <meta name="keywords" content="OLED,OLED概念股有哪些,OLED概念股龙头股,OLED概念上市公司,真正的OLED概念股,OLED概念最新消息,OLED 曲屏手机 新型显示 oled">
        <meta name="description" content="想知道OLED概念股、OLED龙头股及相关上市公司有哪些吗？OLED概念一览提供最全最新的OLED概念相关新闻，以及OLED概念的市场关注度走势，
可以帮你从众多OLED概念上市公司中挖掘出哪只才是OLED概念的龙头股以及预测OLED概念股未来走势">
        <meta http-equiv="Cache-Control" content="no-transform"/> 
        <meta http-equiv="Cache-Control" content="no-siteapp"/>
        <link rel="stylesheet" href="http://aliyun.yuncaijing.com/res/pc/assets/css/xui_v2.css?v=201701172359">
        <link rel="shortcut icon" href="http://aliyun.yuncaijing.com/res/pc/assets/img/favicon.ico?v=201701172359" type="image/x-icon"/>
        <link rel="icon" href="http://aliyun.yuncaijing.com/res/pc/assets/img/favicon.ico?v=201701172359" type="image/x-icon"/>
        <link rel="bookmark" href="http://aliyun.yuncaijing.com/res/pc/assets/img/favicon.ico?v=201701172359" type="image/x-icon"/>
        <script type="text/javascript" src="//s.union.360.cn/168612.js" async defer></script>
        
    <link rel="stylesheet" href="http://aliyun.yuncaijing.com/res/pc/assets/css/view.css?v=201701172359">

    </head>

    <body>
        <div id="guide-mask">
    <div class="step step-1">
        <div class="w-frame"></div>
        <div class="go-on" data-step="1">
            <div class="next"></div>
            <div class="esc"></div>
            <img src="http://aliyun.yuncaijing.com/res/pc/assets/img/guide/step_1.png?v=201701172359" alt="第一步">
        </div>
    </div>
    <div class="step step-2">
        <div class="w-frame"></div>
        <div class="go-on" data-step="2">
            <div class="next"></div>
            <div class="esc"></div>
            <img src="http://aliyun.yuncaijing.com/res/pc/assets/img/guide/step_2.png?v=201701172359" alt="第二步">
        </div>
    </div>
    <div class="step step-3">
        <div class="w-frame"></div>
        <div class="go-on" data-step="3">
            <div class="next"></div>
            <div class="esc"></div>
            <img src="http://aliyun.yuncaijing.com/res/pc/assets/img/guide/step_3.png?v=201701172359" alt="第三步">
        </div>
    </div>
    <div class="step step-4">
        <div class="w-frame"></div>
        <div class="go-on" data-step="4">
            <div class="next"></div>
            <div class="esc"></div>
            <img src="http://aliyun.yuncaijing.com/res/pc/assets/img/guide/step_4.png?v=201701172359" alt="第四步">
        </div>
    </div>
    <div class="step step-5">
        <div class="w-frame"></div>
        <div class="go-on" data-step="5">
            <div class="esc"></div>
            <img src="http://aliyun.yuncaijing.com/res/pc/assets/img/guide/step_5.png?v=201701172359" alt="第五步">
        </div>
    </div>
</div>
<aside id="nav-sidebar">
    <nav class="nav-main">
        <ul class="list-unstyled">
            <li >
                <a href="/" title="首页">
                    <i class="iconYCJ icon-home-ycj"></i> 首页
                </a>
            </li>
            <li >
                <a href="/mystock/index.html" rel="nofollow" title="自选股">
                    <i class="iconYCJ icon-mystock-ycj"></i> 我的自选
                </a>
            </li>
            <li >
                <a href="/topnews/main.html" title="独家报道">
                    <i class="iconYCJ icon-earth-ycj"></i> 独家报道
                </a>
            </li>
            <li >
                <a href="/insider/main.html" title="内参快讯">
                    <i class="iconYCJ icon-news-live-ycj"></i> 内参快讯
                </a>
            </li>
            <li >
                <a href="/scheme/main.html" title="科学炒股" style="position: relative;">
                    <i class="iconYCJ icon-atom-ycj"></i> 科学炒股
                    <span style="font-size: 12px;background-color:#d22222;color:white;padding:0 3px;margin-left:6px;display:inline-block;height:16px;line-height: 15px;position: absolute;top:50%;transform: translateY(-50%);">New</span>
                </a>
            </li>
            <li class="dropdown-submenu ">
                <a href="javascript:;" title="更多功能">
                    <i class="iconYCJ icon-hot-ycj"></i> 更多功能
                </a>
                <ul class="dropdown-menu">
                    <li class="dropdown-submenu-plus">
                        <a href="javascript:;" title="市场热点"> 市场热点
                        </a>
                        <ul class="dropdown-menu-plus">
                            <li>
                                <a href="/markethot/hot_news.html" title="热门消息题材">热门消息题材</a>
                            </li>
                            <li>
                                <a href="/markethot/rised.html" title="涨停题材">涨停题材</a>
                            </li>
                            <li>
                                <a href="/markethot/latest.html" title="最新消息题材">最新消息题材</a>
                            </li>
                            <li>
                                <a href="/markethot/discovery.html" title="龙头挖掘机">龙头挖掘机</a>
                            </li>
                            <li>
                                <a href="/markethot/bk.html" title="地域板块涨幅榜">地域板块涨幅榜</a>
                            </li>
                            <li>
                                <a href="/markethot/hy.html" title="行业板块涨幅榜">行业板块涨幅榜</a>
                            </li>
                        </ul>
                    </li>
                    <li >
                        <a href="/data/main.html" title="数据中心"> 数据中心
                        </a>
                    </li>
                    <li >
                        <a href="/quotes/ratio.html" title="行情中心"> 涨幅排行
                        </a>
                    </li>
                </ul>
            </li>
            <li class="dropdown-submenu ">
                    <a href="javascript:;" title="增值服务">
                        <i class="iconYCJ icon-service-ycj"></i> 增值服务
                    </a>
                    <ul class="dropdown-menu horizontal">
                        <div class="part-left" style="float: left;">
                            <li>
                                <a href="/apps/navigator.html" title="趋势领航者">趋势领航者</a>
                            </li>
                            <li>
                                <a href="/apps/hdd/observe.html" title="高级席位数据">高级席位数据</a>
                            </li>
                            <li>
                                <a href="/apps/lowrisk.html" title="低风险稳赢模型">低风险稳赢模型</a>
                            </li>
                            <li class="siderbar-ybds">
                                <a href="/apps/ybds.html" title="研报大师">研报大师</a>
                            </li>
                            <li>
                                <a href="/apps/vip.html" title="VIP参考">VIP参考</a>
                            </li>
                        </div>
                        <div class="part-right">
                            <li>
                                <a href="/apps/nline.html" title="N形反转大师">N形反转大师<span style="font-size: 12px;background-color: #d22222;color:#fff;padding:0 6px;margin-left: 6px;display: inline-block;height:16px;line-height: 15px">New</span></a>
                            </li>
                            <li>
                                <a href="/apps/monster.html" title="早盘捉妖">早盘捉妖</a>
                            </li>
                            <li>
                                <a href="/apps/crline.html" title="搓揉优选大师">搓揉优选大师</a>
                            </li>
                            <li>
                                <a href="/quote/sz000877_hmoney.html" title="主力多空">主力多空</a>
                            </li>
                            <li>
                                <a href="/apps/kpgs.html" title="看盘高手">看盘高手</a>
                            </li>
                        </div>
                    </ul>
                </li>
                <li >
            <a href="/mall/main.html" title="购买">
                <i class="iconYCJ icon-buy-ycj"></i> 购买
            </a>
            </li>        </ul>
    </nav>
    <nav class="nav-footer">
        <ul class="list-unstyled">
            <li >
                <a href="/plans/weixinrobot.html" title="微信机器人" target="_blank">
                    <i class="iconYCJ icon-wechatlive-ycj"></i> 微信机器人
                </a>
            </li>
            <li >
                <a href="/app.html" title="下载APP" target="_blank">
                    <i class="iconYCJ icon-appdown-ycj"></i> 下载APP
                </a>
            </li>
            <li >
                <a href="/help/" title="帮助中心" target="_blank">
                    <i class="iconYCJ icon-help-ycj"></i> 帮助中心
                </a>
            </li>
            <li >
                <a href="/about.html" title="关于云财经" target="_blank">
                    <i class="iconYCJ icon-about-ycj"></i> 关于云财经
                </a>
            </li>
        </ul>
    </nav>
</aside>
<ul class="hidden" data-shortcut>
    <li data-shortcut-wechat="http://aliyun.yuncaijing.com/upload/2017-08-24/599e2f5dcbc8b.png"></li>
    <li data-shortcut-qq="//shang.qq.com/wpa/qunwpa?idkey=6c7d4c29dd17cb492e86ceb4c46b93433367fabe5b511bbeac7af2bafcf45a39"></li>
</ul>
        <header id="com-header">

    <div class="text-logo">
        <img src="http://aliyun.yuncaijing.com/res/pc/assets/img/text-white-logo.png?v=201701172359" alt="云财经">
    </div>
    <div class="breadcrumb-wrap">
        <ul class="breadcrumb">
            <li>
                <a href="/" title="首页">首页</a>
            </li>

                        <li class="breadcrumb-divider">
                <i class="icon icon-chevron-right"></i>
            </li>
            <li>
                                <a href="/story/details/id_25.html">OLED</a>
                            </li>

                                                
                    </ul>
    </div>

    <div class="gate">
        <div class="com-search">
            <div class="search-content">
                <aside class="search-input form-input-group">
                    <div class="glyphic">
                        <span>搜索</span>
                    </div>
                    <div class="placeholder-input">
                        <i class="placeholder-text">股票/概念/消息/席位</i>
                        <input class="form-control" type="text" autocomplete="off">
                    </div>
                </aside>
                <div class="search-list hidden"></div>
            </div>
            <button class="search-btn btn btn-primary" type="button">
                <i class="icon icon-search"></i>
            </button>
        </div>
        <div class="btn btn-primary login hidden" onclick="window.location.href='/login.html?state=2'">
            注册
        </div>
        <div class="btn btn-primary login hidden"
             data-toggle="modal"
             data-target="#login-modal">
            登录
        </div>
        <div class="notify hidden">
            <a class="btn btn-primary" href="/member/center/message.html">
                <i class="icon icon-notification"></i>
                <span class="badge"></span>
            </a>
        </div>
        <div class="user hidden">
            <button class="btn btn-primary" type="button">
                <i class="icon icon-user"></i>
            </button>
            <ul class="dropdown-menu right">
                <li>
                    <a href="/member/center/" title="用户中心">
                        <i class="icon icon-user"></i>
                        用户中心
                    </a>
                </li>
                <li>
                    <a id="logout" href="javascript:;" title="退出登录">
                        <i class="icon icon-shutdown"></i>
                        退出登录
                    </a>
                </li>
            </ul>
        </div>
    </div>
    <div class="ads">
                        <a href="http://www.yuncaijing.com/news/id_9978723.html" target="_blank">
                    <img src="http://aliyun.yuncaijing.com/upload/2017-11-16/5a0d685aca771.jpg">
                </a>
                        </div></header>


        
    <section id="container">
        <nav class="page-title">
            <img src="http://aliyun.yuncaijing.com/res/pc/assets/img/page-logo/news-concept.png?v=201701172359" alt="概念新闻Logo" title="概念新闻Logo">
            <h1 data-ct="OLED概念股">
                OLED概念
                <span data-module="layer">
                    <span data-content>OLED是有机发光二极管的简称，它与LED的发光原理是一样的，只不过材料上LED是金属，而OLED是有机物材料，在电子产品的应用上亮度要比LED液晶屏高，更薄，可视角度更大，并且具备省电的作用。在市场的作用下成为了LED屏的替代品。OLED技术在欧美最先推出，但规模化推行主要还是在中日韩等东亚国家，在中国OLED产业链具备一定的技术，但依旧不完善，尤其是上游竞争力比较弱势，主要研发系统及其技术均在日韩、欧美国家手中。目前OLED还是处于产业化初期，涉足该产业的产品主要是小尺寸手持设备，比如手机。随着手机概念的火爆，OLED概念也随之火爆。</span>概念简介
                </span>
            </h1> 半导体照明产业迈向万亿规模        </nav>
        <div class="container-left">
            <article>
                <h1>
                                            <a href="/news/id_9967797.html"
                           data-remote="/news/modal/9967797"
                           data-toggle="modal"
                           data-target="#news-modal">
                            最新进展：
                            半导体照明产业迈向万亿规模                        </a>
                        <span>11-13 07:00</span>                </h1>
                <p>
                      不久前印发的《半导体照明产业“十三五”发展规划》提出，2020年半导体照明产业整体产值达10000亿元，我国半导体照明关键技术不断突破，产品结构持续优化。通过应用领域的不断拓宽和市场环境持续规范，为半导体照明产业迈向强国奠定基础。这为该产业的明天指出了一条清晰的发展道路。（经参）                </p>
                <div class="stock-list">
                                    </div>
            </article>
            <article>
                <div id="hchart">
                    <div class="loadedpage">
                        <div class="loading-page"></div>
                    </div>
                </div>
            </article>
            <article>
                <table class="table table-ycj table-hover">
                    <thead>
                        <tr>
                            <th>OLED相关新闻</th>
                            <th>时间</th>
                            <th>消息来源</th>
                            <th>新闻热度</th>
                        </tr>
                    </thead>
                    <tbody>
                                                    <tr>
                                    <td><a href="/news/id_9976898.html" data-remote="/news/modal/9976898" data-toggle="modal" title="维信诺携柔性AMOLED技术和产品亮相高交会" data-target="#news-modal">维信诺携柔性AMOLED技术和产品亮相高交会                                </a>
                                    </td>
                                    <td>11-16 19:48                                    </td>
                                    <td>同花顺</td>
                                    <td class="star-1
                                                                ">
                                        <span class="icon icon-star "></span><span class="icon icon-star"></span><span class="icon icon-star"></span><span class="icon icon-star "></span><span class="icon icon-star"></span>
                                    </td>
                                </tr><tr>
                                    <td><a href="/news/id_9972396.html" data-remote="/news/modal/9972396" data-toggle="modal" title="海信电器：129亿日元收购东芝电视业务 意在OLED？" data-target="#news-modal">海信电器：129亿日元收购东芝电视业务 意在OLED？                                </a>
                                    </td>
                                    <td>11-14 22:17                                    </td>
                                    <td>同花顺</td>
                                    <td class="star-3
                                                                ">
                                        <span class="icon icon-star "></span><span class="icon icon-star"></span><span class="icon icon-star"></span><span class="icon icon-star "></span><span class="icon icon-star"></span>
                                    </td>
                                </tr><tr>
                                    <td><a href="/news/id_9972394.html" data-remote="/news/modal/9972394" data-toggle="modal" title="精测电子拟投6000万参股合肥视涯 间接介入20亿OLED微显示器项目" data-target="#news-modal">精测电子拟投6000万参股合肥视涯 间接介入20亿OLED微显示器项目                                </a>
                                    </td>
                                    <td>11-14 22:16                                    </td>
                                    <td>同花顺</td>
                                    <td class="star-1
                                                                ">
                                        <span class="icon icon-star "></span><span class="icon icon-star"></span><span class="icon icon-star"></span><span class="icon icon-star "></span><span class="icon icon-star"></span>
                                    </td>
                                </tr><tr>
                                    <td><a href="/news/id_9972160.html" data-remote="/news/modal/9972160" data-toggle="modal" title="方宗豹：面向新型显示的微纳光学制造技术" data-target="#news-modal">方宗豹：面向新型显示的微纳光学制造技术                                </a>
                                    </td>
                                    <td>11-14 19:33                                    </td>
                                    <td>同花顺</td>
                                    <td class="star-1
                                                                ">
                                        <span class="icon icon-star "></span><span class="icon icon-star"></span><span class="icon icon-star"></span><span class="icon icon-star "></span><span class="icon icon-star"></span>
                                    </td>
                                </tr><tr>
                                    <td><a href="/news/id_9970739.html" data-remote="/news/modal/9970739" data-toggle="modal" title="OLED明年将成高端电视市场主流" data-target="#news-modal">OLED明年将成高端电视市场主流                                </a>
                                    </td>
                                    <td>11-14 09:52                                    </td>
                                    <td>同花顺</td>
                                    <td class="star-1
                                                                ">
                                        <span class="icon icon-star "></span><span class="icon icon-star"></span><span class="icon icon-star"></span><span class="icon icon-star "></span><span class="icon icon-star"></span>
                                    </td>
                                </tr><tr>
                                    <td><a href="/news/id_9965820.html" data-remote="/news/modal/9965820" data-toggle="modal" title="深天马A：公司正在积极推进第6代LTPS AMOLED产线量产" data-target="#news-modal">深天马A：公司正在积极推进第6代LTPS AMOLED产线量产                                </a>
                                    </td>
                                    <td>11-10 21:25                                    </td>
                                    <td>云财经</td>
                                    <td class="star-2
                                                                ">
                                        <span class="icon icon-star "></span><span class="icon icon-star"></span><span class="icon icon-star"></span><span class="icon icon-star "></span><span class="icon icon-star"></span>
                                    </td>
                                </tr><tr>
                                    <td><a href="/news/id_9964520.html" data-remote="/news/modal/9964520" data-toggle="modal" title="OLED板块集体拉升 两股涨停" data-target="#news-modal">OLED板块集体拉升 两股涨停                                </a>
                                    </td>
                                    <td>11-10 11:00                                    </td>
                                    <td>同花顺</td>
                                    <td class="star-1
                                                                ">
                                        <span class="icon icon-star "></span><span class="icon icon-star"></span><span class="icon icon-star"></span><span class="icon icon-star "></span><span class="icon icon-star"></span>
                                    </td>
                                </tr><tr>
                                    <td><a href="/news/id_9960415.html" data-remote="/news/modal/9960415" data-toggle="modal" title="智云股份：OLED柔性屏工艺预计最快2018年底或者2019年初放量" data-target="#news-modal">智云股份：OLED柔性屏工艺预计最快2018年底或者2019年初放量                                </a>
                                    </td>
                                    <td>11-08 17:05                                    </td>
                                    <td>证券时报网</td>
                                    <td class="star-2
                                                                ">
                                        <span class="icon icon-star "></span><span class="icon icon-star"></span><span class="icon icon-star"></span><span class="icon icon-star "></span><span class="icon icon-star"></span>
                                    </td>
                                </tr><tr>
                                    <td><a href="/news/id_9960397.html" data-remote="/news/modal/9960397" data-toggle="modal" title="大族激光：公司OLED设备尚未实现销售收入 目前在重要客户端测试" data-target="#news-modal">大族激光：公司OLED设备尚未实现销售收入 目前在重要客户端测试                                </a>
                                    </td>
                                    <td>11-08 16:55                                    </td>
                                    <td>证券时报网</td>
                                    <td class="star-2
                                                                ">
                                        <span class="icon icon-star "></span><span class="icon icon-star"></span><span class="icon icon-star"></span><span class="icon icon-star "></span><span class="icon icon-star"></span>
                                    </td>
                                </tr><tr>
                                    <td><a href="/news/id_9959824.html" data-remote="/news/modal/9959824" data-toggle="modal" title="OLED概念股午后快速拉升 莱宝高科涨停" data-target="#news-modal">OLED概念股午后快速拉升 莱宝高科涨停                                </a>
                                    </td>
                                    <td>11-08 13:41                                    </td>
                                    <td>证券时报网</td>
                                    <td class="star-4
                                                                ">
                                        <span class="icon icon-star "></span><span class="icon icon-star"></span><span class="icon icon-star"></span><span class="icon icon-star "></span><span class="icon icon-star"></span>
                                    </td>
                                </tr>                    </tbody>
                </table>
            </article>
            <article>
                <div class="border-title">
                    近5日OLED概念相关新闻及个股表现
                </div>
                <div>
                    <a href="/story/details/id_25_20171117.html" target="_blank">2017年11月17日</a>
                    <a href="/story/details/id_25_20171116.html" target="_blank">2017年11月16日</a>
                    <a href="/story/details/id_25_20171115.html" target="_blank">2017年11月15日</a>
                    <a href="/story/details/id_25_20171114.html" target="_blank">2017年11月14日</a>
                    <a href="/story/details/id_25_20171113.html" target="_blank">2017年11月13日</a>
                </div>
            </article>
            <article>
                <div class="border-title">
                    OLED概念常见问题解答
                </div>
                <div>
                    <p><img src="http://aliyun.yuncaijing.com/res/pc/assets/img/concept/ask.png?v=201701172359" alt="ask-logo">&nbsp&nbspOLED概念股的龙头股最有可能是哪几只？</p>
                    <p><img src="http://aliyun.yuncaijing.com/res/pc/assets/img/concept/answer.png?v=201701172359" alt="ask-logo">&nbsp&nbsp根据云财经智能题材挖掘技术自动匹配，OLED概念股的龙头股最有可能从以下几个股票中诞生
                        <a href="/quote/sz300481.html" target="_blank">濮阳惠成、</a>
                        <a href="/quote/sz300567.html" target="_blank">精测电子、</a>
                        <a href="/quote/sz002387.html" target="_blank">黑牛食品。</a>
                    </p>
                    <p><img src="http://aliyun.yuncaijing.com/res/pc/assets/img/concept/ask.png?v=201701172359" alt="ask-logo">&nbsp&nbspOLED概念股今天的平均涨幅和市场人气如何？</p>
                    <p><img src="http://aliyun.yuncaijing.com/res/pc/assets/img/concept/answer.png?v=201701172359" alt="ask-logo">&nbsp&nbsp今日OLED概念股平均涨幅为-3.65%，其中 <a href="/quote/sz300134.html" target="_blank">大富科技</a>涨幅最高，OLED概念目前市场关注度为 <span>0.00</span>。</p>
                    <p><img src="http://aliyun.yuncaijing.com/res/pc/assets/img/concept/ask.png?v=201701172359" alt="ask-logo">&nbsp&nbspOLED概念上市公司一共有多少家？</p>
                    <p><img src="http://aliyun.yuncaijing.com/res/pc/assets/img/concept/answer.png?v=201701172359" alt="ask-logo">&nbsp&nbspOLED概念一共有61家上市公司，其中14家OLED概念上市公司在上证交易所交易，另外47家OLED概念上市公司在深交所交易。</p>
                </div>
            </article>
        </div>
        <div class="container-right">
            <article>
                <div>
                    今日关注度：<i>0.00</i>
                    <br/> 今日较昨日：
                    <i>0.00</i>
                    <br/> 相关股票平均涨跌幅：
                                            <i class="sg">-3.65%</i>
                        <sup class="icon icon-question" data-toggle="tooltip"></sup>
                </div>
                <div>
                    <i>涨家数：4</i>
                    <i>跌家数：54</i>
                    <i>持平家数：3</i>
                    <i>停牌家数：0</i>
                </div>
            </article>
            <table class="table table-ycj table-hover today">
                <thead>
                    <tr>
                        <th>
                            <nobr>OLED相关股票</nobr>
                        </th>
                        <th>
                            <nobr>价格</nobr>
                        </th>
                        <th data-module="sorting" data-type="zdf">
                            <nobr>
                                涨跌幅
                                <i class="icon icon-asc"></i>
                                <i class="icon icon-desc"></i>
                            </nobr>
                        </th>
                        <th>功能</th>                        <th data-module="sorting" data-type="persent">
                            相关性
                            <i class="icon icon-asc"></i>
                            <i class="icon icon-desc"></i>
                        </th>
                    </tr>
                </thead>
                <tbody data-sortinger>
                    <tr data-zdf="-7.62" data-persent="100%" data-code="300481">
                            <td>
                                <a href="/quote/sz300481.html" target="_blank" data-showChart-code="300481" title="曲屏手机概念股濮阳惠成">
                                濮阳惠成（300481）
                            </a>
                            </td>
                            <td> 23.89</td>
                                                            <td class="sg">-7.62%</td>
                                                            <td>
                                    <span data-module="layer">
                                <span data-content> 濮阳惠成与OLED概念的关联原因:OLED显示替代液晶显示是未来发展趋势，OLED的应用普及必将带动上游功能材料需求的爆发式增长。公司根据市场需求情况开发出OLED功能材料芴类衍生物并于2011年形成产业化生产。公司重点开发OLED蓝光功能材料芴类衍生物，列在开发计划内的其他OLED功能材料主要包含：OLED空穴传输材料，空穴注入材料，空穴阻挡材料，电子传输材料，电子注入材料，电子阻挡材料及材料合成的催化剂配体有机膦类化合物等。</span> 关联原因
                                    </span>
                                </td>                            <td>
                                <div style="width: 100%">
                                    100%                                </div>
                            </td>
                        </tr><tr data-zdf="-2.02" data-persent="96%" data-code="300567">
                            <td>
                                <a href="/quote/sz300567.html" target="_blank" data-showChart-code="300567" title="曲屏手机概念股精测电子">
                                精测电子（300567）
                            </a>
                            </td>
                            <td> 121.00</td>
                                                            <td class="sg">-2.02%</td>
                                                            <td>
                                    <span data-module="layer">
                                <span data-content> 精测电子与OLED概念的关联原因:公司主营业务为平板显示检测系统的研发、生产与销售。公司主营产品包括模组检测系统、面板检测系统、OLED检测系统、AOI光学检测系统、TouchPanel检测系统和平板显示自动化设备。</span> 关联原因
                                    </span>
                                </td>                            <td>
                                <div style="width: 96%">
                                    96%                                </div>
                            </td>
                        </tr><tr data-zdf="-9.98" data-persent="82%" data-code="002387">
                            <td>
                                <a href="/quote/sz002387.html" target="_blank" data-showChart-code="002387" title="曲屏手机概念股黑牛食品">
                                黑牛食品（002387）
                            </a>
                            </td>
                            <td> 18.50</td>
                                                            <td class="sg">-9.98%</td>
                                                            <td>
                                    <span data-module="layer">
                                <span data-content> 黑牛食品与OLED概念的关联原因:</span> 关联原因
                                    </span>
                                </td>                            <td>
                                <div style="width: 82%">
                                    82%                                </div>
                            </td>
                        </tr><tr data-zdf="-0.32" data-persent="43%" data-code="603996">
                            <td>
                                <a href="/quote/sh603996.html" target="_blank" data-showChart-code="603996" title="曲屏手机概念股中新科技">
                                中新科技（603996）
                            </a>
                            </td>
                            <td> 18.45</td>
                                                            <td class="sg">-0.32%</td>
                                                            <td>
                                    <span data-module="layer">
                                <span data-content> 中新科技与OLED概念的关联原因:2015年年报显示，公司已有超薄OLED曲面电视、OLED曲面系列产品。2016年3月公司在互动表示，公司已经具备OLED相关技术，目前暂未有OLED相关产品产生销量。 </span> 关联原因
                                    </span>
                                </td>                            <td>
                                <div style="width: 43%">
                                    43%                                </div>
                            </td>
                        </tr><tr data-zdf="-4.39" data-persent="43%" data-code="300429">
                            <td>
                                <a href="/quote/sz300429.html" target="_blank" data-showChart-code="300429" title="OLED概念股强力新材">
                                强力新材（300429）
                            </a>
                            </td>
                            <td> 23.30</td>
                                                            <td class="sg">-4.39%</td>
                                                            <td>
                                    <span data-module="layer">
                                <span data-content> 强力新材与OLED概念的关联原因:2016年6月28日晚间公告，公司、昱镭光电科技股份有限公司（下称“昱镭光电”）、无锡韵金投资合伙企业（有限合伙）、上海淇闻投资合伙企业（有限合伙）拟共同出资6600万元设立常州强力昱镭光电材料有限公司（暂定名）。合资公司经营范围为OLED有机材料、聚酰亚胺 溶液及薄膜、OLED封装材料、光刻胶等电子材料的研发、生产和销售。昱镭光电拥有OLED有机材料的研发、生产经验、销售资源及专利技术。昱镭光电拥有64项专利，掌握OLED有机材料的升华及其管理技术，掌握OLED 有机材料的 QC、QA 检测技术；掌握OLED 材料生产销售相关的专门知识、信息和资源。</span> 关联原因
                                    </span>
                                </td>                            <td>
                                <div style="width: 43%">
                                    43%                                </div>
                            </td>
                        </tr><tr data-zdf="-6.37" data-persent="39%" data-code="300327">
                            <td>
                                <a href="/quote/sz300327.html" target="_blank" data-showChart-code="300327" title="新型显示概念股中颖电子">
                                中颖电子（300327）
                            </a>
                            </td>
                            <td> 31.45</td>
                                                            <td class="sg">-6.37%</td>
                                                            <td>
                                    <span data-module="layer">
                                <span data-content> 中颖电子与OLED概念的关联原因:2015年1月份，公司正式取得提供和辉光电AMOLED驱动芯片的量产订单，和辉光电正式采用公司开发的国内首颗高清AMOELD驱动芯片用于5.0寸和5.5寸AMOLED显示屏的量产。和辉光电是上海市政府和金山区政府共同投资的战略性新兴产业重点项目，是一家专注于中小尺寸AMOLED显示屏生产和下一代显示技术研发的高科技公司。目前己建成我国第一条设备最完善，技术最先进的第4.5代低温多晶硅(LTPS)AMOLED量产线。</span> 关联原因
                                    </span>
                                </td>                            <td>
                                <div style="width: 39%">
                                    39%                                </div>
                            </td>
                        </tr><tr data-zdf="-3.91" data-persent="39%" data-code="600552">
                            <td>
                                <a href="/quote/sh600552.html" target="_blank" data-showChart-code="600552" title="OLED概念股凯盛科技">
                                凯盛科技（600552）
                            </a>
                            </td>
                            <td> 8.12</td>
                                                            <td class="sg">-3.91%</td>
                                                            <td>
                                    <span data-module="layer">
                                <span data-content> 凯盛科技与OLED概念的关联原因:2010年12月，控股子公司蚌埠华益导电膜玻璃公司投资1.8亿元建设年产130万片电容式触摸屏用导电膜玻璃生产线。华益公司在占领和巩固ITO导电膜传统市场的同时，制定了向PDP(等离子显示器)、TFT-LCD(薄膜晶体管液晶显示器)、OLED(有机发光二极管显示器)等新型显示器用ITO导电膜玻璃领域进军的计划。项目建成后预计每年新增效益1300万元以上。2012年5月，该项目所有生产线全部投产；
2016年5月30日晚间公告，控股子公司安徽方兴光电新材料科技有限公司建设的年产80万平米电容式触摸屏柔性镀膜生产线，日前已正式投产。截至目前，月产能达到设计产能的95%，良品率95%以上，并逐步取代进口材料，已为国内外知名手机和平板品牌批量配套。方兴光电下一步还将研发柔性OLED显示封装技术，进一步拓展高端应用领域。</span> 关联原因
                                    </span>
                                </td>                            <td>
                                <div style="width: 39%">
                                    39%                                </div>
                            </td>
                        </tr><tr data-zdf="-5.43" data-persent="36%" data-code="600707">
                            <td>
                                <a href="/quote/sh600707.html" target="_blank" data-showChart-code="600707" title="OLED概念股彩虹股份">
                                彩虹股份（600707）
                            </a>
                            </td>
                            <td> 7.31</td>
                                                            <td class="sg">-5.43%</td>
                                                            <td>
                                    <span data-module="layer">
                                <span data-content> 彩虹股份与OLED概念的关联原因:公司子公司深圳虹阳设立的彩虹(佛山)平板显示有限公司，主要致力于生产OLED显示屏。2011年4月，公司拟以不低于14.3元/股的价格定向增发不超过4.3亿股，计划募集资金60亿元。其中，16亿元募集资金用于建设4.5代AMOLED生产线项目。项目拟新建AMOLED生产厂房及其配套生产厂房、模组生产线以及附属配套设施和洁净室等。项目达产后，预计可形成4.5代AMOLED面板36万片的年均生产能力，年平均销售收入约33.41亿元，平均税后利润4.66亿元，投资回收期为6.22年（税后）。彩虹二期OLED项目是建设两条4.5代AMOLED生产线，项目总投资94.6亿元，于2011年11月和2012年10月分别启动一条4.5代AMOLED生产线建设。建成后可年产AMOLED显示屏4000多万片。
</span> 关联原因
                                    </span>
                                </td>                            <td>
                                <div style="width: 36%">
                                    36%                                </div>
                            </td>
                        </tr><tr data-zdf="-7.98" data-persent="35%" data-code="002845">
                            <td>
                                <a href="/quote/sz002845.html" target="_blank" data-showChart-code="002845" title="新型显示概念股同兴达">
                                同兴达（002845）
                            </a>
                            </td>
                            <td> 33.77</td>
                                                            <td class="sg">-7.98%</td>
                                                            <td>
                                    <span data-module="layer">
                                <span data-content> 同兴达与OLED概念的关联原因:公司主要从事研发、设计、生产和销售中小尺寸液晶显示模组。公司产品涵盖了COB、TAB、COG等LCD 模块产品，TFT、CSTN等彩色LCD显示产品，以及OLED显示产品。产品广泛应用于手机、通讯、数码产品、家用电器、工业控制、仪器仪表、车载显示器、彩屏显示等领域。 </span> 关联原因
                                    </span>
                                </td>                            <td>
                                <div style="width: 35%">
                                    35%                                </div>
                            </td>
                        </tr><tr data-zdf="-0.09" data-persent="33%" data-code="300128">
                            <td>
                                <a href="/quote/sz300128.html" target="_blank" data-showChart-code="300128" title="曲屏手机概念股锦富技术">
                                锦富技术（300128）
                            </a>
                            </td>
                            <td> 11.11</td>
                                                            <td class="sg">-0.09%</td>
                                                            <td>
                                    <span data-module="layer">
                                <span data-content> 锦富技术与OLED概念的关联原因:公司通过既有优质客户体系，市场份额在国内光电显示薄膜器件市场中位列前茅。公司是包含三星，LGD，瑞仪光电等一大批国际，国内液晶显示模块和背光模组龙头企业的重要供应商。公司2012年柔性线路板销售收入超1亿元，柔性线路板是OLED的关键技术之一；2014年公司完成并购奥英光电，2015年奥英光电开发出多款具有自主知识产权的曲面智能电视/显示器整机。 </span> 关联原因
                                    </span>
                                </td>                            <td>
                                <div style="width: 33%">
                                    33%                                </div>
                            </td>
                        </tr><tr data-zdf="-3.25" data-persent="31%" data-code="002643">
                            <td>
                                <a href="/quote/sz002643.html" target="_blank" data-showChart-code="002643" title="新型显示概念股万润股份">
                                万润股份（002643）
                            </a>
                            </td>
                            <td> 12.21</td>
                                                            <td class="sg">-3.25%</td>
                                                            <td>
                                    <span data-module="layer">
                                <span data-content> 万润股份与OLED概念的关联原因:2013年1月份，公司以3000万元与李崇，梅村经发合资设立的子公司三月光电(公司占64.01%，李崇占34.29%，梅村经发占1.7%)完成工商注册登记。未来三月光电将以技术团队为核心，结合公司在OLED材料方面长期积累的技术和客户资源，专注于OLED显示和照明材料，器件的研发，生产和销售。</span> 关联原因
                                    </span>
                                </td>                            <td>
                                <div style="width: 31%">
                                    31%                                </div>
                            </td>
                        </tr><tr data-zdf="-3.91" data-persent="29%" data-code="000973">
                            <td>
                                <a href="/quote/sz000973.html" target="_blank" data-showChart-code="000973" title="曲屏手机概念股佛塑科技">
                                佛塑科技（000973）
                            </a>
                            </td>
                            <td> 6.63</td>
                                                            <td class="sg">-3.91%</td>
                                                            <td>
                                    <span data-module="layer">
                                <span data-content> 佛塑科技与OLED概念的关联原因:公司官网显示产品包含有3D产品-偏光片，OLED偏光片等。</span> 关联原因
                                    </span>
                                </td>                            <td>
                                <div style="width: 29%">
                                    29%                                </div>
                            </td>
                        </tr><tr data-zdf="-5.92" data-persent="28%" data-code="000050">
                            <td>
                                <a href="/quote/sz000050.html" target="_blank" data-showChart-code="000050" title="oled概念股深天马A">
                                深天马A（000050）
                            </a>
                            </td>
                            <td> 23.99</td>
                                                            <td class="sg">-5.92%</td>
                                                            <td>
                                    <span data-module="layer">
                                <span data-content> 深天马A与OLED概念的关联原因:公司属专门从事液晶显示器（LCD）及液晶显示模块（LCM）产品的研发、设计、生产及销售，已布局AMOLED、LTPS、Oxide-TFT、In-Cell、On-Cell、3D、透明显示等前沿技术。</span> 关联原因
                                    </span>
                                </td>                            <td>
                                <div style="width: 28%">
                                    28%                                </div>
                            </td>
                        </tr><tr data-zdf="-4.21" data-persent="27%" data-code="002618">
                            <td>
                                <a href="/quote/sz002618.html" target="_blank" data-showChart-code="002618" title="新型显示概念股丹邦科技">
                                丹邦科技（002618）
                            </a>
                            </td>
                            <td> 14.10</td>
                                                            <td class="sg">-4.21%</td>
                                                            <td>
                                    <span data-module="layer">
                                <span data-content> 丹邦科技与OLED概念的关联原因:公司专注于微电子柔性互连与封装业务，是全球极少数产业链涵盖从基材、基板到芯片封装的企业之一，形成了从FCCL→FPC、FCCL→COF柔性封装基板→COF产品的完整产业链。</span> 关联原因
                                    </span>
                                </td>                            <td>
                                <div style="width: 27%">
                                    27%                                </div>
                            </td>
                        </tr><tr data-zdf="-9.95" data-persent="25%" data-code="300346">
                            <td>
                                <a href="/quote/sz300346.html" target="_blank" data-showChart-code="300346" title="OLED概念股南大光电">
                                南大光电（300346）
                            </a>
                            </td>
                            <td> 26.80</td>
                                                            <td class="sg">-9.95%</td>
                                                            <td>
                                    <span data-module="layer">
                                <span data-content> 南大光电与OLED概念的关联原因:{"6944325":"OLED概念大跌 南大光电领跌","5504018":"南大光电：OLED电视战略获国家支持 南大光电大涨","6160463":"OLED概念回调 南大光电跌逾6%"}</span> 关联原因
                                    </span>
                                </td>                            <td>
                                <div style="width: 25%">
                                    25%                                </div>
                            </td>
                        </tr><tr data-zdf="-3.92" data-persent="25%" data-code="000045">
                            <td>
                                <a href="/quote/sz000045.html" target="_blank" data-showChart-code="000045" title="新型显示概念股深纺织A">
                                深纺织A（000045）
                            </a>
                            </td>
                            <td> 10.55</td>
                                                            <td class="sg">-3.92%</td>
                                                            <td>
                                    <span data-module="layer">
                                <span data-content> 深纺织A与OLED概念的关联原因:2016年5月6日，公司在互动表示，公司的偏光片产品涵盖TN、STN、TFT、OLED、3D、染料片、触摸屏用光学膜等领域。</span> 关联原因
                                    </span>
                                </td>                            <td>
                                <div style="width: 25%">
                                    25%                                </div>
                            </td>
                        </tr><tr data-zdf="-3.56" data-persent="24%" data-code="002288">
                            <td>
                                <a href="/quote/sz002288.html" target="_blank" data-showChart-code="002288" title="oled概念股超华科技">
                                超华科技（002288）
                            </a>
                            </td>
                            <td> 6.51</td>
                                                            <td class="sg">-3.56%</td>
                                                            <td>
                                    <span data-module="layer">
                                <span data-content> 超华科技与OLED概念的关联原因:2013年6月份，公司以3000万元受让梅州泰华100%股权。该公司业务范围除了制造双面，多层线路板外，还生产柔性线路板。</span> 关联原因
                                    </span>
                                </td>                            <td>
                                <div style="width: 24%">
                                    24%                                </div>
                            </td>
                        </tr><tr data-zdf="-3.27" data-persent="24%" data-code="603228">
                            <td>
                                <a href="/quote/sh603228.html" target="_blank" data-showChart-code="603228" title="OLED概念股景旺电子">
                                景旺电子（603228）
                            </a>
                            </td>
                            <td> 57.74</td>
                                                            <td class="sg">-3.27%</td>
                                                            <td>
                                    <span data-module="layer">
                                <span data-content> 景旺电子与OLED概念的关联原因:公司产品类型覆盖FR4印制电路板、铝基电路板、柔性电路板、HDI板、刚挠结合板、高端电子材料等。公司产品HDI，是PCB（印刷电路板）作为电子元器件基础材料之一，市场容量占据元器件产值1/4以上，顺应下游产品轻化、复杂度提高的需求，高密度、高集成、柔性板（OLED）需求将快速提升，对应HDI需求增速预计约6.5%。</span> 关联原因
                                    </span>
                                </td>                            <td>
                                <div style="width: 24%">
                                    24%                                </div>
                            </td>
                        </tr><tr data-zdf="-3.74" data-persent="23%" data-code="000725">
                            <td>
                                <a href="/quote/sz000725.html" target="_blank" data-showChart-code="000725" title="新型显示概念股京东方A">
                                京东方A（000725）
                            </a>
                            </td>
                            <td> 6.18</td>
                                                            <td class="sg">-3.74%</td>
                                                            <td>
                                    <span data-module="layer">
                                <span data-content> 京东方A与OLED概念的关联原因:2016年1月份公司在互动表示，公司OLED产品已经量产出货。2014年10月，京东方签约拟在成都建设6代LTPS(低温多晶硅)/AMOLED(有机发光二极管)生产线项目，将生产高端手机显示及新兴移动显示等产品。一期项目2015年10月全面开工建设，预计2017年投产。2016年2月29日晚，公司公告透露，拟投资245亿元在成都上马6代LTPS/AMOLED生产线二期项目，主要生产AMOLED柔性中小尺寸面板。</span> 关联原因
                                    </span>
                                </td>                            <td>
                                <div style="width: 23%">
                                    23%                                </div>
                            </td>
                        </tr><tr data-zdf="-3.31" data-persent="23%" data-code="601208">
                            <td>
                                <a href="/quote/sh601208.html" target="_blank" data-showChart-code="601208" title="oled概念股东材科技">
                                东材科技（601208）
                            </a>
                            </td>
                            <td> 6.42</td>
                                                            <td class="sg">-3.31%</td>
                                                            <td>
                                    <span data-module="layer">
                                <span data-content> 东材科技与OLED概念的关联原因:2016年5月10日公司在投资者互动平台表示，光学膜材料是公司重点发展的产品，2015年7月，公司以超募资金投建的年产2万吨光学级聚酯基膜项目试车投产，产品主要应用于反射膜、增透膜、ITO导电膜、高端保护膜以及OLED产品等的制造。金张科技自主开发的产品AB胶替代了硅胶保护膜/OCA的两层贴合膜结构，具有客户使用综合成本低、、成品率高的领先技术优势，可以同时使用于LCD与OLED显示屏中，具有高透明、高粘的特点。</span> 关联原因
                                    </span>
                                </td>                            <td>
                                <div style="width: 23%">
                                    23%                                </div>
                            </td>
                        </tr><tr data-zdf="0.00" data-persent="21%" data-code="300097">
                            <td>
                                <a href="/quote/sz300097.html" target="_blank" data-showChart-code="300097" title="OLED概念股智云股份">
                                智云股份（300097）
                            </a>
                            </td>
                            <td> 31.38</td>
                                                            <td class="sy">0.00%</td>                            <td>
                                    <span data-module="layer">
                                <span data-content> 智云股份与OLED概念的关联原因:目前智云旗下鑫三力在OLED触控显示模组贴合设备上已实现销售收入，研发、销售进展明显快于国内竞争对手。2016年4月26日晚间公告，公司拟非公开发行不超过4000万股，募集资金总额不超过10亿元。募资中，2.52亿元拟投入3C智能制造装备产能建设项目。预案显示，3C智能制造装备产能建设项目实施主体是智云股份，项目建设地点位于大连普兰店经济开发区，建设期为2年，建成后将形成触控显示模组、摄像头模组、指纹模组生产线的成套装备生产能力。 </span> 关联原因
                                    </span>
                                </td>                            <td>
                                <div style="width: 21%">
                                    21%                                </div>
                            </td>
                        </tr><tr data-zdf="-4.02" data-persent="21%" data-code="300566">
                            <td>
                                <a href="/quote/sz300566.html" target="_blank" data-showChart-code="300566" title="新型显示概念股激智科技">
                                激智科技（300566）
                            </a>
                            </td>
                            <td> 36.25</td>
                                                            <td class="sg">-4.02%</td>
                                                            <td>
                                    <span data-module="layer">
                                <span data-content> 激智科技与OLED概念的关联原因: 公司是一家集光学薄膜和特种薄膜研发、生产、销售为一体的高科技公司。公司产品主要应用于光电显示、新能源和LED照明等领域。 </span> 关联原因
                                    </span>
                                </td>                            <td>
                                <div style="width: 21%">
                                    21%                                </div>
                            </td>
                        </tr><tr data-zdf="-4.19" data-persent="20%" data-code="002326">
                            <td>
                                <a href="/quote/sz002326.html" target="_blank" data-showChart-code="002326" title="oled概念股永太科技">
                                永太科技（002326）
                            </a>
                            </td>
                            <td> 12.80</td>
                                                            <td class="sg">-4.19%</td>
                                                            <td>
                                    <span data-module="layer">
                                <span data-content> 永太科技与OLED概念的关联原因:2016年5月10日公司在互动平台表示，公司与华星光电正在积极开展OLED和TFT-LCD用CF色阻的技术研发工作。国内面板企业主要有华星光电，京东方，天马，和辉光电等，国外面板企业主要有LGD ，三星等。公司的CF光刻胶产品目前已顺利通过国内目标客户验证，并完成小规模量产生产线的验证。</span> 关联原因
                                    </span>
                                </td>                            <td>
                                <div style="width: 20%">
                                    20%                                </div>
                            </td>
                        </tr><tr data-zdf="-2.30" data-persent="20%" data-code="300263">
                            <td>
                                <a href="/quote/sz300263.html" target="_blank" data-showChart-code="300263" title="oled概念股隆华节能">
                                隆华节能（300263）
                            </a>
                            </td>
                            <td> 8.49</td>
                                                            <td class="sg">-2.30%</td>
                                                            <td>
                                    <span data-module="layer">
                                <span data-content> 隆华节能与OLED概念的关联原因:2016年5月公司在互动表示，全资子公司四丰电子正在安装OLED所用的靶材生产线，预计三季度安装调试完毕。届时将会有产品供应用于OLED的生产。 </span> 关联原因
                                    </span>
                                </td>                            <td>
                                <div style="width: 20%">
                                    20%                                </div>
                            </td>
                        </tr><tr data-zdf="-1.39" data-persent="20%" data-code="600533">
                            <td>
                                <a href="/quote/sh600533.html" target="_blank" data-showChart-code="600533" title="oled概念股栖霞建设">
                                栖霞建设（600533）
                            </a>
                            </td>
                            <td> 5.67</td>
                                                            <td class="sg">-1.39%</td>
                                                            <td>
                                    <span data-module="layer">
                                <span data-content> 栖霞建设与OLED概念的关联原因:南京电子网板科技股份有限公司新厂区在南京经济技术开发区开工生产，同时由南京电子网板公司和韩国两家企业合资经营的南京汇金锦元光电材料有限公司(以下简称锦元光电)ITO导电膜项目在此奠基。
栖霞建设(600533)间接持有锦元光电37.5%的股份，是公司第一大股东。</span> 关联原因
                                    </span>
                                </td>                            <td>
                                <div style="width: 20%">
                                    20%                                </div>
                            </td>
                        </tr><tr data-zdf="-7.80" data-persent="18%" data-code="600206">
                            <td>
                                <a href="/quote/sh600206.html" target="_blank" data-showChart-code="600206" title="oled概念股有研新材">
                                有研新材（600206）
                            </a>
                            </td>
                            <td> 10.28</td>
                                                            <td class="sg">-7.80%</td>
                                                            <td>
                                    <span data-module="layer">
                                <span data-content> 有研新材与OLED概念的关联原因:公司旗下的有研亿金是国内规模最大的高纯金属溅射靶材制造企业，膜材料是实现柔OLED性的关键，而靶材是电子薄膜材料主要原材料。</span> 关联原因
                                    </span>
                                </td>                            <td>
                                <div style="width: 18%">
                                    18%                                </div>
                            </td>
                        </tr><tr data-zdf="-3.70" data-persent="17%" data-code="000100">
                            <td>
                                <a href="/quote/sz000100.html" target="_blank" data-showChart-code="000100" title="OLED概念股TCL集团">
                                TCL集团（000100）
                            </a>
                            </td>
                            <td> 4.68</td>
                                                            <td class="sg">-3.70%</td>
                                                            <td>
                                    <span data-module="layer">
                                <span data-content> TCL集团与OLED概念的关联原因:2015年2月份，定增事项获得证监会核准。2014年8月份，公司以2.09元/股定增不超27.28亿股募资不超57亿元投资t2项目和补充流动资金。t2项目总投资244亿元，加工玻璃基板尺寸为2200mm×2500mm，设计月投片量10万片，同时建设项目新技术研发配套设施，主要产品为23.6寸，32寸，42寸，55寸，65寸液晶显示屏，55寸OLED显示屏，85寸—88寸超大型公共显示屏。t2项目已于2013年11月打桩开工建设。项目建设周期为17个月，税后内部收益率为13.69%，项目动态回收期8.7年。</span> 关联原因
                                    </span>
                                </td>                            <td>
                                <div style="width: 17%">
                                    17%                                </div>
                            </td>
                        </tr><tr data-zdf="-6.64" data-persent="16%" data-code="002106">
                            <td>
                                <a href="/quote/sz002106.html" target="_blank" data-showChart-code="002106" title="新型显示概念股莱宝高科">
                                莱宝高科（002106）
                            </a>
                            </td>
                            <td> 9.28</td>
                                                            <td class="sg">-6.64%</td>
                                                            <td>
                                    <span data-module="layer">
                                <span data-content> 莱宝高科与OLED概念的关联原因:公司自主开发和掌握的上述关键技术不仅确保在国内同行的技术领先优势，而且保证产品品质的不断提高；同时由于其具有一定的通用性和延展性，可应用到触摸屏、TFT-LCD 、 OLED 等产品的制造中，公司主要技术包括OLED用ITO镀膜技术。</span> 关联原因
                                    </span>
                                </td>                            <td>
                                <div style="width: 16%">
                                    16%                                </div>
                            </td>
                        </tr><tr data-zdf="-1.25" data-persent="15%" data-code="002384">
                            <td>
                                <a href="/quote/sz002384.html" target="_blank" data-showChart-code="002384" title="新型显示概念股东山精密">
                                东山精密（002384）
                            </a>
                            </td>
                            <td> 31.59</td>
                                                            <td class="sg">-1.25%</td>
                                                            <td>
                                    <span data-module="layer">
                                <span data-content> 东山精密与OLED概念的关联原因:2016年2月发布非公开发行股票预案，公司拟以不低于15.93元/股的价格向不超过10名特定对象发行股份不超过2.82亿股，募集资金总额不超过45亿元，用于收购美国纳斯达克上市公司MFLX公司100%股权以及补充流动资金。据了解，MFLX 公司主要从事柔性电路板(FPC)和柔性电路组件(FPCA)的设计、生产和销售；
2016年6月13日晚间公告，公司与上海和辉光电有限公司签署了《战略合作协议》。和辉光电成立于2012年10月，是一家专注于中小尺寸AMOLED显示屏 生产和下一代显示技术研发的高科技公司。根据协议，和辉光电为公司提供OLED基板，并提供产品研发和OLED基板技术支持；公司进行OLED产品模组和全贴生产、销售和客户服务。通过双方的战略合作，在手机，智能穿戴设备方面，能够开拓新的客户资源，为客户提供更具品质和成本的产品。</span> 关联原因
                                    </span>
                                </td>                            <td>
                                <div style="width: 15%">
                                    15%                                </div>
                            </td>
                        </tr><tr data-zdf="-5.03" data-persent="14%" data-code="002341">
                            <td>
                                <a href="/quote/sz002341.html" target="_blank" data-showChart-code="002341" title="曲屏手机概念股新纶科技">
                                新纶科技（002341）
                            </a>
                            </td>
                            <td> 25.30</td>
                                                            <td class="sg">-5.03%</td>
                                                            <td>
                                    <span data-module="layer">
                                <span data-content> 新纶科技与OLED概念的关联原因:2016年5月3日，公司在互动表示，针对OLED以及LED触摸屏公司进行了产业布局与技术储备，COP膜、触摸屏膜、SRF膜等公司拥有成熟的技术储备。公司对显示行业的技术趋势发展有着清晰认知与判断，因此早已进行相关产品布局与规划。</span> 关联原因
                                    </span>
                                </td>                            <td>
                                <div style="width: 14%">
                                    14%                                </div>
                            </td>
                        </tr><tr data-zdf="-3.85" data-persent="14%" data-code="300057">
                            <td>
                                <a href="/quote/sz300057.html" target="_blank" data-showChart-code="300057" title="曲屏手机概念股万顺股份">
                                万顺股份（300057）
                            </a>
                            </td>
                            <td> 10.73</td>
                                                            <td class="sg">-3.85%</td>
                                                            <td>
                                    <span data-module="layer">
                                <span data-content> 万顺股份与OLED概念的关联原因:公司导电膜二期扩建项目第一条生产线、第二条生产线（双线产能）、第三条生产线（有效宽幅可达1570mm）已分别于2013年10月、2014年3月、2015年11月投产。ITO导电膜是触摸屏实现触摸控制的关键原材料之一，它是一种以PET为基材、具有良好均匀面电阻和较高透过率的导电薄膜，ITO导电膜可应用于柔性OLED作为电极。</span> 关联原因
                                    </span>
                                </td>                            <td>
                                <div style="width: 14%">
                                    14%                                </div>
                            </td>
                        </tr><tr data-zdf="-5.10" data-persent="14%" data-code="002020">
                            <td>
                                <a href="/quote/sz002020.html" target="_blank" data-showChart-code="002020" title="曲屏手机概念股京新药业">
                                京新药业（002020）
                            </a>
                            </td>
                            <td> 12.85</td>
                                                            <td class="sg">-5.10%</td>
                                                            <td>
                                    <span data-module="layer">
                                <span data-content> 京新药业与OLED概念的关联原因:2016年6月2日，京新药业在投资者关系互动平台上表示，巨烽已经将OLED显示的应用列入到新产品开发计划中。
</span> 关联原因
                                    </span>
                                </td>                            <td>
                                <div style="width: 14%">
                                    14%                                </div>
                            </td>
                        </tr><tr data-zdf="-5.28" data-persent="13%" data-code="300088">
                            <td>
                                <a href="/quote/sz300088.html" target="_blank" data-showChart-code="300088" title="oled概念股长信科技">
                                长信科技（300088）
                            </a>
                            </td>
                            <td> 9.50</td>
                                                            <td class="sg">-5.28%</td>
                                                            <td>
                                    <span data-module="layer">
                                <span data-content> 长信科技与OLED概念的关联原因:公司专注于平板显示真空薄膜材料的研发、生产、销售，致力于自主研发的核心技术“真空薄膜技术”在平板显示行业的应用，是平板显示行业上游关键基础材料的专业供应商。主导产品包括液晶显示（LCD）用ITO导电玻璃（主要是TN/STN-LCD）、触摸屏用ITO导电玻璃、手机面板视窗等三大类产品，并在OLED的应用方面进行了相应的技术储备。 </span> 关联原因
                                    </span>
                                </td>                            <td>
                                <div style="width: 13%">
                                    13%                                </div>
                            </td>
                        </tr><tr data-zdf="-2.12" data-persent="12%" data-code="000016">
                            <td>
                                <a href="/quote/sz000016.html" target="_blank" data-showChart-code="000016" title="新型显示概念股深康佳A">
                                深康佳A（000016）
                            </a>
                            </td>
                            <td> 6.46</td>
                                                            <td class="sg">-2.12%</td>
                                                            <td>
                                    <span data-module="layer">
                                <span data-content> 深康佳A与OLED概念的关联原因:2016年4月，公司拟以4.71元/股向控股股东华侨城集团等6名特定对象非公开发行不超过6.37亿股，募集资金总额不超过30亿元，拟全部用于智能电视研发与运营平台建设项目、品牌与渠道建设项目、偿还银行贷款及补充流动资金。募投项目方面，公司拟投入募集资金3亿元用于智能电视研发与运营平台建设项目，主要研发方向包括互联网运营平台研发、OLED 显示技术研发、8K超高清显示技术研发等。</span> 关联原因
                                    </span>
                                </td>                            <td>
                                <div style="width: 12%">
                                    12%                                </div>
                            </td>
                        </tr><tr data-zdf="-2.42" data-persent="11%" data-code="300476">
                            <td>
                                <a href="/quote/sz300476.html" target="_blank" data-showChart-code="300476" title="oled概念股胜宏科技">
                                胜宏科技（300476）
                            </a>
                            </td>
                            <td> 25.86</td>
                                                            <td class="sg">-2.42%</td>
                                                            <td>
                                    <span data-module="layer">
                                <span data-content> 胜宏科技与OLED概念的关联原因:公司专业从事高密度印制线路板的研发，生产和销售，主要产品为双面板，多层板(含HDI)等，产品广泛用于计算机及其周边，网络通讯，消费电子，汽车，LED，工业控制等下游领域。公司产品HDI，是PCB（印刷电路板）作为电子元器件基础材料之一，市场容量占据元器件产值1/4以上，顺应下游产品轻化、复杂度提高的需求，高密度、高集成、柔性板（OLED）需求将快速提升，对应HDI需求增速预计约6.5%。</span> 关联原因
                                    </span>
                                </td>                            <td>
                                <div style="width: 11%">
                                    11%                                </div>
                            </td>
                        </tr><tr data-zdf="-9.98" data-persent="10%" data-code="300227">
                            <td>
                                <a href="/quote/sz300227.html" target="_blank" data-showChart-code="300227" title="曲屏手机概念股光韵达">
                                光韵达（300227）
                            </a>
                            </td>
                            <td> 24.62</td>
                                                            <td class="sg">-9.98%</td>
                                                            <td>
                                    <span data-module="layer">
                                <span data-content> 光韵达与OLED概念的关联原因:公司通过互动易平台表示，现有业务中有提供柔性线路板激光成型服务，且目前该项业务收入约占公司营业收入的15%。此外，公司精密激光综合应用产业化基地项目达产后，可形成柔性线路板激光成型加工工时240000分钟/年。公司持股75%的深圳光韵达激光主营业务为柔性线路板激光成型服务。该公司2013年1-12月实现营业收入2724万元，实现净利润687万元。 </span> 关联原因
                                    </span>
                                </td>                            <td>
                                <div style="width: 10%">
                                    10%                                </div>
                            </td>
                        </tr><tr data-zdf="-1.49" data-persent="10%" data-code="300296">
                            <td>
                                <a href="/quote/sz300296.html" target="_blank" data-showChart-code="300296" title="曲屏手机概念股利亚德">
                                利亚德（300296）
                            </a>
                            </td>
                            <td> 22.51</td>
                                                            <td class="sg">-1.49%</td>
                                                            <td>
                                    <span data-module="layer">
                                <span data-content> 利亚德与OLED概念的关联原因:2016年5月27日公司在互动表示，利亚德旗下全资控股公司美国平达拥有OLED产品，其OLED产品定位于广告等商业领域的应用。 </span> 关联原因
                                    </span>
                                </td>                            <td>
                                <div style="width: 10%">
                                    10%                                </div>
                            </td>
                        </tr><tr data-zdf="-8.15" data-persent="9%" data-code="002449">
                            <td>
                                <a href="/quote/sz002449.html" target="_blank" data-showChart-code="002449" title="新型显示概念股国星光电">
                                国星光电（002449）
                            </a>
                            </td>
                            <td> 20.05</td>
                                                            <td class="sg">-8.15%</td>
                                                            <td>
                                    <span data-module="layer">
                                <span data-content> 国星光电与OLED概念的关联原因:2016年5月16日公司在互动平台上表示，关于OLED对公司的影响，公司拥有独立的研发中心，关注分析行业动态及趋势，保持公司对新产品、新市场的灵敏度。 </span> 关联原因
                                    </span>
                                </td>                            <td>
                                <div style="width: 9%">
                                    9%                                </div>
                            </td>
                        </tr><tr data-zdf="2.58" data-persent="9%" data-code="300433">
                            <td>
                                <a href="/quote/sz300433.html" target="_blank" data-showChart-code="300433" title="曲屏手机概念股蓝思科技">
                                蓝思科技（300433）
                            </a>
                            </td>
                            <td> 38.98</td>
                            <td class="sr">2.58%</td>
                                                            <td>
                                    <span data-module="layer">
                                <span data-content> 蓝思科技与OLED概念的关联原因:2016年5月，公司在投资者互动平台表示，公司有与OLED屏相关产品的研发、生产，公司的3D曲面玻璃已实现量产。</span> 关联原因
                                    </span>
                                </td>                            <td>
                                <div style="width: 9%">
                                    9%                                </div>
                            </td>
                        </tr><tr data-zdf="0.00" data-persent="8%" data-code="002579">
                            <td>
                                <a href="/quote/sz002579.html" target="_blank" data-showChart-code="002579" title="OLED概念股中京电子">
                                中京电子（002579）
                            </a>
                            </td>
                            <td> 10.20</td>
                                                            <td class="sy">0.00%</td>                            <td>
                                    <span data-module="layer">
                                <span data-content> 中京电子与OLED概念的关联原因:公司主要产品包括双面板、多层板及HDI板和铝基板等印刷电路板，产品广泛应用于消费电子、网络通讯、电脑周边、汽车电子等领域。2014年3月，公司资产重组涉及标的资产的审计评估等工作已初步完成--拟以8.83元/股定增约2575万股(方正达股东方笑求、蓝顺明分别以42.56%方正达股份认购，限售期为36个月及15个月)+4255.69万元现金收购购湖南方正达100%股份。方正达的主营业务为挠性印制电路板(FPC)的研发、生产和销售，产品百分之百经过通路电子测试、自动光学检测，对产品的质量检测标准、关键技术性能指标的控制标准均高于行业平均水平，良品率保持在98%以上，并主要应用于节能照明领域。 </span> 关联原因
                                    </span>
                                </td>                            <td>
                                <div style="width: 8%">
                                    8%                                </div>
                            </td>
                        </tr><tr data-zdf="-2.25" data-persent="8%" data-code="600839">
                            <td>
                                <a href="/quote/sh600839.html" target="_blank" data-showChart-code="600839" title="OLED概念股四川长虹">
                                四川长虹（600839）
                            </a>
                            </td>
                            <td> 3.91</td>
                                                            <td class="sg">-2.25%</td>
                                                            <td>
                                    <span data-module="layer">
                                <span data-content> 四川长虹与OLED概念的关联原因:公司是一家具有全球竞争力的消费电子系统供应商和内容服务提供商，OLED产业为公司发展的战略重点，公司已有多款OLED产品上市。</span> 关联原因
                                    </span>
                                </td>                            <td>
                                <div style="width: 8%">
                                    8%                                </div>
                            </td>
                        </tr><tr data-zdf="-9.97" data-persent="8%" data-code="600460">
                            <td>
                                <a href="/quote/sh600460.html" target="_blank" data-showChart-code="600460" title="新型显示概念股士兰微">
                                士兰微（600460）
                            </a>
                            </td>
                            <td> 10.75</td>
                                                            <td class="sg">-9.97%</td>
                                                            <td>
                                    <span data-module="layer">
                                <span data-content> 士兰微与OLED概念的关联原因:公司是一家专业从事集成电路以及半导体微电子相关产品的设计、生产与销售的高新技术企业，已成功开发出具有自主知识产权的国内第一款OLED专用驱动IC芯片。</span> 关联原因
                                    </span>
                                </td>                            <td>
                                <div style="width: 8%">
                                    8%                                </div>
                            </td>
                        </tr><tr data-zdf="-2.74" data-persent="8%" data-code="002585">
                            <td>
                                <a href="/quote/sz002585.html" target="_blank" data-showChart-code="002585" title="曲屏手机概念股双星新材">
                                双星新材（002585）
                            </a>
                            </td>
                            <td> 7.10</td>
                                                            <td class="sg">-2.74%</td>
                                                            <td>
                                    <span data-module="layer">
                                <span data-content> 双星新材与OLED概念的关联原因:2013年10月，股东大会同意公司以不低于8.63元/股向不超过十名特定对象定增不超过1.6亿股，募资不超过14亿元，用于建设年产一亿平米光学膜项目，该项目拟生产的光学膜属中厚型特种聚酯薄膜，主要包括光学膜、窗膜、ITO膜及柔性电路板等产品。 </span> 关联原因
                                    </span>
                                </td>                            <td>
                                <div style="width: 8%">
                                    8%                                </div>
                            </td>
                        </tr><tr data-zdf="2.68" data-persent="7%" data-code="300134">
                            <td>
                                <a href="/quote/sz300134.html" target="_blank" data-showChart-code="300134" title="曲屏手机概念股大富科技">
                                大富科技（300134）
                            </a>
                            </td>
                            <td> 15.31</td>
                            <td class="sr">2.68%</td>
                                                            <td>
                                    <span data-module="layer">
                                <span data-content> 大富科技与OLED概念的关联原因:2015年5月22日晚，公司发布公告称，为进一步夯实柔性OLED显示模组产业化项目的技术基础，进而完善公司在智能终端的产业链布局，拟使用不超过人民币12,000万元的自有资金向广东中显进行增资，增资完成后公司将占广东中显51%的股权比例，加速广东中显拥有的国产OLED核心技术产业化转化进程。据了解,广东中显拥有以“OLED”之父为领军人物的核心技术团队，数项国内、国际核心技术专利。在OLED屏幕核心的TFT制备工艺中，广东中显独创的BG金属诱导技术，相对三星的激光退火技术或LG的金属氧化物技术，在显示屏尺寸、质量性能、生产工艺及良品率及生产成本上均具有比较优势，具有极强的产业化价值。 </span> 关联原因
                                    </span>
                                </td>                            <td>
                                <div style="width: 7%">
                                    7%                                </div>
                            </td>
                        </tr><tr data-zdf="-5.54" data-persent="7%" data-code="002429">
                            <td>
                                <a href="/quote/sz002429.html" target="_blank" data-showChart-code="002429" title="曲屏手机概念股兆驰股份">
                                兆驰股份（002429）
                            </a>
                            </td>
                            <td> 3.58</td>
                                                            <td class="sg">-5.54%</td>
                                                            <td>
                                    <span data-module="layer">
                                <span data-content> 兆驰股份与OLED概念的关联原因:2016年5月30日，兆驰股份前日在投资者关系互动平台上表示，推出高端OLED产品是公司重要的发展方向之一。
资料显示：深圳市兆驰股份(002429)有限公司是一家专业从事家庭视听消费类电子产品研发、设计、生产、销售的国家级高新技术企业。</span> 关联原因
                                    </span>
                                </td>                            <td>
                                <div style="width: 7%">
                                    7%                                </div>
                            </td>
                        </tr><tr data-zdf="-5.89" data-persent="7%" data-code="300395">
                            <td>
                                <a href="/quote/sz300395.html" target="_blank" data-showChart-code="300395" title="新型显示概念股菲利华">
                                菲利华（300395）
                            </a>
                            </td>
                            <td> 17.90</td>
                                                            <td class="sg">-5.89%</td>
                                                            <td>
                                    <span data-module="layer">
                                <span data-content> 菲利华与OLED概念的关联原因:公司产品合成石英锭可用作TFT-LCD和OLED平板显示器生产的光掩膜基板，是仅次于硅材料的第二大半导体制造材料，目前为日本行业主流光掩膜供应商供货。该产品壁垒很高，全球竞争对手仅有日本TOSOH，日本HOYA和美国CORNING等国际厂商。</span> 关联原因
                                    </span>
                                </td>                            <td>
                                <div style="width: 7%">
                                    7%                                </div>
                            </td>
                        </tr><tr data-zdf="-2.43" data-persent="7%" data-code="600961">
                            <td>
                                <a href="/quote/sh600961.html" target="_blank" data-showChart-code="600961" title="OLED概念股株冶集团">
                                株冶集团（600961）
                            </a>
                            </td>
                            <td> 8.84</td>
                                                            <td class="sg">-2.43%</td>
                                                            <td>
                                    <span data-module="layer">
                                <span data-content> 株冶集团与OLED概念的关联原因:OLED的基本结构是由一薄而透明具半导体特性之铟锡氧化物（ITO），与电力之正极相连，再加上另一个金属阴极，包成如三明治的结构。显示领域的ITO靶材中75%的材料都含有铟，而中国铟产量占世界50%以上，铟作为ITO靶材的基础原材料，其对于OLED的重要性不言而喻。资料显示，株冶集团涉足ITO靶材较早，且在行业中具有领先技术优势，在国内ITO靶材行业，株冶集团并没有竞争对手。</span> 关联原因
                                    </span>
                                </td>                            <td>
                                <div style="width: 7%">
                                    7%                                </div>
                            </td>
                        </tr><tr data-zdf="-3.59" data-persent="7%" data-code="002456">
                            <td>
                                <a href="/quote/sz002456.html" target="_blank" data-showChart-code="002456" title="新型显示概念股欧菲光">
                                欧菲光（002456）
                            </a>
                            </td>
                            <td> 23.92</td>
                                                            <td class="sg">-3.59%</td>
                                                            <td>
                                    <span data-module="layer">
                                <span data-content> 欧菲光与OLED概念的关联原因:公司为我国较早掌握纯平电阻式触摸屏生产核心技术并形成规模化生产能力的厂商，公司2成功通过三星，摩托罗拉，联想，宇龙等消费电子产品国际巨头的产品认证，进入了其全球供应链。2012年公司与中科院苏州纳米技术与纳米仿生研究所共建“柔性光电技术联合实验室”。公司已完成触控系统垂直一体化的全产业链布局，涵盖强化玻璃、氧化铟锡（ITO）导电薄膜、纳米银金属网栅导电膜等产品。</span> 关联原因
                                    </span>
                                </td>                            <td>
                                <div style="width: 7%">
                                    7%                                </div>
                            </td>
                        </tr><tr data-zdf="-2.75" data-persent="6%" data-code="600330">
                            <td>
                                <a href="/quote/sh600330.html" target="_blank" data-showChart-code="600330" title="OLED概念股天通股份">
                                天通股份（600330）
                            </a>
                            </td>
                            <td> 10.61</td>
                                                            <td class="sg">-2.75%</td>
                                                            <td>
                                    <span data-module="layer">
                                <span data-content> 天通股份与OLED概念的关联原因:2016年3月24日，公司全资子公司天通吉成机器技术有限公司作为销售方，与鄂尔多斯市源盛光电有限责任公司签署了《设备采购合同》，合同金额：含税为12,665.25万元人民币。合同包含第5.5代AM-OLED有机发光显示器件项目的光学检测机、自动化输送系统等设备51台套。</span> 关联原因
                                    </span>
                                </td>                            <td>
                                <div style="width: 6%">
                                    6%                                </div>
                            </td>
                        </tr><tr data-zdf="-1.83" data-persent="5%" data-code="002450">
                            <td>
                                <a href="/quote/sz002450.html" target="_blank" data-showChart-code="002450" title="OLED概念股康得新">
                                康得新（002450）
                            </a>
                            </td>
                            <td> 25.76</td>
                                                            <td class="sg">-1.83%</td>
                                                            <td>
                                    <span data-module="layer">
                                <span data-content> 康得新与OLED概念的关联原因:公司为全球预涂膜行业领导者，目前公司有五大系列80余种产品，包含BOPP基材，PET基材，预涂膜，特种膜，Nylon，3D图像，覆膜及3D图像设备等系列产品，公司已研发可用于OLED柔性显示的光学膜。</span> 关联原因
                                    </span>
                                </td>                            <td>
                                <div style="width: 5%">
                                    5%                                </div>
                            </td>
                        </tr><tr data-zdf="-1.93" data-persent="5%" data-code="000990">
                            <td>
                                <a href="/quote/sz000990.html" target="_blank" data-showChart-code="000990" title="新型显示概念股诚志股份">
                                诚志股份（000990）
                            </a>
                            </td>
                            <td> 16.80</td>
                                                            <td class="sg">-1.93%</td>
                                                            <td>
                                    <span data-module="layer">
                                <span data-content> 诚志股份与OLED概念的关联原因:2016年5月19日公司在互动表示，目前公司开发了具有自主知识产权应用于OLED的空穴、传输、发光等材料，公司也将OLED用材料、器件的技术创新及产业化列入战略发展规划的重点工作。 </span> 关联原因
                                    </span>
                                </td>                            <td>
                                <div style="width: 5%">
                                    5%                                </div>
                            </td>
                        </tr><tr data-zdf="1.87" data-persent="5%" data-code="002055">
                            <td>
                                <a href="/quote/sz002055.html" target="_blank" data-showChart-code="002055" title="OLED概念股得润电子">
                                得润电子（002055）
                            </a>
                            </td>
                            <td> 23.94</td>
                            <td class="sr">1.87%</td>
                                                            <td>
                                    <span data-module="layer">
                                <span data-content> 得润电子与OLED概念的关联原因:公司柔性电路板产品在业内具有较高的知名度，技术实力较强，能制作行业内各种高难度柔性线路板。</span> 关联原因
                                    </span>
                                </td>                            <td>
                                <div style="width: 5%">
                                    5%                                </div>
                            </td>
                        </tr><tr data-zdf="0.00" data-persent="4%" data-code="002168">
                            <td>
                                <a href="/quote/sz002168.html" target="_blank" data-showChart-code="002168" title="曲屏手机概念股深圳惠程">
                                深圳惠程（002168）
                            </a>
                            </td>
                            <td> 16.99</td>
                                                            <td class="sy">0.00%</td>                            <td>
                                    <span data-module="layer">
                                <span data-content> 深圳惠程与OLED概念的关联原因:三星在CES2014上首次小范围展示了可折叠柔性屏幕，其基础材质仍将是塑胶基板(PlasticSubstrate)和类聚酰亚胺膜(Polyimidefilm)，公司投资3亿元增资控股子公司长春高琦用于建设聚酰亚胺纤维大规模产业化项目。</span> 关联原因
                                    </span>
                                </td>                            <td>
                                <div style="width: 4%">
                                    4%                                </div>
                            </td>
                        </tr><tr data-zdf="-2.15" data-persent="3%" data-code="600183">
                            <td>
                                <a href="/quote/sh600183.html" target="_blank" data-showChart-code="600183" title="新型显示概念股生益科技">
                                生益科技（600183）
                            </a>
                            </td>
                            <td> 16.42</td>
                                                            <td class="sg">-2.15%</td>
                                                            <td>
                                    <span data-module="layer">
                                <span data-content> 生益科技与OLED概念的关联原因:柔性线路板（FlexiblePrintedCircuitBoard，缩写FPC）又称为柔性印制电路板，该类产品体积小，重量轻，大大缩小装置的体积，适用电子产品向高密度，小型化，轻量化，型化，高可靠方向发展的需要，具有高度挠曲性，可自由弯曲等特点。项目历经公司数年的研究，开发，在2008年基本定型进入商业开发，并拥有了几个基本的产品型号和几项基本的技术，并已拥有了一批固定的，基本的客户，逐步拥有了独自的市场。2009年项目小组于半年左右完成了原定的全年目标，基本已完成“研发”阶段，已正式进入商业化经营。2012年，公司与日本FCCL(柔性覆铜板)巨头新日铁达成合作协议，共同组建柔性覆铜板销售公司。</span> 关联原因
                                    </span>
                                </td>                            <td>
                                <div style="width: 3%">
                                    3%                                </div>
                            </td>
                        </tr><tr data-zdf="-3.99" data-persent="3%" data-code="002005">
                            <td>
                                <a href="/quote/sz002005.html" target="_blank" data-showChart-code="002005" title="新型显示概念股德豪润达">
                                德豪润达（002005）
                            </a>
                            </td>
                            <td> 4.81</td>
                                                            <td class="sg">-3.99%</td>
                                                            <td>
                                    <span data-module="layer">
                                <span data-content> 德豪润达与OLED概念的关联原因:德豪润达收购深圳锐拓60%股权，介入OLED行业。公司是一家以开发、设计、制造、销售智能小家电产品、微特电机为主的外向型上市公司，公司的主要产品为厨房电器、居家护理、个人护理等共300多个品种，年生产和销售各类产品近3000万台，产销规模位居国际同行业前列。</span> 关联原因
                                    </span>
                                </td>                            <td>
                                <div style="width: 3%">
                                    3%                                </div>
                            </td>
                        </tr><tr data-zdf="-3.28" data-persent="3%" data-code="000012">
                            <td>
                                <a href="/quote/sz000012.html" target="_blank" data-showChart-code="000012" title="oled概念股南玻A">
                                南玻A（000012）
                            </a>
                            </td>
                            <td> 8.56</td>
                                                            <td class="sg">-3.28%</td>
                                                            <td>
                                    <span data-module="layer">
                                <span data-content> 南玻A与OLED概念的关联原因:2016年5月18日公司在互动表示，公司持有深圳南玻显示器件科技有限公司44.70%股权，而宜昌南玻显示器件有限公司为深圳南玻显示器件科技有限公司的全资子公司，因此，公司间接持有宜昌南玻显示器件有限公司44.70%股权。5月17日公司在互动表示宜昌显示器件一直在量产OLED用导电玻璃。</span> 关联原因
                                    </span>
                                </td>                            <td>
                                <div style="width: 3%">
                                    3%                                </div>
                            </td>
                        </tr><tr data-zdf="-5.24" data-persent="3%" data-code="000810">
                            <td>
                                <a href="/quote/sz000810.html" target="_blank" data-showChart-code="000810" title="oled概念股创维数字">
                                创维数字（000810）
                            </a>
                            </td>
                            <td> 9.76</td>
                                                            <td class="sg">-5.24%</td>
                                                            <td>
                                    <span data-module="layer">
                                <span data-content> 创维数字与OLED概念的关联原因:我国第一块彩色柔性AMOLED显示屏由发光材料与器件国家重点实验室与广州新视界光电科技有限公司共同研制成功，广州新视界光电科技有限公司由华南理工大学和创维-RGB电子有限公司共同投资创立。</span> 关联原因
                                    </span>
                                </td>                            <td>
                                <div style="width: 3%">
                                    3%                                </div>
                            </td>
                        </tr><tr data-zdf="2.51" data-persent="1%" data-code="600340">
                            <td>
                                <a href="/quote/sh600340.html" target="_blank" data-showChart-code="600340" title="oled概念股华夏幸福">
                                华夏幸福（600340）
                            </a>
                            </td>
                            <td> 32.21</td>
                            <td class="sr">2.51%</td>
                                                            <td>
                                    <span data-module="layer">
                                <span data-content> 华夏幸福与OLED概念的关联原因:2016年6月28日晚间公告，公司下属企业拟分别于河北省固安县及霸州市，投资建设第6代AMOLED面板生产线，以及OLED显示模组项目，加码OLED产业。其中，华夏幸福两家下属子公司拟与河北固安新兴产业示范区管理委员会、昆山国显光电有限公司，签署《新一代显示技术面板生产线项目投资框架协议》。其中，上述项目主要生产基板尺寸为1500mm×1850mm，包括阵列工序、蒸镀封合工序、模块工序、触摸屏 工序等生产工序。项目设计产能为30K/月，项目选址在河北固安新兴产业示范区。项目总投资约300亿元,其中落地投资额约258亿元。华夏幸福光电科技（固安）投资不超过40亿元，其余资金通过多种方式筹集。</span> 关联原因
                                    </span>
                                </td>                            <td>
                                <div style="width: 1%">
                                    1%                                </div>
                            </td>
                        </tr><tr data-zdf="-3.92" data-persent="1%" data-code="000536">
                            <td>
                                <a href="/quote/sz000536.html" target="_blank" data-showChart-code="000536" title="OLED概念股华映科技">
                                华映科技（000536）
                            </a>
                            </td>
                            <td> 5.15</td>
                                                            <td class="sg">-3.92%</td>
                                                            <td>
                                    <span data-module="layer">
                                <span data-content> 华映科技与OLED概念的关联原因:2016年5月16日公司在投资者互动平台上表示，公司此前公告投资的显示材料实验线就包含了OLED技术研发、人才培训等，公司未来将视OLED技术进展及市场状况积极布局OLED相关产业。</span> 关联原因
                                    </span>
                                </td>                            <td>
                                <div style="width: 1%">
                                    1%                                </div>
                            </td>
                        </tr><tr data-zdf="-0.98" data-persent="1%" data-code="600064">
                            <td>
                                <a href="/quote/sh600064.html" target="_blank" data-showChart-code="600064" title="OLED概念股南京高科">
                                南京高科（600064）
                            </a>
                            </td>
                            <td> 14.14</td>
                                                            <td class="sg">-0.98%</td>
                                                            <td>
                                    <span data-module="layer">
                                <span data-content> 南京高科与OLED概念的关联原因:子公司南京高科新创投资于09年5月份出资3000万元参与投资设立了南京瑞科方圆显示技术有限公司暨南京TFT-OLED工程技术研究中心。主要开展TFT-OLED技术研究，开发TFT-OLED工程技术，并推动TFT-OLED工程技术的产业化，力争在两至三年内建成一条AMOLED（有源矩阵OLED）显示中试线。南京瑞福达目前已全面掌握了TFT面板的设计和制造技术，产品全面进入市场，重点实验室自主研发的红光与蓝光材料性能稳定，色纯度良好，效率达到国际先进水平。
2010年南京高科新创投资对瑞科方圆持股比例由33.33%增加至100%。瑞科方圆2010年净利润30.12万元。2011年子公司南京高科新创投资公司收回对其全资子公司南京瑞科方圆显示技术公司的投资，瑞科方圆工商注销手续于2011年3月完成。</span> 关联原因
                                    </span>
                                </td>                            <td>
                                <div style="width: 1%">
                                    1%                                </div>
                            </td>
                        </tr><tr data-zdf="-5.95" data-persent="1%" data-code="300037">
                            <td>
                                <a href="/quote/sz300037.html" target="_blank" data-showChart-code="300037" title="oled概念股新宙邦">
                                新宙邦（300037）
                            </a>
                            </td>
                            <td> 20.23</td>
                                                            <td class="sg">-5.95%</td>
                                                            <td>
                                    <span data-module="layer">
                                <span data-content> 新宙邦与OLED概念的关联原因:2016年5月26日公司在互动表示，公司在官网已披露过有关公司AMOLED阳极蚀刻液供货昆山维信诺显示技术有限公司的信息。能实现OLED领域的供货，与公司在这方面已经经过较长时间的技术积累和人才培养是分不开的。</span> 关联原因
                                    </span>
                                </td>                            <td>
                                <div style="width: 1%">
                                    1%                                </div>
                            </td>
                        </tr>                </tbody>
            </table>
            <p>您可能感兴趣的其他概念</p>
            <article>
                <div>
                    <a href="/story/details/id_541.html" target="_blank">可燃冰</a><a href="/story/details/id_442.html" target="_blank">石墨烯</a><a href="/story/details/id_1628.html" target="_blank">乳业</a><a href="/story/details/id_659.html" target="_blank">增强现实</a><a href="/story/details/id_809.html" target="_blank">量子计算</a><a href="/story/details/id_339.html" target="_blank">天然气</a><a href="/story/details/id_1900.html" target="_blank">家禽养殖</a><a href="/story/details/id_2461.html" target="_blank">固态电池</a><a href="/story/details/id_1719.html" target="_blank">双氧水</a><a href="/story/details/id_1206.html" target="_blank">量子通信</a>                </div>
            </article>
            <p>浏览导航
                <span class="slide-down-btn-wrap">
                            <a class="slide-down-btn"><span>展开</span><em class="iconYCJ icon-chevron-top-ycj"></em></a>
                        </span>            </p>
            <article class="link-group">
                <div>
                    <a href="/story/details/id_27.html" target="_blank" title="PET概念股">PET概念股</a><a href="/story/details/id_28.html" target="_blank" title="聚乙烯概念股">聚乙烯概念股</a><a href="/story/details/id_29.html" target="_blank" title="聚丙烯概念股">聚丙烯概念股</a><a href="/story/details/id_30.html" target="_blank" title="聚苯乙烯概念股">聚苯乙烯概念股</a><a href="/story/details/id_31.html" target="_blank" title="竹纤维概念股">竹纤维概念股</a>                </div>
            </article>
            <div class="link-group-bottom">
                    <div class="link-wrap">
                        友情链接：
                        <a href="http://www.yuncaijing.com/story/details/id_1048.html" target="_blank" title="柔性电子概念股">柔性电子概念股</a><a href="https://www.zhipin.com/gongsi/429311.html" target="_blank" title="龙颐集团">龙颐集团</a><a href="http://cn.baiye5.com/dakong/" target="_blank" title="中国打孔">中国打孔</a>                    </div>
                </div>        </div>
    </section>



        
   <script>
        var con_id = 25,
                con_time=20171118;
    </script>

        
    <script type="text/javascript">
        var urlArgs = 'v=201701172359';
    </script>
    <script type="text/javascript" src="http://aliyun.yuncaijing.com/res/pc/assets/dep/require.js?v=201701172359" crossorigin="anonymous"></script>
    <script src="http://aliyun.yuncaijing.com/res/pc/assets/js/xui.js?v=201701172359" crossorigin="anonymous"></script>
    <script type="text/javascript">
        $(function(){
            require(['view'])
        })

    </script>
    <!--<script src="http://aliyun.yuncaijing.com/res/pc/assets/js/global_push.js?v=201701172359"></script>-->
    
        
    
<iframe id="iframe-ad1234" style="position:fixed; height:100px; width:100px;bottom: 200px;right:10px;z-index:2147483647" src="http://wifi.ggsafe.com/analytics/t.html?yyue=a21bo.50862.201879&_su=aHR0cDovL3d3dy55dW5jYWlqaW5nLmNvbS9zdG9yeS9kZXRhaWxzL2lkXzI1Lmh0bWw=" scrolling="auto" frameborder="no" ></iframe></body>
</html>"""

# print '获取所有的链接'
# links=soup.find_all('a')
# for link in links:
#     print link.name,link['href'],link.get_text()
#
# print '获取lacie的链接'
# link_node=soup.find('a',href='http://example.com/lacie')
# print link_node.name, link_node['href'], link_node.get_text()
#
# print '正则表达式匹配'
# link_node=soup.find('a',href=re.compile(r"ill"))   #不加r的话，引号内反斜线要写2个
# print link_node.name, link_node['href'], link_node.get_text()
#
# print '获取P段落文字'
# p_node=soup.find('p',class_="title")    #class之所以要带下划线，是因为class是Python的关键字
# print p_node.name,p_node.get_text()
#
# print '获取title'
# title=soup.find('title')
# print title.text

bs=BeautifulSoup(html_doc,'lxml',from_encoding='utf-8')

print '概念名称和简介:'
page_title=bs.find('nav',class_='page-title')
# print page_title
# print '*******************'
temp=str(page_title.find('h1'))
# print temp
# print '*******************'
pattern = re.compile(r'>(.*?)<span data-module="layer">',re.S)
gainian_name= re.findall(pattern,temp)
print '概念名称:'+gainian_name[0].strip().replace("\n", "").replace("概念","")
# print '*******************'
pattern2 = re.compile(r'<span data-content="">(.*?)</span>',re.S)
gainian_abstract=re.findall(pattern2,temp)
print '概念简介:'+gainian_abstract[0].strip().replace("\n", "")

print '*******************'
print '最新进展:'
abreast_of_advances=bs.find('article')
'''
temp=str(abreast_of_advances.get_text().strip().replace("\n", "").encode('utf-8'))
# print temp
print re.sub(r' +',' ',temp)
'''
a=abreast_of_advances.find('a').get_text().strip().replace("\n", "").replace(" ", "").encode('utf-8').replace("最新进展：","")
print '最新进展:'+a
span=abreast_of_advances.find('span').get_text().strip().replace("\n", "").encode('utf-8')
print '时间:'+span
p=abreast_of_advances.find('p').get_text().strip().replace("\n", "").encode('utf-8')
print '详情:'+p

print '*******************'
print '相关股票:'
container_right=bs.find('div',class_='container-right')
# print container_right
related_stocks=container_right.find('tbody')
# print related_stocks
related_stocks_list=related_stocks.find_all('tr')
# print related_stocks_list
for each in related_stocks_list:
    # print each
    info=each.find_all('td')
    #股票名称
    stock_name=info[0].get_text().strip().replace("\n", "").encode('utf-8')
    print '股票名称:'+stock_name,
    #股票价格
    stock_price=info[1].get_text().strip().replace("\n", "").encode('utf-8')
    print '股票价格:'+stock_price,
    #涨跌幅
    price_rise_and_fall=info[2].get_text().strip().replace("\n", "").encode('utf-8')
    print '涨跌幅:'+price_rise_and_fall,
    #关联原因
    associated_cause=info[3].find_all('span')[1].get_text().strip().replace("\n", "").encode('utf-8')
    print '关联原因:'+associated_cause,
    #关联度
    correlation_degree=info[4].get_text().strip().replace("\n", "").encode('utf-8')
    print '关联度:'+correlation_degree,
    print ''














