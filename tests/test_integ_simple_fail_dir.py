from pathlib import Path

import pytest as pytest

import exiot
from exiot import RunParams
from .prepenv import EXAMPLES_PATH

PREP_DATA_SINGLE_PATH = EXAMPLES_PATH / 'single_fail'


@pytest.fixture(scope='module')
def run_params(tmp_path_factory, echocat_exe: Path) -> RunParams:
    return RunParams(dict(
        tests_dir=PREP_DATA_SINGLE_PATH,
        executable=echocat_exe,
        ws=tmp_path_factory.mktemp('prep_ws'),
    ))


@pytest.fixture(scope='module')
def fail_run(run_params) -> exiot.ProjectResult:
    parser = exiot.DirectoryTestsParser(run_params)
    project = parser.parse()

    result = exiot.ProjectRunner(run_params, project).run()
    exiot.print_project_result(result, verbose_size=1000)
    return result


@pytest.mark.integ
def test_fail_dir_run_full(run_params, fail_run: exiot.ProjectResult):
    assert fail_run.is_fail()
    assert len(fail_run.suites) == 1


@pytest.mark.integ
def test_fail_exit_mismatch(run_params, fail_run: exiot.ProjectResult):
    suite = fail_run.suites[0]
    assert suite.is_fail()
    test = suite.find_test('mismatch_exit')
    assert test
    assert test.is_fail()

    assert test.main_action.is_pass()

    assert len(test.actions) == 3
    assert test.n_failed == 1


@pytest.mark.integ
def test_fail_out_mismatch(run_params, fail_run: exiot.ProjectResult):
    suite = fail_run.suites[0]
    assert suite.is_fail()
    test = suite.find_test('mismatch_out')
    assert test
    assert test.is_fail()

    assert test.main_action.is_pass()

    assert len(test.actions) == 3
    assert test.n_failed == 1


@pytest.mark.integ
def test_fail_err_mismatch(run_params, fail_run: exiot.ProjectResult):
    suite = fail_run.suites[0]
    assert suite.is_fail()
    test = suite.find_test('mismatch_out')
    assert test
    assert test.is_fail()

    assert test.main_action.is_pass()

    assert len(test.actions) == 3
    assert test.n_failed == 1


@pytest.mark.integ
def test_fail_unknown(run_params, fail_run: exiot.ProjectResult):
    suite = fail_run.suites[0]
    assert suite.is_fail()
    test = suite.find_test('unknown')
    assert test
    assert test.is_fail()

    assert test.main_action.is_pass()

    assert len(test.actions) == 3
    assert test.n_failed == 2
