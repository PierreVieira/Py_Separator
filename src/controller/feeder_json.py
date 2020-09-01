from src.model.arquivo_json import ArquivoJson


def alimentar_json(words_from_file):
    json = ArquivoJson('../files/words.json')
    for word in words_from_file:
        dict_palavra = None
        try:
            dict_palavra = json.get_word(word)
        except KeyError:
            dict_palavra = json.insert(word)
        finally:
            print(dict_palavra)
            pass
            # fazer algo com o dict_palavra (por exemplo imprimir na tela a separação silábica)


alimentar_json(['amigo', 'chocolate'])
