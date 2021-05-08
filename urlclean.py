#!/bin/python3
import urllib.parse
import re
import sys


r_url=sys.argv[1]
raw_url=re.findall("=http.*?&",r_url)
encoded_url=raw_url[0].translate({ord(i): None for i in '&='})
a=urllib.parse.unquote(encoded_url)
print(a)
