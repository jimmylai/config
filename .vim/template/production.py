#!/usr/bin/env python
# -*- encoding: utf8 -*-
'''Program
'''

import sys
import optparse


__author__ = 'noahsark'


def main(args):
    '''\
    %prog [options]
    '''
    return 0


if __name__ == '__main__':
    PARSER = optparse.OptionParser(usage=main.__doc__)
    OPTIONS, ARGS = PARSER.parse_args()

    if len(ARGS) != 0:
        PARSER.print_help()
        sys.exit(1)

    sys.exit(main(ARGS))

