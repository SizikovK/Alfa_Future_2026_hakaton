"""Developer tasks: run inv check, inv format, inv test in backend/."""

import shlex
import sys
from pathlib import Path

from invoke import task

BACKEND_DIR = Path(__file__).resolve().parent


def run_module(context, module, arguments):
    with context.cd(str(BACKEND_DIR)):
        context.run(f"{shlex.quote(sys.executable)} -m {module} {arguments}", echo=True)


@task
def check(context):
    """Check Python lint and formatting without modifying files."""
    run_module(context, "ruff", "check .")
    run_module(context, "ruff", "format --check .")


@task
def format(context):
    """Fix lint issues and format Python files."""
    run_module(context, "ruff", "check --fix .")
    run_module(context, "ruff", "format .")


@task
def test(context):
    """Run Python tests."""
    run_module(context, "pytest", "")
