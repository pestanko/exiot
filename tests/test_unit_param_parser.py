from pathlib import Path

import pytest

from exiot import ParamParser


@pytest.fixture
def parser() -> 'ParamParser':
    return ParamParser.default()


def test_parser_single_no_annot(parser: ParamParser):
    res = parser.parse(["hello: world"])
    assert res['hello'] == 'world'


def test_parser_single_boolean(parser: ParamParser):
    res = parser.parse(["boolean"])
    assert res['boolean'] is True


def test_parser_multiple_no_annot(parser: ParamParser):
    res = parser.parse([
        "hello: world",
        "how: are you",
        "number: 123456"
    ])
    assert res['hello'] == 'world'
    assert res['how'] == 'are you'
    assert res['number'] == '123456'


def test_parser_multiple_with_annot(parser: ParamParser):
    res = parser.parse([
        "hello: world",
        "path: @path /home",
        "number: @int 123456",
        "float: @float 123456.123",
    ])

    assert res['hello'] == 'world'
    assert res['path'] == Path("/home")
    assert res['number'] == 123456
    assert res['float'] == 123456.123
