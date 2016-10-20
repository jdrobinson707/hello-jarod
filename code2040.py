#code2040 fellows application

import json, requests
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2

def main():
    #--------------------
    #Step 1: Registration
    #--------------------
    github = 'https://github.com/jdrobinson707/hello-jarod'
    url = 'http://challenge.code2040.org/api/register'
    token = '66d5f9f688c97246594893b381490a59'
    data = { 'github': github, 'token': token }
    headers = {'Content-type': 'application/json'}

    try:
        response = requests.post(url, data=json.dumps(data), headers=headers)
    except requests.ConnectionError:
        sys.exit()
main()

