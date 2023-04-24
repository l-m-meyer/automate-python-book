import pytest, sys
from deleteUnwantedFiles import *


class TestMain:
    def test_main(self):
        assert callable(main)


    def test_retrieves_folder(self):
        assert callable(get_folder)



class TestGetFolder:
    def test_folder_input(self):
        folder = get_folder()
        assert type(folder) is str

