#code2040 fellows application

import json, requests, datetime, iso8601
from datetime import timedelta
     
def main(token: str):

    github = 'https://github.com/jdrobinson707/hello-jarod'
    
    #--------------------
    #Step 1: Registration
    #--------------------
    
    payload = { 'token': token,
                'github': github } 

    # creates Response obj by sending correct data as json to given endpoint    
    r = requests.post('http://challenge.code2040.org/api/register', json=payload)
    print(r.text)

    #-------------------------
    #Step II: Reverse a string
    #-------------------------

    
    r = requests.post('http://challenge.code2040.org/api/reverse', data = {'token': token })
    
    payload = { 'token': token,
                'string': r.text[::-1] } # reverses string received from r
    
    r = requests.post('http://challenge.code2040.org/api/reverse/validate', json = payload)
    print(r.text)

    #------------------------------
    #Step III: Needle in a Haystack
    #------------------------------
    
    r = requests.post('http://challenge.code2040.org/api/haystack', data = {'token': token} )

    _dict = r.json() # returns r data as dictionary

    needle = _dict['needle']
    haystack = _dict['haystack'] 
    
    payload = { 'token': token,
                'needle': haystack.index(needle) } # returns index of the needle in the haystack
    
    r = requests.post('http://challenge.code2040.org/api/haystack/validate', json = payload)
    print(r.text)

    #------------------------------
    #Step IV: Prefix
    #------------------------------

    r = requests.post('http://challenge.code2040.org/api/prefix/', data = {'token': token} )

    _list = []
    _dict = r.json()
    
    prefix = _dict['prefix'] 
    word_list = _dict['array'] 

    for word in word_list:
        # if word begins with given string add it to _list
        if not word.startswith(prefix):
            _list.append(word)
    
    payload = { 'token': token,
                'array': _list }
    
    r = requests.post('http://challenge.code2040.org/api/prefix/validate', json = payload)
    print(r.text)
    
    #------------------------------
    #Step V: The dating game
    #------------------------------

    r = requests.post('http://challenge.code2040.org/api/dating', data = {'token': token} )
    
    _dict = r.json()
    
    initial_time = iso8601.parse_date(_dict['datestamp']) # parse given string into iso8601 format
    
    # parse given int into timedelta object that can be added to initial_time
    interval = timedelta(seconds = int(_dict['interval']))
    
    final_time = initial_time + interval 
    
    payload = { 'token': token,
                'datestamp': final_time.isoformat().replace("+00:00", "Z")} # format date into string for serializability
    
    r = requests.post('http://challenge.code2040.org/api/dating/validate', json = payload)
    print(r.text)

    

main('66d5f9f688c97246594893b381490a59')
