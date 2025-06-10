# Eileen Hwang
# hwangem@uci.edu
# 64501698

import urllib
import urllib.request
import bookmark_connection as bmc
from bookmark_connection import BookmarkProtocol

"""
The following code snippets can be used to help you prepare your test function:
The url to use for testing.
Be sure to run bookmark_server.py before making requests!

url = 'http://localhost:8000'

The format to use for your request data.
Don't forget to encode before sending a request!

json = {'data':bmc.BookmarkProtocol.format(
                                BookmarkProtocol(BookmarkProtocol.ADD, data))}
"""

def http_api_test(data):
    # TODO: write your http connection code here. You can use the above snippets to help
    #url = 'https://www.youtube.com/'
    #parsed_url = urllib.parse.urlparse(url) #hostname, scheme, path
    #info = urllib.parse.urlencode()
    port = 'http://localhost:8000'
    json = {'data':bmc.BookmarkProtocol.format(
                                BookmarkProtocol(BookmarkProtocol.ADD, data))}
    #print(json)
    headers = {'content-type':'application/json'} #copied from slides (double check)
    data = urllib.parse.urlencode(json)
    data = data.encode('utf-8')
    #print(data)
    request = urllib.request.Request(port, data, headers)
    response = urllib.request.urlopen(request) #open the url and perform the request 
    #response = urllib.request.urlopen(url, request.data, request.headers)
    resp_data = response.read()
    response.close()
    print(resp_data)

if __name__ == '__main__':
    # TODO: call your test code from here. You might try writing a few different url tests.
    http_api_test('https://www.youtube.com/')
    http_api_test('https://www.google.com/')
    http_api_test('https://accounts.google.com/b/0/AddMailService')
