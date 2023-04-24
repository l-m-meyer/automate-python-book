import pytest, os
from deleteUnwantedFiles import *


test_folder = 'C:/Users/limeyer/Documents/automatepy/ch9'
test_small_file = './deleteUnwantedFiles.py'

class TestMain:
    def test_calls_main(self):
        assert callable(main)


    def test_calls_get_folder(self):
        assert callable(get_folder)


    def test_calls_get_large_files(self):
        assert callable(get_large_files)


class TestGetFolder:
    def test_folder_input(self):
        folder = get_folder()
        assert type(folder) is str


    def test_calls_compare_file_size(self):
        assert callable(compare_file_size)


class TestCompareFileSize:
    def test_compare_file_size(self):
        small_file = compare_file_size(test_small_file)
        assert small_file is False

    
    def test_file_size_less_than_100MB(self):
        file = get_file_size_in_MB(test_small_file)
        
        assert not file > 100

    
    def test_file_returns_float(self):
        file = get_file_size_in_MB(test_small_file)
        
        assert type(file) is float


class TestGetLargeFiles:
    def test_get_large_files(self):
        large_files = get_large_files(test_folder)
        assert type(large_files) is list