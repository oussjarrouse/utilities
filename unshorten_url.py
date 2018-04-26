import sys

from urllib.parse import urlparse
from http.client import HTTPConnection

def unshorten(url):
    try:
        parsed = urlparse(url)
        h = HTTPConnection(parsed.netloc)
        h.request('HEAD', parsed.path)
        response = h.getresponse()
        if response.status//100 == 3 and response.getheader('Location'):
            return response.getheader('Location')
        else:
            return url
    except Exception as e:
        print(e)
        return 'X - ' + url

if __name__ == "__main__":
    for line in sys.stdin:
        stripped = line.strip()
        outputLine = unshorten(stripped)
