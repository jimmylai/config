#!/usr/bin/env python
# -*- encoding: utf8 -*-
'''Program
'''


from fabric.api import cd, run, hosts, local


__author__ = 'noahsark'


@hosts('localhost')
def vim():
    local('cp .vimrc ~/')
    local('cp .vim ~/ -r')


@hosts('localhost')
def hg():
    local('cp .hgrc ~/')


@hosts('localhost')
def font():
    local('sudo cp truetype/*.ttf /usr/share/fonts/truetype')
    local('fc-cache -fv')


@hosts('localhost')
def bash():
    local('cat .bashrc >> ~/.bashrc')
    local('cp .inputrc ~/')


@hosts('localhost')
def screen():
    local('cp .screenrc ~/')
    local('cp .tmux.conf ~/')
