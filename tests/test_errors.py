# stdlib
import ast

# 3rd party
import pytest

# this package
from flake8_slots import SLOT000, SLOT001, SLOT002, Plugin, Visitor

string_a = "\nclass String(str): pass"
string_b = "import builtins\nclass String(builtins.str): pass"
builtins_tuple_a = "\nclass Tuple(tuple): pass"
builtins_tuple_b = "import builtins\nclass Tuple(builtins.tuple): pass"
typing_tuple_a = "import typing\nclass Tuple(typing.Tuple): pass"
typing_tuple_b = "from typing import Tuple\nclass TupleTuple(Tuple): pass"
typing_tuple_c = "import typing\nclass Tuple(typing.Tuple[str, int, float]): pass"
namedtuple_a = "import collections\nclass Person(collections.namedtuple('foo', 'name, age')): pass"
namedtuple_b = "from collections import namedtuple\nclass Person(namedtuple('foo', 'name, age')): pass"

sources = pytest.mark.parametrize(
		"source, error",
		[
				(string_a, SLOT000),
				(string_b, SLOT000),
				(builtins_tuple_a, SLOT001),
				(builtins_tuple_b, SLOT001),
				(typing_tuple_a, SLOT001),
				(typing_tuple_b, SLOT001),
				(typing_tuple_c, SLOT001),
				(namedtuple_a, SLOT002),
				(namedtuple_b, SLOT002),
				]
		)


@sources
def test_plugin(source: str, error: str):
	plugin = Plugin(ast.parse(source))
	assert list("{}:{}: {}".format(*r) for r in plugin.run()) == [f"2:0: {error}"]


@sources
def test_visitor(source: str, error: str):
	visitor = Visitor()
	visitor.visit(ast.parse(source))

	assert visitor.errors == [(2, 0, error)]
