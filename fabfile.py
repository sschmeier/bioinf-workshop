"""
Execute from develop branch
"""
from __future__ import with_statement
from fabric.api import *
from fabric.colors import *
from fabric.contrib.console import confirm

@hosts('seb@vm010865', 'seb@vm010944') # only for deploy
def deploy():
    """ Pulls in changes on remotes. """
    base_dir = '/webapps/seb_django/www'
    submodule = 'courses/bioinf-workshop'
    
    with settings(warn_only=True):
        if run("test -d %s/%s" %(base_dir, submodule)).failed:
            puts(red("[Submodule does not exist: %s]"%submodule))
            with cd(base_dir):
                run("git submodule add git@github.com:sschmeier/bioinf-workshop.git %s" %(submodule))
                run("git submodule init")

    puts(yellow("[Activate env]"))
    run('source ~/bin/activate')

    puts(yellow("[Update submodule: %s]"%submodule))
    with cd(base_dir):
        run("git submodule update --remote --merge %s"%submodule)

def deploy_dp():
    local("git -C ~/Dropbox/Public/bioinf-workshop pull")
        
def git(branch="develop", version=None):
    """
    branch: the branch that should be merged into master.
    """
    local("git add -u && git commit")
    local("git co master")
    local("git merge %s --no-ff" %branch)
    with settings(warn_only=True):
        if version:
            local('git tag -a %s'%version)
    local("git push")
    local("git co gh-pages")
    local("git merge master")
    local("git push origin gh-pages")
    local("git co develop")
