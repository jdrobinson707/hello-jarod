#code2040 fellows application

import json, requests
     
def main():
    #--------------------
    #Step 1: Registration
    #--------------------
    github = 'https://github.com/jdrobinson707/hello-jarod'
    url = 'http://challenge.code2040.org/api/register'
    token = '66d5f9f688c97246594893b381490a59'
    payload = { 'token': token,
             'github': github }
    r = requests.post(url, json=payload)
    print(r.text)
    

main()


