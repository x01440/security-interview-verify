# Security Interview Verification
#
# Security Flaws:
# Guessable Authentication Key
# Same key for each login
# Role encoded in query string
# Config URL exposed for discovery
# API documentation exposed without key
# SQL query update without escaping web content

import urllib

SECRET_KEY = "123456"

# Test server up
with urllib.request.urlopen('http://127.0.0.1/') as response:
   html = response.read()

# Test guessable auth key
with urllib.request.urlopen('http://127.0.0.1/') as response:
   html = response.read()


# Test Auth vs. Bearer token (basic auth)

# Test role encoded in query string

# Test config URL exposed

# Test API documentation exposed

# Test SQL query update
