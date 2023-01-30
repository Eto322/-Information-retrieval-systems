import os
from abc import ABC, abstractmethod

class Index(ABC):
    def __init__(self, directory='test'):
        self.index = {}
        self.directory = directory

    @staticmethod
    def get_words(file_path):
        with open(file_path, "r") as file:
            words = set(file.read().split())
        return words

    def get_file_paths(self):
        return [os.path.join(dp, f) for dp, dn, filenames in os.walk(self.directory) for f in filenames]

    @abstractmethod
    def build_index(self):
        pass

    @abstractmethod
    def search(self, search_word):
        pass


class InvertedIndex(Index):
    def build_index(self):
        for file_path in self.get_file_paths():
            for word in self.get_words(file_path):
                if word in self.index:
                    self.index[word].append(file_path)
                else:
                    self.index[word] = [file_path]

    def search(self, search_word):
        return self.index.get(search_word, [])


class ForwardIndex(Index):
    def build_index(self):
        for file_path in self.get_file_paths():
            self.index[file_path] = self.get_words(file_path)

    def search(self, search_word):
        return [file_path for file_path, words in self.index.items() if search_word in words]
