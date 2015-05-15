#!/usr/bin/env python

import os
import tempfile
import sys
import xmlrpclib as cl
rserver = cl.ServerProxy('http://bugs.python.org/xmlrpc', allow_none=True)

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
    os.system('wget http://bugs.python.org/file%s/' % patchid)
    os.system('mv index.html new_patch.patch')
    print("Received the patch.")

if __name__ == '__main__':
    get_latest_patch(sys.argv[1])
