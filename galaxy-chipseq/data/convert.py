#!/usr/bin/env python
"""
NAME: xxx
=========

DESCRIPTION
===========

INSTALLATION
============

USAGE
=====

VERSION HISTORY
===============

0.1.0   xxxx/xx/xx    Initial version.


template version: 1.0 (2015/08/27)
"""
__version__='0.1.0'
__date__='xxxx/xx/xx'
__email__='s.schmeier@gmail.com'
__author__='Sebastian Schmeier'
import sys, os, os.path, argparse, csv, collections, gzip, bz2, zipfile, time
## import pandas as pd ## non standard library to be imported

# When piping stdout into head python raises an exception
# Ignore SIG_PIPE and don't throw exceptions on it...
# (http://docs.python.org/library/signal.html)
from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE,SIG_DFL)

def parse_cmdline():
    
    ## parse cmd-line -----------------------------------------------------------
    sDescription = 'Read delimited file.' 
    sVersion='version %s, date %s' %(__version__,__date__)
    sEpilog = 'Copyright %s (%s)' %(__author__, __email__)

    oParser = argparse.ArgumentParser(description=sDescription,
                                      version=sVersion,
                                      epilog=sEpilog)
    oParser.add_argument('sFile',
                         metavar='FILE',
                         help='Delimited file. [if set to "-" or "stdin" reads from standard in]')
    oParser.add_argument('-a', '--header',
                         dest='bHead',
                         action='store_true',
                         default=False,
                         help='Header in File. [default: False]')
    oParser.add_argument('-d', '--delimiter',
                         metavar='STRING',
                         dest='sDEL',
                         default='\t',
                         help='Delimiter used in file.  [default: "tab"]')
    oParser.add_argument('-f', '--field',
                         metavar='INT',
                         type=int,
                         dest='sFIELD',
                         default=1,
                         help='Field / Column in file to use.  [default: 1]')
    oParser.add_argument('-o', '--out',
                         metavar='STRING',
                         dest='sOut',
                         default=None,
                         help='Out-file. [default: "stdout"]')
    
    # PANDAS
    ## oParser.add_argument('-l', '--labels', 
    ##                      dest='iLabel',
    ##                      metavar="INT",
    ##                      type=int,
    ##                      default=None,
    ##                      help='Column number to use as labels. [default: None]')
    # FOR CONFIG-FILE PARSING
    ## oParser.add_argument('--config',
    ##                      dest = 'sConfig',
    ##                      metavar='CONFIG-FILE',
    ##                      default='config.ini',
    ##                      help='Config-file to read. [default: config.ini]')
    
    group1 = oParser.add_argument_group('Threading', 'Multithreading arguments:')
  
    group1.add_argument('-p', '--processes',
                         metavar='INT',
                         type=int,
                         dest='iP',
                         default=1,
                         help='Number of sub-processes (workers) to use. It is only logical to not give more processes than cpus/cores are available. [default: 1]')
    group1.add_argument('-t', '--time',
                         action='store_true',
                         dest='bTIME',
                         default=False,
                         help='Time the runtime and print to stderr. [default: False]')
    
    
    oArgs = oParser.parse_args()
    return oArgs, oParser

def load_file(s):
    """ LOADING FILES """
    if s in ['-', 'stdin']:
        oF = sys.stdin
    elif s.split('.')[-1] == 'gz':
        oF = gzip.open(s)
    elif s.split('.')[-1] == 'bz2':
        oF = bz2.BZFile(s)
    elif s.split('.')[-1] == 'zip':
        oF = zipfile.Zipfile(s)
    else:
        oF = open(s)
    return oF

def my_func(args):
    """
    THIS IS THE ACCTUAL WORKFUNCTION THAT HAS TO BE EXECUTED MULTPLE TIMES.
    This funion will be distributed to the cores requested.
    # do stuff
    res = ...
    return (args, res)
    """
    # Do stuff and create result
    # EXAMPLE: Here we add up arg1 and arg2 and wait a bit.
    res = args[0] + args[1]
    time.sleep(0.2)
    return (args, res)

def main():
    oArgs, oParser = parse_cmdline()

    # get field number to use in infile
    iF = oArgs.sFIELD - 1
    if iF < 0: oParser.error('Field -f has to be an integer > 0. EXIT.')
        
    oF = load_file(oArgs.sFile)

    if not oArgs.sOut:
        oFout = sys.stdout
    elif oArgs.sOut in ['-', 'stdout']:
        oFout = sys.stdout
    elif oArgs.sOut.split('.')[-1] == 'gz':
        oFout = gzip.open(oArgs.sOut, 'wb')
    else:
        oFout = open(oArgs.sOut, 'w')
        
    # -------------------------------------------------------
    # USING a config parser
    # Read config file if it exists
    # e.g.
    # [Classes]
    # c1 = 1
    # c2 = 3
    ## from ConfigParser import SafeConfigParser  
    ## dParams = {}
    ## if os.path.isfile(oArgs.sConfig):
    ##     oConfigParser = SafeConfigParser()
    ##     oConfigParser.read(oArgs.sConfig)
    ##     for section_name in oConfigParser.sections():
    ##         for name, value in oConfigParser.items(section_name):
    ##             dParams[name] = value                   
    # -------------------------------------------------------

    # ------------------------------------------------------
    # PANDAS approach
    # Check labels
    ## if oArgs.iLabel:
    ##     if oArgs.iLabel <= 0:
    ##         oParser.error('Label column number has to be > 0. EXIT.')
    ##     iLabel = oArgs.iLabel - 1
    ## else:
    ##     iLabel = False
    ## oDF = pd.read_csv(oF, sep=oArgs.sDEL, header=header, index_col=iLabel)
    # ------------------------------------------------------
   

   
    oR = csv.reader(oF, delimiter = oArgs.sDEL)
    if oArgs.bHead:
        aH = oR.next()

    d = collections.OrderedDict()
    for a in oR:
        aF = []
        for s in a:
            if len(s)>0:
                aF.append(s)

        
        if len(aF)>5:
            tR = (aF[0],aF[6],aF[7],aF[10],aF[3])
            
            
        else:
            tR=(aF[0],aF[2],aF[3],aF[4],aF[1])

        d[tR] = None

    for t in d:
        oFout.write('%s\t%s\t%s\t%s\t1\t%s\n'%(t))
        
       
    oF.close()
            
    
    oFout.close()
   
    return
        
if __name__ == '__main__':
    sys.exit(main())


