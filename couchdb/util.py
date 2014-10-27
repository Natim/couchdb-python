import sys

if sys.version_info[0] < 3:
    from couchdb.util2 import *  # NOQA
else:
    from couchdb.util3 import *  # NOQA


def pyexec(code, gns, lns):
    # http://bugs.python.org/issue21591
    exec(code, gns, lns)
