#!/usr/bin/python
# encoding: utf-8

import sys
from workflow import Workflow


def main(wf):
    # Get args from Workflow, already in normalized Unicode.
    # This is also necessary for "magic" arguments to work.
    args = wf.args

    # Add an item to Alfred feedback
    if len(args):
        port = args[0]
        wf.add_item(title='http://localhost:%s' % port, arg='http://localhost:%s' % port, valid=True)

        # Search for port
        results = search(port)
        [wf.add_item(title=line, arg=line, valid=True) for line in results]
    else:
        # Load urls from `url_db.txt`
        load_file(wf)

    # Send output to Alfred. You can only call this once.
    # Well, you *can* call it multiple times, but subsequent calls
    # are ignored (otherwise the JSON sent to Alfred would be invalid).
    wf.send_feedback()

def load_file(wf):
    with open('url_db.txt') as reader:
        lines = reader.read().splitlines()
        for line in reversed(lines):
            wf.add_item(title=line, arg=line, valid=True)

def search(port):
    results = []
    with open('url_db.txt') as reader:
        lines = reader.read().splitlines()
        for line in lines:
            if 'http://localhost:%s' % port in line:
                results.append(line)
    return results

if __name__ == '__main__':
    # Create a global `Workflow` object
    wf = Workflow()
    # Call your entry function via `Workflow.run()` to enable its
    # helper functions, like exception catching, ARGV normalization,
    # magic arguments etc.
    sys.exit(wf.run(main))
