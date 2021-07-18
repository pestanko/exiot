from pathlib import Path

import pytest as pytest

import exiot
from exiot import RunParams
from .prepenv import EXAMPLES_PATH

PREP_DATA_SINGLE_PATH = EXAMPLES_PATH / 'proj_def_yml'


@pytest.fixture(scope='module')
def run_params(tmp_path_factory, echocat_exe: Path) -> RunParams:
    return RunParams(dict(
        tests_dir=PREP_DATA_SINGLE_PATH,
        executable=echocat_exe,
        ws=tmp_path_factory.mktemp('prep_ws'),
    ))


@pytest.fixture(scope='module')
def succ_run(run_params) -> exiot.ProjectResult:
    parser = exiot.FileScenarioDefParser(run_params)
    project = parser.parse()

    result = exiot.ProjectRunner(run_params, project).run()
    exiot.print_project_result(result, verbose_size=1000)
    return result


@pytest.mark.integ
def test_sc_succ_run(succ_run):
    assert succ_run.is_pass()
    all_suites = len(succ_run.suites)
    assert len(succ_run.df.suites) == all_suites
    assert succ_run.n_oks == all_suites
    assert succ_run.n_passed == all_suites
    assert succ_run.n_failed == 0


@pytest.mark.integ
def test_sc_succ_suites_run(succ_run):
    for res_suite in succ_run.suites:
        n_tests = len(res_suite.tests)
        assert res_suite.is_pass()
        assert res_suite.is_ok()
        assert not res_suite.is_fail()
        assert n_tests == len(res_suite.df.tests)
        assert res_suite.n_failed == 0
        assert res_suite.n_passed == n_tests
        assert res_suite.n_oks == n_tests

        for t_res in res_suite.tests:
            assert t_res.is_pass()
            assert t_res.is_ok()
            assert t_res.n_passed != 0
            assert t_res.n_oks != 0
            assert t_res.n_failed == 0
