import os
from pathlib import Path

import pytest

import pysett
from .prepenv import build_echocat


@pytest.fixture(autouse=True)
def _enable_logging():
    pysett.load_logger(os.getenv('TEST_LOG_LEVEL', 'debug'))


@pytest.fixture(scope="session")
def echocat_exe(tmp_path_factory) -> Path:
    build_dir = tmp_path_factory.mktemp('echocat_build')
    res = build_echocat(build_dir)
    assert res
    return res
