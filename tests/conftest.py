"""Fixtures shared by the plugin tests."""

import pathlib

import pytest
from tmt.log import Logger
from tmt.utils import Path


@pytest.fixture
def tmppath(tmp_path: pathlib.Path) -> Path:
    """A temporary directory as tmt's own ``Path``."""

    return Path(tmp_path)


@pytest.fixture(name='root_logger')
def fixture_root_logger() -> Logger:
    """A logger to use for logging and/or spawning logger hierarchy."""

    return Logger.create(verbose=0, debug=0, quiet=False, apply_colors_logging=False)
