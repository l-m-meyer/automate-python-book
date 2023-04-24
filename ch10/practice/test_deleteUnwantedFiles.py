import pytest
from deleteUnwantedFiles import *


class TestMain:
    def test_main(self):
        assert callable(main)


    def test_retrieves_folder(self):
        assert callable(get_folder)

