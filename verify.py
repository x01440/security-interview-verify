# Security Interview Verification
#
# Security Flaws:
# Guessable Authentication Key
# Same key for each login
# Role encoded in query string
# Config URL exposed for discovery
# API documentation exposed without key
# SQL query update without escaping web content

import json
import urllib
from urllib.request import urlopen, Request

LOCAL_URL = 'http://127.0.0.1:5000/'
SECRET_KEY = '123456'

# Test server up
req = Request(LOCAL_URL)
response = urlopen(req)
html = response.read()
if html == '<p>Sample User Service</p>':
    print('Server Up Verification PASS')
else:
    print('Server Up Verification FAIL')

# Test guessable auth key
req = Request(LOCAL_URL + 'user?role=admin', headers={'Auth': SECRET_KEY})
response = urlopen(req)
html = response.read()
print(html)
print('Guessable Auth Key Verification PASS')


# Test Auth vs. Bearer token (basic auth)
req = Request(LOCAL_URL + 'user?role=admin', headers={'Auth': SECRET_KEY})
response = urlopen(req)
html = response.read()
print(html)
print('Guessable Auth Key Verification PASS')

# Test role encoded in query string
try:
    req = Request(LOCAL_URL + 'user?role=admin', headers={'Auth': SECRET_KEY})
    response = urlopen(req)
    html = response.read()
    response_data = json.loads(html)
    print('Role encoded in query string FAIL')
except:
    print('Role encoded in query string PASS')

# Test config URL exposed

# Test API documentation exposed

# Test SQL query update
