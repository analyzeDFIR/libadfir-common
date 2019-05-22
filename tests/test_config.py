## -*- coding: UTF-8 -*-
## test_config.py
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

from unittest import TestCase
import sys
from os import path

from ..config import include_dependencies_in_path


class TestConfigIncludeDependenciesInPath(TestCase):
    """Unit tests for include_dependencies_in_path"""

    def setUp(self):
        """Set argv[0] to full path to test file"""
        self.original_argv = sys.argv
        self.original_path = sys.path
        sys.argv[0] = path.abspath(__file__)

    def testNoDirpath(self):
        """dirpath is None"""
        include_dependencies_in_path()
        self.assertEqual(sys.path[-1], path.abspath(path.dirname(__file__)))

    def testProvidedDirpath(self):
        """dirpath is 'lib'"""
        include_dependencies_in_path(path.join(
            path.abspath(path.dirname(__file__)),
            'lib'
        ))
        self.assertEqual(sys.path[-1], path.join(
            path.abspath(path.dirname(__file__)),
            'lib'
        ))

    def tearDown(self):
        """Reset sys.argv to original value"""
        sys.argv = self.original_argv
        sys.path = self.original_path
