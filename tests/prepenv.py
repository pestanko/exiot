import logging
import subprocess
from pathlib import Path
from typing import Optional

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
    try:
        res = subprocess.run(args)
    except Exception as ex:
        TEST_LOG.warning(f"[EXE] Unable to build using '{cmd}': {ex}")
        return None
    TEST_LOG.debug(f"[EXE] {args} [exit={res.returncode}] STDOUT:  {res.stdout}")
    TEST_LOG.debug(f"[EXE] {args} [exit={res.returncode}] STDERR: {res.stderr}")
    if res.returncode != 0:
        return None
    files = list(output.glob("echocat"))
    return files[0] if files else None
