from pathlib import Path

import pytest as pytest

import exiot
from exiot import RunParams
from .prepenv import EXAMPLES_PATH

PREP_DATA_SINGLE_PATH = EXAMPLES_PATH / 'single'


@pytest.fixture(scope='module')
def run_params(tmp_path_factory, echocat_exe: Path) -> RunParams:
    return RunParams(dict(
        tests_dir=PREP_DATA_SINGLE_PATH,
        executable=echocat_exe,
        ws=tmp_path_factory.mktemp('prep_ws'),
    ))


@pytest.mark.integ
@pytest.mark.passing
def test_directory_struct(run_params):
    parser = exiot.DirectoryTestsParser(run_params)
    project = parser.parse()
    assert project
    assert project.parent is None
    assert project.kind == 'project'
    assert project.name == 'single'
    assert project.id == 'single'
    assert len(project.suites) == 1

    suite = project.suites[0]
    assert suite.id == 'single'
    exiot.print_project_df(project)
    assert len(suite.tests) == 6
    hello_test = suite.find_test('hello')
    assert hello_test.id == 'hello'
    assert hello_test.name == 'hello'

    assert len(hello_test.validations) == 3


@pytest.mark.integ
@pytest.mark.passing
def test_directory_run(run_params):
    parser = exiot.DirectoryTestsParser(run_params)
    project = parser.parse()

    result = exiot.ProjectRunner(run_params, project).run()
    exiot.print_project_result(result)
    assert result.is_pass()
