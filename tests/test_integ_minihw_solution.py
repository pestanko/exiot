from pathlib import Path

import pytest
import shutil

import exiot
from exiot import RunParams
from .prepenv import EXAMPLES_PATH, build_cmake

PREPARED_FILES = EXAMPLES_PATH / 'minihw_not_impl'


@pytest.fixture(scope='module')
def mini_base_dir(tmp_path_factory) -> Path:
    base = tmp_path_factory.mktemp('mini_not_impl')
    shutil.copytree(src=PREPARED_FILES, dst=base, dirs_exist_ok=True)
    return base


@pytest.fixture(scope='module')
def run_params(tmp_path_factory, mini_base_dir: Path) -> RunParams:
    bld = build_cmake(mini_base_dir)
    assert bld
    assert bld.returncode == 0
    return RunParams(dict(
        tests_dir=mini_base_dir,
        executable=None,
        ws=tmp_path_factory.mktemp('prep_ws_mini_notimpl'),
        target='solution'
    ))


@pytest.fixture(scope='module')
def succ_run(run_params: RunParams) -> exiot.ProjectResult:
    parser = exiot.MiniHwParser(run_params)
    project = parser.parse()

    result = exiot.ProjectRunner(run_params, project).run()
    exiot.print_project_result(result, verbose_size=1000)
    return result


@pytest.mark.slow
@pytest.mark.cmake
@pytest.mark.integ
@pytest.mark.passing
def test_run_minihw(succ_run: exiot.ProjectResult):
    assert succ_run.is_pass()
    for suite in succ_run.suites:
        assert suite.is_ok()
        assert suite.is_pass()
        for test in suite.tests:
            assert test.is_ok()
            assert test.is_pass()
