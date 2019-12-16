import re
import sys
import pyperclip
from config import LINK_TEMPLATE as LT
from config import DOMAIN

def wrap_link(link):
    return "[📃]({})".format(handle_link(link))


def handle_link(link):
    if link[-1] != '/':
        link += '/'
    link = re.sub(r':', '%3A', link)
    link = re.sub(r'/', '%2F', link)
    return LT.format(link)


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
    link = wrap_link(raw)
    print(link)
    pyperclip.copy(link)


if __name__ == "__main__":
    main()
