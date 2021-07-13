from pathlib import Path

import pytest as pytest

import exiot
from exiot import RunParams
from .prepenv import PREP_DATA_PATH

PREP_DATA_SINGLE_PATH = PREP_DATA_PATH / 'proj_def_yml'


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


def test_sc_succ_run(succ_run):
    assert succ_run.is_pass()
