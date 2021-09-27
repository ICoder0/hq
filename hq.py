import sys
import argparse
import json
from lxml import etree
from sys import exit


# author: bofa1ex
# curl http://testapi.cn | hq
# -x title="//["@id=123"]/value()"
# -x link="//["@id=123"]/value()"
# -x "//["@id=123"]/value()" => _0=$it,_1=$it,_2=$it

def hq():
    parser = argparse.ArgumentParser()
    parser.add_argument('html', nargs='?', type=argparse.FileType('rb'),
                        default=sys.stdin, help="HTML", metavar="HTML")
    parser.add_argument('-x', '--xpath', default=[], action='append',
                        help="Xpath Expression")
    parser.add_argument('-c', '--css', default=[], action='append',
                        help='CSS3 Selector Expression')
    parser.add_argument('-f', '--file', default='',
                        help='File to read input from')
    args = parser.parse_args()

    hp = etree.HTMLParser(encoding="utf-8", recover=True, strip_cdata=True)

    inp = open(args.file) if args.file else args.html
    document = etree.parse(inp, hp)

    resp = {}
    for index, exp in enumerate(args.xpath):
        it = exp.split('=', 1)

        key = '_{}'.format(index) if len(it) == 1 else it[0]
        val = it[0] if len(it) == 1 else it[1]

        items = [
            ele if isinstance(ele, str) else etree.tostring(ele).decode('utf-8')
            for ele in list(document.xpath(val))
        ]

        resp[key] = items[0] if len(items) == 1 else items

    sys.stdout.write(json.dumps(resp))
    sys.stdout.flush()


if __name__ == "__main__":
    exit(hq())
