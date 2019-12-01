import requests
from socket import gethostbyname
from sys import argv

def help():
    print('--domain (domain name to scan)')
    print('--wordlist (list of words to search)')
    quit()

def generator(string):
    for word in string:
        subdomain = word.replace('\n','')
        yield subdomain

def request(domain):
    try:
        ip = gethostbyname(domain)
    except:
        pass
    else:
        print(domain + "     " + ip)



if '--help' in argv:
    help()

if '--domain' in argv:
    domain = argv[argv.index('--domain') + 1]
else:
    print('****************************************')
    print('specify the argument --domain')
    print('****************************************')
    help()

if '--wordlist' in argv:
    wordlist = argv[argv.index('--wordlist') + 1]
else:
    print('****************************************')
    print('specify the argument --wordlist')
    print('****************************************')
    help()






with open(wordlist,'rt') as dictionary:
    for subdomain in generator(dictionary):
        request(subdomain + '.' + domain)
