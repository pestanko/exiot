import subprocess
from pathlib import Path

import pytest

import pysett
from .prepenv import ECHO_CAT_PATH


@pytest.fixture(autouse=True)
def _enable_logging():
    pysett.load_logger('DEBUG')


@pytest.fixture()
def prep_ws(tmp_path) -> Path:
    pth = tmp_path / 'prep_ws'
    pth.mkdir(parents=True)
    return pth


@pytest.fixture()
def echocat_exe(tmp_path) -> Path:
    pth = tmp_path / 'echocat_bld'
    pth.mkdir(parents=True)
    binary = f"{pth}/echocat"
    res = subprocess.run(["gcc", "-std=c99", "-o", binary, f"{ECHO_CAT_PATH}"])
    print(res.stdout)
    print(res.stderr)
    assert res.returncode == 0
    file = list(pth.glob("echocat"))
    assert file
    return file[0]
