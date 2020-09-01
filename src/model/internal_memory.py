import json

from src.model.collector import Collector
import src.constants as consts


class InternalMemory:
    def __init__(self):
        lista = []
        for char in consts.alphabet:
            with open('../../files/internal_memory' + char + '.json', encoding='utf-8') as char_internal_json:
                lista.append(json.load(char_internal_json))
            self.words = lista.copy()

    def get_word(self, word: str):
        posicao = consts.char_map_position[word[0]]
        return self.words[posicao][word]

    def insert(self, word: str):
        collector = Collector(word)
        object_word = collector.word_object
        posicao = consts.char_map_position[word[0]]
        self.words[posicao].append(object_word)
        with open('../../files/internal_memory' + word[0] + '.json', 'w', encoding='utf-8') as char_internal_json:
            json.dump(self.words[posicao], char_internal_json, ensure_ascii=False)
        return object_word
