#!/usr/bin/python
# encoding: utf-8

import sys
import json
from full import main as full_main

query = sys.argv[1:]
items = []

def load_db():
    with open('url_db.txt') as reader:
        urls = reader.read().splitlines()
        return reversed(urls)

def search(port):
    items = []
    with open('url_db.txt') as reader:
        urls = reader.read().splitlines()
        for url in urls:
            if 'http://localhost:%s' % port in url:
                items.append(url)
    return items

def construct_response_item(url):
    # docs: https://www.alfredapp.com/help/workflows/inputs/script-filter/json/ 
    return {
        "title": url,
        "arg": url
    }

def main():
    if len(query) > 0:
        port = query[0]
        if port.startswith('//'):
            # port is full url
            full_main(port)
        else:
            items.append(construct_response_item('http://localhost:%s' % port))

            # Search for port
            urls = search(port)
            [items.append(construct_response_item(url)) for url in urls]

            response = json.dumps({
                "items": items
            })
            sys.stdout.write(response)
    else:
        # Load urls from `url_db.txt`
        urls = load_db()
        [items.append(construct_response_item(url)) for url in urls]

        response = json.dumps({
            "items": items
        })
        sys.stdout.write(response)

main()
