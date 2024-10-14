import re
from urllib import request


def extract_emails(url):
    html = request.urlopen(url).read().decode('utf8')

    regex = r'*@[\w\-]+(?:[.](?!com)[\w\-]+)+'

    return [x for x in re.findall(regex, html)]


print(extract_emails("url"))
