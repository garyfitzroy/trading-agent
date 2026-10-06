from __future__ import annotations

import os


def test_environment_file_example_exists() -> None:
    assert os.path.exists(".env.example")
