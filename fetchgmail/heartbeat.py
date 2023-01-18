import urllib.request
import sys

url=sys.argv[1]
fp = urllib.request.urlopen(url)
mybytes = fp.read()
fp.close()