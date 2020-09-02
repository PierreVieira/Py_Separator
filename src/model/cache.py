from collections import deque

import src.constants as consts
import json


class MemoryCache:
    def __init__(self, route_file):
        self._route_file = route_file
        self.current_cache = self._load_cache()

    def _load_cache(self):
        list_cache = deque()
        for char in consts.alphabet:
            with open(self._route_file + char + '.json', encoding='utf-8') as char_cache_json:
                data = json.load(char_cache_json)
                list_cache.append([data])
        return list_cache

    def overrite_cache(self):
        for char in consts.alphabet:
            with open(self._route_file + char + '.json', 'w', encoding='utf-8') as char_cache_json:
                position = consts.char_map_position[char]
                json.dump(self.current_cache[position][0], char_cache_json, ensure_ascii=False)

    def __str__(self):
        i = 0
        string = ''
        for char in consts.alphabet:
            string += f'{char} -> {self.current_cache[i]}' + '\n'
            i += 1
        return string

    def __repr__(self):
        return self.__str__()
