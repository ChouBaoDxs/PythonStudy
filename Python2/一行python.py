# -*- coding: UTF-8 -*-

#判断一个字符串中是否存在某些词,代码如下：
wordlist = ["scala", "akka", "play framework", "sbt", "typesafe"]
tweet = "This is an example tweet talking about scala and sbt"
print map(lambda x: x in tweet.split(),wordlist)
















