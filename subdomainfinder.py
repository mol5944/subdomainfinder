import requests
from socket import gethostbyname
from sys import argv
from threading import Thread
from time import sleep

def help():
    print('--domain: Domain name to scan')
    print('--wordlist: List of words to search')
    print('--threads: Threads to scan')
    print('--sleep_thr: Waiting between threads')
    print('--output: Output file')
    quit()

def save(file_name,string):
    with open(file_name,'at') as file:
        file.write(string + '\n')

def generator(string):
    for word in string:
        subdomain = word.replace('\n','')
        yield subdomain

def request(domain,output):
    try:
        ip = gethostbyname(domain)
    except:
        pass
    else:
        bool = False

        try:
            resp_http = requests.get('http://' + domain)
        except:
            pass
        else:
            bool = True

        try:
            resp_https = requests.get('https://' + domain)
        except:
            pass
        else:
            bool = True

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



count_thr = 0

with open(wordlist,'rt') as dictionary:
    for subdomain in generator(dictionary):
        if count_thr == threads:
            sleep(sleep_thr)
            count_thr = 0
        thr = Thread(target=request, args=(subdomain + '.' + domain,output,))
        thr.start()
        count_thr += 1
