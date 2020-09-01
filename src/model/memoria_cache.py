import src.constants as consts
import json


class MemoryCache:
    def __init__(self):
        self._palavras_cacheadas = self._load_cache()
        self.new_words = []

    def _load_cache(self):
        lista_cache = []
        for char in consts.alphabet:
            with open('../words_cache/' + char) as char_cache_json:
                data = json.load(char_cache_json)
                lista_cache.append([data])
        return lista_cache

    def insert_new_words(self, new_words):
        """
        Insere as palavras novas que o usuário solicitou na memória cache.
        Até esse fluxo do programa a cache teoricamente tem "memória infinita".
        Quando o programa finaliza o tamanho da cache é definido no arquivo constants.py
        :param new_words:
        :return:
        """
        pass
