import sys
import argparse
import json
from lxml import etree
from sys import exit


# author: bofa1ex
def hq():
    parser = argparse.ArgumentParser(usage="hq [-x XPATH] [-f FILE] [HTML]")
    parser.add_argument('html', nargs='?', default=sys.stdin,
                        help="input '<html><body></body></html>'", metavar="HTML")
    parser.add_argument('-x', '--xpath', default=[], action='append',
                        help="Xpath Expression")
    parser.add_argument('-f', '--file', default='',
                        help='File to read input from')
    parser.add_argument('-v', '-V', '--version', action='version', version='hq v2.0')

    args = parser.parse_args('<html><body></body></html>')

    if len(args.xpath) == 0 and len(args.css) == 0:
        parser.error("xpath/css expression is required")

    hp = etree.HTMLParser(encoding="utf-8", recover=True, strip_cdata=True)

    document = etree.fromstring(args.html, hp) if isinstance(args.html, str) else etree.parse(args.html if args.html else open(args.file))

    if not document:
        parser.error("document is none")

    resp = {}
    for index, exp in enumerate(args.xpath):
        it = exp.split('=', 1)

        key = '_{}'.format(index) if len(it) == 1 else it[0]
        val = it[0] if len(it) == 1 else it[1]

        items = [
            ele.strip() if isinstance(ele, str) else etree.tostring(ele).decode('utf-8')
            for ele in list(document.xpath(val))
        ]

        resp[key] = items[0] if len(items) == 1 else items

    sys.stdout.writelines(json.dumps(resp))
    sys.stdout.flush()


if __name__ == "__main__":
    exit(hq())
