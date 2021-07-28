from pathlib import Path

import pytest as pytest

import exiot
from exiot import RunParams
from .prepenv import EXAMPLES_PATH

PREP_DATA_SINGLE_PATH = EXAMPLES_PATH / 'proj_def_fail_yml'


@pytest.fixture(scope='module')
def run_params(tmp_path_factory, echocat_exe: Path) -> RunParams:
    return RunParams(dict(
        tests_dir=PREP_DATA_SINGLE_PATH,
        executable=echocat_exe,
        ws=tmp_path_factory.mktemp('prep_ws'),
    ))


@pytest.fixture(scope='module')
def fail_run(run_params) -> exiot.ProjectResult:
    parser = exiot.FileScenarioDefParser(run_params)
    project = parser.parse()

    result = exiot.ProjectRunner(run_params, project).run()
    exiot.print_project_result(result, verbose_size=1000)
    return result


@pytest.mark.integ
@pytest.mark.failing
def test_sc_fail_run(fail_run):
    assert fail_run.is_fail()


@pytest.mark.integ
@pytest.mark.failing
def test_sc_fail_all_suites(fail_run):
    assert fail_run.n_failed == len(fail_run.suites)
    assert fail_run.n_oks == 0
    assert fail_run.n_passed == 0

    for suite_res in fail_run.suites:
        assert suite_res.is_fail()
        assert suite_res.n_passed == 0
        assert suite_res.n_failed == len(suite_res.tests)

        for t_res in suite_res.tests:
            assert t_res.is_fail()
