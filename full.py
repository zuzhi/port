#!/usr/bin/env python3

import sys
import json

query = sys.argv[1:]
items = []

def load_db():
    with open('url_db.txt') as reader:
        urls = reader.read().splitlines()
        return reversed(urls)

def search(input_url):
    items = []
    with open('url_db.txt') as reader:
        urls = reader.read().splitlines()
        for url in urls:
            if url.startswith('http://localhost'):
                continue
            if 'http:%s' % input_url in url:
                items.append(url)
    return items

def construct_response_item(url):
    # docs: https://www.alfredapp.com/help/workflows/inputs/script-filter/json/
    return {
        "title": url,
        "arg": url
    }

def main(input_url):
    if input_url:
        items.append(construct_response_item('http:%s' % input_url))

        # Search for input_url
        urls = search(input_url)
        [items.append(construct_response_item(url)) for url in urls]
    else:
        # Load urls from `url_db.txt`
        urls = load_db()
        [items.append(construct_response_item(url)) for url in urls]

    response = json.dumps({
        "items": items
    })

    sys.stdout.write(response)
