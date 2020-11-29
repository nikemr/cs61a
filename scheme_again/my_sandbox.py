"""A Scheme interpreter and its read-eval-print loop."""
from __future__ import print_function  # Python 2 compatibility

import sys
import os

from scheme_builtins import *
from scheme_reader import *
from ucb import main, trace

def apply(args):

    python_args = []
    # BEGIN PROBLEM 3
    idx=0
    ctl=len(args)
    while 
        python_args.append(args.first)
        args=args.rest
        idx+=1
        
        print(python_args)
    print(python_args)
    

    
       
twos = Pair(2, Pair(3, nil))

apply(twos)