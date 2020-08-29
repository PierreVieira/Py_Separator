import json

from src.classes.collector import Collector


class ArquivoJson:
    def __init__(self, caminho: str):
        self._caminho = caminho

    def get_word(self, word: str):
        with open(self._caminho, encoding='utf-8') as json_file:
            words = json.load(json_file)
        return words[word]

    def insert(self, word: str):
        collector = Collector(word)
        object = collector.word_object
