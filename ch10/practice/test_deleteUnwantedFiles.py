import pytest, os
from deleteUnwantedFiles import *


class TestMain:
    def test_calls_main(self):
        assert callable(main)


    def test_calls_get_folder(self):
        assert callable(get_folder)


class TestGetFolder:
    def test_folder_input(self):
        folder = get_folder()
        assert type(folder) is str


    def test_calls_compare_file_size(self):
        assert callable(compare_file_size)


class TestCompareFileSize:
    def test_compare_file_size(self):
        small_file = compare_file_size('./deleteUnwantedFiles.py')
        assert small_file is None

    
    def test_file_size_less_than_100MB(self):
        small_file = get_file_size_in_MB('./deleteUnwantedFiles.py')
        
        assert not small_file > 100

