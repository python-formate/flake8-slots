# stdlib
import ast

# 3rd party
import pytest

# this package
from flake8_slots import Plugin, Visitor

string_a = "\nclass String(str): __slots__ = ['foo']"
string_b = "import builtins\nclass String(builtins.str):  __slots__ = ['foo']"
builtins_tuple_a = "\nclass Tuple(tuple):  __slots__ = ()"
builtins_tuple_b = "import builtins\nclass Tuple(builtins.tuple):  __slots__ = ()"
typing_tuple_a = "import typing\nclass Tuple(typing.Tuple):  __slots__ = ()"
typing_tuple_b = "from typing import Tuple\nclass TupleTuple(Tuple):  __slots__ = ()"
typing_tuple_c = "import typing\nclass Tuple(typing.Tuple[str, int, float]):  __slots__ = ()"
namedtuple_a = "import collections\nclass Person(collections.namedtuple('foo', 'name, age')):  __slots__ = ()"
namedtuple_b = "from collections import namedtuple\nclass Person(namedtuple('foo', 'name, age')):  __slots__ = ()"

typing_namedtuple_a = """\
import typing
class Person(typing.NamedTuple):
	__slots__ = ()
	name: str
	age: int
"""

typing_namedtuple_b = """\
from typing import NamedTuple
class Person(NamedTuple):
	__slots__ = ()
	name: str
	age: int
"""

sources = pytest.mark.parametrize(
		"source",
		[
				string_a,
				string_b,
				builtins_tuple_a,
				builtins_tuple_b,
				typing_tuple_a,
				typing_tuple_b,
				typing_tuple_c,
				namedtuple_a,
				namedtuple_b,
				typing_namedtuple_a,
				typing_namedtuple_b,
				]
		)


@sources
def test_plugin(source: str):
	plugin = Plugin(ast.parse(source))
	assert not list("{}:{}: {}".format(*r) for r in plugin.run())


@sources
def test_visitor(source: str):
	visitor = Visitor()
	visitor.visit(ast.parse(source))

	assert not visitor.errors
