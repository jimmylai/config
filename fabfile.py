#!/usr/bin/env python
# -*- encoding: utf8 -*-
'''Program
'''


from fabric.api import cd, run, hosts, local, prefix


__author__ = 'noahsark'


VIRTUALENV_PATH = '/home/noahsark/env/bin/activate'


@hosts('localhost')
def vim():
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


@hosts('localhost')
def all():
    vim()
    hg()
    font()
    bash()
    screen()


@hosts('localhost')
def setup_python_package():
    '''Install python packages in VIRTUALENV_PATH by pip.'''
    packages = ['fabric', 'nose', 'coverage', 'ipython', 'pylint']
    for pkg in packages:
        with prefix('. %s' % VIRTUALENV_PATH):
            run('pip install %s' % pkg)
