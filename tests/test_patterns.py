## -*- coding: UTF-8 -*-
## test_patterns.py
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

from typing import Any

from unittest import TestCase
from ..patterns import RegistryMetaclassMixin, Container


class MetaClass(RegistryMetaclassMixin, type):
    _REGISTRY = dict()

    @classmethod
    def _add_class(cls, name: str, new_cls: Any) -> None:
        if name.find('Base') != -1:
            return
        cls._REGISTRY[name] = new_cls


class AbstractBaseClass(metaclass=MetaClass):
    pass


class ImplementationA(AbstractBaseClass):
    pass


class ImplementationB(AbstractBaseClass):
    pass


class AnotherMetaClass(RegistryMetaclassMixin, type):
    _REGISTRY = dict()

    @classmethod
    def _add_class(cls, name: str, new_cls: Any) -> None:
        pass


class TestRegistryMixin(TestCase):
    """Unit tests for RegistryMetaclassMixin."""

    def test_mixin_registry_method_registry_is_none(self):
        """_REGISTRY is None."""
        self.assertEqual(RegistryMetaclassMixin.registry(), dict())

    def test_mixin_retrieve_method_registry_is_none(self):
        """_REGISTRY is None."""
        self.assertTrue(RegistryMetaclassMixin.retrieve('ImplementationA') is None)

    def test_meta_class_add_class_filtering(self):
        """_add_class filters out the AbstractBaseClass."""
        self.assertTrue(MetaClass.retrieve('AbstractBaseClass') is None)

    def test_non_base_classes_in_registry(self):
        """ImplementationA and ImplementationB in _REGISTRY"""
        self.assertTrue(
            MetaClass.retrieve('ImplementationA') == ImplementationA and \
            MetaClass.retrieve('ImplementationB') == ImplementationB
        )

    def test_multiple_subclass_independent_registries(self):
        """MetaClass and AnotherMetaClass have different registries."""
        self.assertIsNot(MetaClass._REGISTRY, AnotherMetaClass._REGISTRY) #pylint: disable=W0212


class TestContainer(TestCase):
    """Unit tests for Container."""

    def test_dictionary_set_get_kv(self):
        """Set and get key-value pair via dict methods."""
        container = Container()
        container['key'] = 'value'
        self.assertEqual(container.get('key'), 'value')

    def test_dictionary_delete_kv(self):
        """Remove key-value pair via dict method."""
        container = Container()
        container['key'] = 'value'
        del container['key']
        self.assertTrue(container.get('key') is None)

    def test_attribute_set_get_kv(self):
        """Set and get key-value pair via attribute methods."""
        container = Container()
        container.key = 'value'
        self.assertEqual(container.key, 'value')

    def test_attribute_delete_kv(self):
        """Remove key-value pair via attribute method."""
        container = Container()
        container.key = 'value'
        del container.key
        self.assertRaises(AttributeError, getattr, container, 'key')

    def test_new_container_from_mapping(self):
        """Create new container from existing mapping."""
        mapping = dict(key='value')
        container = Container(mapping)
        self.assertTrue(container.key == mapping.get('key'))

    def test_new_container_from_iterable(self):
        """Create new container from existing iterable."""
        iterable = [('key', 'value')]
        container = Container(iterable)
        self.assertTrue(container.key == 'value')

    def test_new_container_from_kv(self):
        """Create new container from key-value pairs in form 'key=value'."""
        container = Container(key='value')
        self.assertTrue(container.key == 'value')
