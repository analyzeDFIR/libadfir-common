## -*- coding: UTF-8 -*-
## task.py
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

class TaskResult(object):
    '''
    Class used to hold the resulting state of running
    a task
    '''
    def __init__(self, state=None):
        self.state = state
    @property
    def state(self):
        '''
        Getter for state
        '''
        return self.__state
    @state.setter
    def state(self, value):
        '''
        Setter for state
        '''
        assert value is None or isinstance(value, dict)
        self.__state = value

class BaseTask(object):
    '''
    Abstract class for creating tasks
    '''
    def __init__(self, *args, **kwargs):
        self.__result = None
    @property
    def result(self):
        '''
        Getter for result
        '''
        return self.__result
    @result.setter
    def result(self, value):
        '''
        Setter for result
        '''
        assert isinstance(value, TaskResult)
        self.__result = value
    def __call__(self):
        '''
        @BaseTask.run
        '''
        return self.run()
    def _preamble(self):
        '''
        Args:
            N/A
        Procedure:
            Conduct necessary setup steps before the task is processed
        Preconditions:
            N/A
        '''
        pass
    def _process_task(self):
        '''
        Args:
            N/A
        Procedure:
            Process this task
        Preconditions:
            N/A
        '''
        raise NotImplementedError('_process_task is not implemented for type %s'%type(self).__name__)
    def _postamble(self):
        '''
        Args:
            N/A
        Procedure:
            Conduct necessary teardown tasks after task is processed
        '''
        pass
    def run(self):
        '''
        Args:
            N/A
        Returns:
            TaskResult
            Result from running this task
        Preconditions:
            N/A
        '''
        self._preamble()
        self._process_task()
        self._postamble()
        return self.result
