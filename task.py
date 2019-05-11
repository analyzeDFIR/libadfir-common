## -*- coding: UTF-8 -*-
## task.py
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

from typing import Optional, Dict, Any

from enum import Enum

from .patterns import Container

class TaskStatus(Enum):
    '''
    Enum representing whether a task was:
        1) Successful
        2) Partially successful (encountered error after making some progress)
        3) Unsuccessful (failed)
    '''
    SUCCESS         = 0
    PARTIAL_SUCCESS = 1
    FAILURE         = 2

class TaskResult(object):
    '''
    Container for the result from running a task.  The status attribute
    contains a TaskStatus enum value signaling if the task was successful,
    and the state attribute is a dictionary of data returned from running
    the task.  The state data could be used, for example, to pass data
    from task to another in a pipeline-like fashion.
    '''
    def __init__(self, 
        status: Optional[TaskStatus] = None, 
        state: Optional[Container[str, Any]] = None
    ) -> None:
        self.status = status
        self.state = state
    @property
    def status(self) -> Optional[TaskStatus]:
        '''
        Getter for status
        '''
        return self.__status
    @status.setter
    def status(self, value: Optional[TaskStatus]) -> None:
        '''
        Setter for status
        '''
        self.__status = value
    @property
    def state(self) -> Optional[Container[str, Any]]:
        '''
        Getter for state
        '''
        return self.__state
    @state.setter
    def state(self, value: Optional[Container[str, Any]]) -> None:
        '''
        Setter for state
        '''
        self.__state = value

class BaseTask(object):
    '''
    Abstract task class, can be used for any kind of task
    that involves some setup steps, a main set or loop,
    and some teardown steps.  The term 'task' is used
    loosely here, and this class is purposefully flexible
    in order to serve many different use cases.
    '''
    def __init__(self, result: Optional[TaskResult] = None) -> None:
        self.result = result
    @property
    def result(self) -> Optional[TaskResult]:
        '''
        Getter for result
        '''
        return self.__result
    @result.setter
    def result(self, value: Optional[TaskResult]) -> None:
        '''
        Setter for result
        '''
        self.__result = value
    def __call__(self) -> Optional[TaskResult]:
        '''
        @BaseTask.run
        '''
        return self.run()
    def _preamble(self) -> None:
        '''
        Args:
            N/A
        Procedure:
            Conduct necessary setup steps before the task is processed.
        Preconditions:
            N/A
        '''
        pass
    def _process_task(self) -> None:
        '''
        Args:
            N/A
        Procedure:
            Process this task.
        Preconditions:
            N/A
        '''
        raise NotImplementedError(
            '_process_task is not implemented for type %s'%type(self).__name__
        )
    def _postamble(self) -> None:
        '''
        Args:
            N/A
        Procedure:
            Conduct necessary teardown tasks after task is processed.
        '''
        pass
    def run(self) -> Optional[TaskResult]:
        '''
        Args:
            N/A
        Returns:
            Run this task and return the result.  Subclasses may overload
            this function signature to accept other parameters, though the 
            __call__ function should be updated accordingly.
        Preconditions:
            N/A
        '''
        self._preamble()
        self._process_task()
        self._postamble()
        return self.result
