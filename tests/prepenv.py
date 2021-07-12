import subprocess
from pathlib import Path
from typing import Optional

import pytest

import pysett

PREP_DATA_PATH = Path(__file__).parent / 'prepared_data'
ECHO_CAT_PATH = PREP_DATA_PATH / 'echocat.c'


def build_echocat(output: Path) -> Optional[Path]:
    for cmd in ('clang', 'gcc'):
        res = _build_with_command(cmd, output)
        if res:
            return res
    return None


def _build_with_command(cmd: str, output: Path) -> Optional[Path]:
    binary = f"{output}/echocat"
    res = subprocess.run([cmd, "-std=c99", '-g', "-o", binary, f"{ECHO_CAT_PATH}"])
    print(res.stdout)
    print(res.stderr)
    if res.returncode != 0:
        return None
    files = list(output.glob("echocat"))
    return files[0] if files else None
