#!/usr/bin/python
# encoding: utf-8

import sys

def save_url_db(url):
    lines = {}
    with open('url_db.txt') as reader:
        lines = list(reader.read().splitlines())
        if url not in lines:
            lines.append(url)

    with open('url_db.txt', 'w') as writer:
        writer.writelines("%s\n" % line for line in lines)

if __name__ == '__main__':
    save_url_db(sys.argv[1])
