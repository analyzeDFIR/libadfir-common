## -*- coding: UTF-8 -*-
## patterns.py
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

from typing import Optional, Any, NoReturn, Dict, TypeVar
T = TypeVar('T')
S = TypeVar('S')


class RegistryMetaclassMixin:
    """Registry mixin class implementing registry pattern
    with Python metaprogramming. Intended to be used as
    mixin with type.
    """
    _REGISTRY = None

    @classmethod
    def registry(cls) -> Dict[str, Any]:
        """Getter for copy of static _REGISTRY"""
        if cls._REGISTRY is None:
            return dict()
        return dict(cls._REGISTRY)

    @classmethod
    def retrieve(cls, name: str) -> Optional[Any]:
        """
        Args:
            name    => name of class to retrieve from registry
        Returns:
            Class 'name' if in registry, None otherwise.
        Preconditions:
            N/A
        """
        return cls.registry().get(name)

    @classmethod
    def _create_class(cls, name: str, bases: tuple, attrs: Dict[str, Any]) -> Any:
        """
        Args:
            name    => name of the class to be created
            bases   => base class(es) that the class to be created extends
            attrs   => namespace for the class to be created
        Returns:
            The new class.
        Preconditions:
            N/A
        """
        new_cls = type.__new__(cls, name, bases, attrs)
        return new_cls

    @classmethod
    def _add_class(cls, name: str, new_cls: Any) -> NoReturn:
        """
        Args:
            new_cls => new class to add to registry
        Procedure:
            Apply checks to new class and add to registry if all checks passed.
        Preconditions:
            N/A
        """
        raise NotImplementedError(
            '_add_class not implemented for class %s'%cls.__name__
        )

    def __new__(cls, name: str, bases: tuple, attrs: Dict[str, Any]) -> Any:
        """
        Args:
            name    => name of new class
            bases   => tuple of base classes
            attrs   => dictionary of type attributes
        Returns:
            Newly created directive class.
        Preconditions:
            N/A
        """
        new_cls = cls._create_class(name, bases, attrs)
        cls._add_class(name, new_cls)
        return new_cls


class Container(Dict[T, S]):
    """Generic container that implements both the Dict API
    as well as attribute-like access to data in the mapping.
    For example, to access the value for key 'this_key' in the container
    variable 'tup' one could use:
        tup.this_key or
        tup['this_key'] or
        tup.get('this_key')
    """

    def __getattr__(self, key: T) -> S:
        """Attribute access implementation
        (passthrough to dict.__getitem__)
        """
        try:
            return self[key]
        except KeyError:
            raise AttributeError(key)

    def __setattr__(self, key: T, value: S) -> None:
        """Attribute set implementation
        (passthrough to dict.__setitem__)
        """
        try:
            self[key] = value
        except KeyError:
            raise AttributeError(key)

    def __delattr__(self, key: T) -> S:
        """Attribute deletion implementation
        (passthrough to dict.__delitem__)
        """
        try:
            del self[key]
        except KeyError:
            raise AttributeError(key)
