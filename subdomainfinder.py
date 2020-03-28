import requests
from socket import gethostbyname
from sys import argv
from threading import Thread
from time import sleep

find_ip = list()

def help():
    print('--domain: Domain name to scan')
    print('--wordlist: List of words to search')
    print('--threads: Threads to scan')
    print('--sleep_thr: Waiting between threads')
    print('--output: Output file')
    print('--Ing_the_s_ip: Ignore the same ip')
    quit()

def save(file_name,string):
    with open(file_name,'at') as file:
        file.write(string + '\n')

def generator(string):
    for word in string:
        subdomain = word.replace('\n','')
        yield subdomain

def request(domain,output,Ing_the_s_ip):
    try:
        ip = gethostbyname(domain)
        if ip not in find_ip:
            find_ip.append(ip)
            old_ip = True
        else:
            old_ip = False
    except:
        pass
    else:
        bool = False

        try:
            resp_http = requests.get('http://' + domain)
        except:
            pass
        else:
            if resp_http.status_code != 404:
                if Ing_the_s_ip == True and old_ip == True:
                    bool = True
                if Ing_the_s_ip == False:
                    bool = True

        try:
            resp_https = requests.get('https://' + domain)
        except:
            pass
        else:
            if resp_https.status_code != 404:
                if Ing_the_s_ip == True and old_ip == True:
                    bool = True
                if Ing_the_s_ip == False:
                    bool = True
        if bool:
            print(domain + "     " + ip)
            if output != None:
                save(output,domain + "     " + ip)



if '--help' in argv:
    help()

if '--domain' in argv:
    domain = argv[argv.index('--domain') + 1]
else:
    print('****************************************')
    print('Specify the argument --domain')
    print('****************************************')
    help()

if '--wordlist' in argv:
    wordlist = argv[argv.index('--wordlist') + 1]
else:
    print('****************************************')
    print('Specify the argument --wordlist')
    print('****************************************')
    help()

if '--threads' in argv:
    threads = int(argv[argv.index('--threads') + 1])
else:
    threads = 1

if '--sleep_thr' in argv:
    sleep_thr = int(argv[argv.index('--sleep_thr') + 1])
else:
    sleep_thr = 0

if '--output' in argv:
    output = argv[argv.index('--output') +1]
else:
    output = None

if '--Ing_the_s_ip' in argv:
    Ing_the_s_ip = True
else:
    Ing_the_s_ip = False


count_thr = 0

with open(wordlist,'rt') as dictionary:
    for subdomain in generator(dictionary):
        if count_thr == threads:
            sleep(sleep_thr)
            count_thr = 0
        thr = Thread(target=request, args=(subdomain + '.' + domain,output,Ing_the_s_ip,))
        thr.start()
        count_thr += 1
