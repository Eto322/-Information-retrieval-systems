import unittest
import tempfile
import shutil
from os import path
from indexes import InvertedIndex, ForwardIndex

class TestIndexes(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.file_pass_1 = path.join(self.test_dir, 'test1.txt')
        self.file_pass_2 = path.join(self.test_dir, 'test2.txt')
        with open(self.file_pass_1, "w") as file:
            file.write("Test file 1 File asd ")
        with open(self.file_pass_2, "w") as file:
            file.write("File 2 test file ")

    def tearDown(self):
        if path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)

    def index_search(self, index):
        index.build_index()
        assert index.search('1') == [self.file_pass_1]
        assert index.search('2') == [self.file_pass_2]
        assert set(index.search('File')) == {self.file_pass_1, self.file_pass_2}

    def test_inverted_index(self):
        index = InvertedIndex(self.test_dir)
        self.index_search(index)

    def test_forward_index(self):
        index = ForwardIndex(self.test_dir)
        self.index_search(index)

    def index_search_bad_directory(self, index):
        shutil.rmtree(self.test_dir)
        index.build_index()
        assert index.search('test') == []
        assert index.search('1') == []
        assert index.search('asd') == []

    def test_inverted_index_bad_dir(self):
        index = InvertedIndex(self.test_dir)
        self.index_search_bad_directory(index)

    def test_forward_index_bad_dir(self):
        index = ForwardIndex(self.test_dir)
        self.index_search_bad_directory(index)
