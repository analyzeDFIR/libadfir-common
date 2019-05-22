## -*- coding: UTF-8 -*-
## test_task.py
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

from unittest import TestCase

from ..patterns import Container
from ..task import TaskStatus, TaskResult, BaseTask


class SimpleTask(BaseTask):

    @property
    def previous_task_result(self) -> TaskResult:
        """Getter for previous_task_result"""
        return self.__previous_task_result

    @previous_task_result.setter
    def previous_task_result(self, value: TaskResult) -> None:
        """Setter for previous_task_result"""
        self.__previous_task_result = value

    def _preamble(self,
        previous_task_result: Optional[TaskResult] = None
    ) -> None:
        """@BaseTask._preamble"""
        if previous_task_result is None:
            previous_task_result = TaskResult(TaskStatus.SUCCESS, Container())
        self.previous_task_result = previous_task_result

    def _process_task(self) -> None:
        """@BaseTask._process_task"""
        self.result = TaskResult(
            TaskStatus.SUCCESS, 
            Container(task=type(self).__name__)
        )


class TestTask(TestCase):
    """Unit tests for TaskResult and BaseTask"""

    def testRunSingleTaskRunMethod(self):
        """Run single SimpleTask and check result"""
        task = SimpleTask()
        result = task.run()
        self.assertTrue(result.status == TaskStatus.SUCCESS)

    def testRunSingleTaskCallMethod(self):
        """Run single SimpleTask and check result"""
        task = SimpleTask()
        result = task()
        self.assertTrue(result.status == TaskStatus.SUCCESS)

    def testSimpleTaskPipeline(self):
        """Run sequence of SimpleTasks, passing results down pipeline"""
        previous_task_result = None
        for i in range(5):
            task = SimpleTask(previous_task_result)
            previous_task_result = task()
            with self.subTest(i=i):
                self.assertEqual(previous_task_result.status,TaskStatus.SUCCESS)
