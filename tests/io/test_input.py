import pytest
import app.io.input as inp


# read_file_default tests
def test_read_file_default():
    file_read_str = inp.read_file_default('./tests/test_data/def_test.txt')
    assert file_read_str == 'TEST DEFAULT'


def test_read_file_default_raises():
    with pytest.raises(FileNotFoundError):
        inp.read_file_default('nonexistent.txt')


def test_read_file_default_multi_lines():
    file_read_str = inp.read_file_default('./tests/test_data/def_test2.txt')
    assert file_read_str == 'Line 1\nLine 2\nLine 3'
