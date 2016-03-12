"""
Execute from develop branch
"""
from __future__ import with_statement
from fabric.api import *
from fabric.colors import *

@hosts('seb@vm010865.massey.ac.nz', 'seb@vm010944.massey.ac.nz') # only for deploy
def deploy():
    """ Pulls in changes on remotes. """
    base_dir = '/webapps/seb_django/www'
    submodule = 'courses/bioinf-workshop'

    puts(yellow("[Activate env]"))
    run('source ~/bin/activate')
    
    with settings(warn_only=True):
        if run("test -d %s/%s" %(base_dir, submodule)).failed:
            puts(red("[Submodule does not exist: %s]"%submodule))
            with cd(base_dir):
                run("git submodule add git@github.com:sschmeier/bioinf-workshop.git %s" %(submodule))
                run("git submodule init")
 
    puts(yellow("[Update submodule: %s]"%submodule))
    with cd(base_dir):
        run("git submodule update --remote --merge %s"%submodule)

def deploy_local(dir='~/Dropbox/Public', repo='bioinf-workshop', name='bioinf-workshop'):
    with settings(warn_only=True):
        if local("test -d %s/%s" %(dir, name)).failed:
            puts(red("[Repo does not exist in %s/%s: %s]"%(dir, name, repo)))
            puts(yellow("[Cloning repo into %s/%s: %s]"%(dir, name, repo)))
            with lcd(dir):
                local('git clone git@github.com:sschmeier/%s.git %s'%(repo,name))
        else:
            puts(yellow("[Pulling newest changes into %s/%s: %s]"%(dir, name, repo)))
            with lcd(dir):
                local("git -C %s pull"%(name)) 
        
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
