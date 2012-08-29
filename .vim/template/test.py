#!/usr/bin/env python
# -*- encoding: utf8 -*-
'''Test
'''
from nose import with_setup
import nose.tools as nt


__author__ = 'noahsark'

def setup():
    pass

def teardown():
    pass

@with_setup(setup, teardown)
def test():
    data = ''
    expected = ''
    actual = ''
    nt.assert_equal(actual, expected)
    
