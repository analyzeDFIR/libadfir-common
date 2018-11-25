## -*- coding: UTF-8 -*-
## config.py
##
## Copyright (c) 2018 analyzeDFIR
## 
## Permission is hereby granted, free of charge, to any person obtaining a copy
## of this software and associated documentation files (the "Software"), to deal
## in the Software without restriction, including without limitation the rights
## to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
## copies of the Software, and to permit persons to whom the Software is
## furnished to do so, subject to the following conditions:
## 
## The above copyright notice and this permission notice shall be included in all
## copies or substantial portions of the Software.
## 
## THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
## IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
## FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
## AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
## LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
## OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
## SOFTWARE.

import sys
from os import path
from datetime import datetime
import logging

LOGGING_DEFAULTS = dict(\
    format='%(asctime)s.%(msecs)s\t%(levelname)s\t%(name)s\t%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.INFO\
)

def initialize_paths():
    '''
    Args:
        N/A
    Procedure:
        Initialize sys.path to include the lib directory of dependencies.  Raises
        exception if unable to successfully append to sys.path, for example if sys.arv[0]
        is not a valid path.
    Preconditions:
        N/A
    '''
    try:
        runpath = path.abspath(path.dirname(sys.argv[0]))
        assert path.exists(runpath), 'Run path %s does not exist'%runpath
    except Exception as e:
        raise Exception('Unable to append lib directory to path (%s)'%str(e))
    else:
        try:
            sys.path.append(path.join(runpath))          # add runpath so 'from src.<module> import <object>' doesn't fail
            sys.path.append(path.join(runpath, 'lib'))   # add lib for dependencies not pip-installed
        except Exception as e:
            raise Exception('Unable to append lib directory to path (%s)'%str(e))
