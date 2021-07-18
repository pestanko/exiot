import logging
import subprocess
from pathlib import Path
from typing import Optional, List

import exiot

PROJECT_ROOT = Path(__file__).parent.parent
EXAMPLES_PATH = PROJECT_ROOT / 'examples'

ECHO_CAT_PATH = EXAMPLES_PATH / 'echocat.c'

TEST_LOG = logging.getLogger(exiot.APP_NAME + ".tests")


def build_echocat(output: Path) -> Optional[Path]:
    for cmd in ('clang', 'gcc'):
        res = _build_with_command(cmd, output)
        if res:
            return res
    return None


def _build_with_command(cmd: str, output: Path) -> Optional[Path]:
    binary = f"{output}/echocat"
    args = [cmd, "-std=c99", '-g', "-o", binary, f"{ECHO_CAT_PATH}"]
    _exec_cmd(args)
    files = list(output.glob("echocat"))
    return files[0] if files else None


def _exec_cmd(args: List[str]) -> Optional[subprocess.CompletedProcess]:
    try:
        res = subprocess.run(args)
    except Exception as ex:
        TEST_LOG.warning(f"[EXE] Unable to build using '{args[0]}': {ex}")
        return None
    TEST_LOG.debug(f"[EXE] {args} [exit={res.returncode}] STDOUT:  {res.stdout}")
    TEST_LOG.debug(f"[EXE] {args} [exit={res.returncode}] STDERR: {res.stderr}")
    if res.returncode != 0:
        return None
    return res


def build_with_cmake(root: Path, build: Optional['Path'] = None) -> Optional[subprocess.CompletedProcess]:
    build = build if build else root / 'build'
    args = ['cmake', '-B', str(build), str(root)]
    res = _exec_cmd(args)
    if res.returncode != 0:
        return res
    res = _exec_cmd(['make', '-k', '-C', str(build)])
    
    return res
