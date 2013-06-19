#!/usr/bin/env python
# -*- encoding: utf8 -*-
'''Program
'''


from fabric.api import cd, run, hosts, local, prefix
import os


__author__ = 'noahsark'


VIRTUALENV_PATH = '~/env/bin/activate'


@hosts('localhost')
def vim():
    local('cp .bash_profile ~/')
    local('cp .vimrc ~/')
    local('cp .vim ~/ -r')


@hosts('localhost')
def hg():
    local('cp .hgrc ~/')


@hosts('localhost')
def git():
    local('cp .gitconfig ~/')


@hosts('localhost')
def font():
    dir_path = '/usr/share/fonts/truetype'
    if not os.path.isdir(dir_path):
        local('sudo mkdir %s' % dir_path)

    local('sudo cp truetype/*.ttf %s' % dir_path)
    local('fc-cache -fv')


@hosts('localhost')
def bash():
    local('cat .bashrc >> ~/.bashrc')
    local('cp .inputrc ~/')


@hosts('localhost')
def screen():
    local('cp .screenrc ~/')
    local('cp .tmux.conf ~/')


@hosts('localhost')
def setup():
    vim()
    hg()
    #font()
    bash()
    screen()
    git()


@hosts('localhost')
def setup_python_package():
    '''Install python packages in VIRTUALENV_PATH by pip.'''
    packages = ['fabric', 'nose', 'coverage', 'ipython', 'pylint']
    for pkg in packages:
        with prefix('. %s' % VIRTUALENV_PATH):
            local('pip install %s' % pkg)
