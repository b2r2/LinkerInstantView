import re
import sys
import pyperclip
from config import LINK_TEMPLATE as LT
from config import DOMAIN

def wrap_link(url):
    return "[📃]({})".format(handle_link(url))


def handle_link(url):
    if url[-1] != '/':
        url += '/'
    url = re.sub(r':', '%3A', url)
    url = re.sub(r'/', '%2F', url)
    return LT.format(url)


def get_link():
    buf = pyperclip.paste().strip()
    c = re.compile(DOMAIN)
    if len(re.findall(c, buf)) == 1 and len(re.findall("rhash", buf)) == 0:
        return buf
    try:
        link = sys.argv[1]
    except IndexError:
        sys.exit("Usage main.py https://... or copy in the buffer")
    return link.strip()


def main():
    raw = get_link()
    url = wrap_link(raw)
    print(url)
    pyperclip.copy(url)


if __name__ == "__main__":
    main()
