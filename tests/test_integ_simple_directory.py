from pathlib import Path

import pytest as pytest

import pysett
from pysett import RunParams
from .prepenv import PREP_DATA_PATH

PREP_DATA_SINGLE_PATH = PREP_DATA_PATH / 'single'


@pytest.fixture()
def run_params(prep_ws: Path, echocat_exe: Path) -> RunParams:
    return RunParams(dict(
        tests_dir=PREP_DATA_SINGLE_PATH,
        executable=echocat_exe,
        ws=prep_ws,
    ))


def test_directory_struct(run_params):
    parser = pysett.DirectoryTestsParser(run_params)
    project = parser.parse()
    assert project
    assert project.parent is None
    assert project.kind == 'project'
    assert project.name == 'single'
    assert project.id == 'single'
    assert len(project.suites) == 1

    suite = project.suites[0]
    assert suite.id == 'single'
    assert len(suite.tests) == 3
    hello_test = suite.find_test('hello')
    assert hello_test.id == 'hello'
    assert hello_test.name == 'hello'

    assert len(hello_test.validations) == 3


def test_directory_run(run_params):
    parser = pysett.DirectoryTestsParser(run_params)
    project = parser.parse()

    result = pysett.ProjectRunner(run_params, project).run()
    pysett.print_project_result(result)
    assert result.is_pass()
