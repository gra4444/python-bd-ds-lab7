import pandas.errors
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


# read_csv_file_pd tests
def test_read_csv_file_pd():
    file_read_str = inp.read_csv_file_pd('./tests/test_data/test_pd.csv')
    assert file_read_str == '   test\n0  text'


def test_read_csv_file_pd_raises_fnfe():
    with pytest.raises(FileNotFoundError):
        inp.read_csv_file_pd('nonexistent.csv')


def test_read_csv_file_pd_empty_raises_ede():
    with pytest.raises(pandas.errors.EmptyDataError):
        inp.read_csv_file_pd('./tests/test_data/empty_pd.csv')
