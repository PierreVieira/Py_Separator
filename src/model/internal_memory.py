import json

from src.model.collector import Collector
import src.constants as consts


class InternalMemory:
    def __init__(self, route_file):
        self.words = []
        self._route_file = route_file
        self._load_internal_memory()

    def _load_internal_memory(self):
        for char in consts.alphabet:
            lista = []
            with open(self._route_file + char + '.json', encoding='utf-8') as char_internal_json:
                lista.append(json.load(char_internal_json))
            self.words.append(lista)

    def get_word(self, word: str):
        posicao = consts.char_map_position[consts.mapping_letter[word[0]].upper()]
        palavras = self.words[posicao]
        return palavras[0][word]

    def insert(self, word: str):
        collector = Collector(word)
        object_word = collector.word_object
        posicao = consts.char_map_position[consts.mapping_letter[word[0]].upper()]
        self.words[posicao][0][word] = object_word[word]
        with open(self._route_file + consts.mapping_letter[word[0]] + '.json', 'w', encoding='utf-8') as char_internal_json:
            json.dump(self.words[posicao][0], char_internal_json, ensure_ascii=False)
        return object_word

    def __str__(self):
        i = 0
        string = ''
        for char in consts.alphabet:
            string += f'{char} -> {self.words[i]}' + '\n'
            i += 1
        return string

    def __repr__(self):
        return self.__str__()
