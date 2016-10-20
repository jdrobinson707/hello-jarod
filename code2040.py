#code2040 fellows application

import json, requests
     
def main():
    #--------------------
    #Step 1: Registration
    #--------------------
    github = 'https://github.com/jdrobinson707/hello-jarod'
    url = 'http://challenge.code2040.org/api/register'
    token = '66d5f9f688c97246594893b381490a59'
    payload = { token: '66d5f9f688c97246594893b381490a59',
             github: 'https://github.com/jdrobinson707/hello-jarod }
    requests.post(url, data=json.dumps(payload))

main()


