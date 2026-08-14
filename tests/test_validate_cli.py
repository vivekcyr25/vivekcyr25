"""
Unit tests for CLI argument parsing in scripts/validate_svgs.py
"""

from scripts.validate_svgs import main


def test_validate_svgs_main_default(capsys):
    ret = main([])
    assert ret == 0
    captured = capsys.readouterr()
    assert "Validating" in captured.out


def test_validate_svgs_main_invalid_dir():
    ret = main(["--dir", "non_existent_dir_12345"])
    assert ret == 1
