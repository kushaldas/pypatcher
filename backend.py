#!/usr/bin/env python
import os
import requests


def main():
    q = Queue("bug-messages")
    q.connect()
    while True:
        t = q.wait()
        text = t.data
        data = text.split('/')[-1]
        if data.startswith(u'issue'):
            bugid = data[5]
            print "Got: %s" % bugid

if __name__ == '__main__':
    main()
