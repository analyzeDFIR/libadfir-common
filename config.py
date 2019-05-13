## -*- coding: UTF-8 -*-
## config.py
##
## Copyright (c) 2019 analyzeDFIR
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

from typing import Optional

import sys
from os import path
from datetime import datetime

LOGGING_DEFAULTS = dict(\
    format='%(asctime)s.%(msecs)s\t%(levelname)s\t%(name)s\t%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=20    # logging.INFO
)

def include_dependencies_in_path(dirpath: Optional[str] = None) -> None:
    '''
    Args:
        dirpath => path to dependency directory
    Procedure:
        Initialize sys.path to include a directory of dependencies.  If dirpath
        is None, includes the launch path of the running python program.  Raises
        exception if unable to successfully append to sys.path, for example if
        dirpath is None and sys.argv[0] is not a valid path.
    Preconditions:
        N/A
    '''
    try:
        if dirpath is None:
            dirpath = path.abspath(path.dirname(sys.argv[0]))
    except Exception as e:
        raise Exception(
            'Unable to append %s directory to sys.path (%s)'%(dirpath, str(e))
        )
    else:
        try:
            sys.path.append(dirpath)
        except Exception as e:
            raise Exception(
                'Unable to append %s directory to sys.path (%s)'%(
                    dirpath, 
                    str(e)
                )
            )
