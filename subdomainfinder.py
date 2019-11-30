import requests
from socket import gethostbyname

domain = input('domain: ')
wordlist = input('wordlist: ')
protocol = input('protocol: ')

def generator(string):
    for word in string:
        subdomain = word.replace('\n','')
        yield subdomain

def request(domain,protocol):
    try:
        requests.get(protocol + domain)
    except:
        pass
    else:
        print(domain + "     " + gethostbyname(domain))

with open(wordlist,'rt') as dictionary:
    for subdomain in generator(dictionary):
        request(subdomain + '.' + domain,protocol)
