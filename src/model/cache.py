from collections import deque

import src.constants as consts
import json


class MemoryCache:
    def __init__(self):
        self.current_cache = self._load_cache()

    @staticmethod
    def _load_cache():
        list_cache = deque()
        for char in consts.alphabet:
            with open('../../cache_memory/' + char + '.json', encoding='utf-8') as char_cache_json:
                data = json.load(char_cache_json)
                list_cache.append([data])
        return list_cache

    def _overrite_cache(self):
        for char in consts.alphabet:
            with open('../internal_memory/' + char + '.json', 'w', encoding='utf-8') as char_cache_json:
                position = consts.char_map_position[char]
                json.dump(self.current_cache[position], ensure_ascii=False)

    def insert_new_words(self, new_words):
        """
        Insere as palavras novas que o usuário solicitou na memória cache.
        Até esse fluxo do programa a cache teoricamente tem "memória infinita".
        Quando o programa finaliza o tamanho da cache é definido no arquivo constants.py
        :param new_words: lista de 26 listas (1 lista para cada letra)
        :return:
        """
        for char in consts.alphabet:
            position = consts.char_map_position[char]
            cont_lenght = len(self.current_cache[position])
            for word in new_words[position]:
                if word not in self.current_cache[position]:
                    if cont_lenght == consts.char_cache[position]:
                        self.current_cache.popleft()
                    else:
                        cont_lenght += 1
                    self.current_cache[position].append(word)
        self._overrite_cache()