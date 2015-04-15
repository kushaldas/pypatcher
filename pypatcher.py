#!/usr/bin/env python3.4

import os
import requests
from bs4 import BeautifulSoup
import xmlrpc.client as cl
rserver = cl.ServerProxy('http://bugs.python.org/xmlrpc', allow_none=True)

def parse_mainpage(url='http://bugs.python.org/'):
    """
    Will parse the mainpage and get us a list of bugs.

    :param url: String, url of the main page.
    """
    html = requests.get(url)
    soup = BeautifulSoup(html.text)
    tags1 = soup.find_all('tr', {'class': 'odd'})
    tags2 = soup.find_all('tr', {'class': 'even'})
    return tags1 + tags2

def get_bugids(tags):
    """
    Gets all the bugs with patches
    :param tags: List of bs4 tags
    :return: List of bugids
    """
    bugids  = []
    for data in tags:
        tds = data.findAll('td')
        bugid = tds[0]
        has_patch = tds[3]
        if len(has_patch.contents) > 2:
            datum = str(has_patch.contents[1])
            if datum and datum.find('has patch') > 0:
                bugids.append(bugid.string)
    return bugids

def get_latest_patch(bugid):
    """
    Gets the latest patch for the given bug in the filesystem.
    :param bugid: Bugid in string
    :return: patch filename.
    """
    patchid = None
    data = rserver.display('issue%s' % bugid)
    if len(data['files']) > 0:
        patchid = data['files'][-1]
    patch = requests.get('http://bugs.python.org/file%s/' % patchid)
    patchfile = os.path.join('patches', 'file%s' % patchid)
    patch_text = patch.text
    with open(patchfile, 'w') as fobj:
        fobj.write(patch_text)
    print('Wrote %s' % patchfile)
    return patchfile

if __name__ == '__main__':
    tags = parse_mainpage()
    bugids = get_bugids(tags)
    print(bugids)
    for bug in bugids:
        get_latest_patch(bug)
