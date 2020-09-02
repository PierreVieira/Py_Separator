import src.constants as consts


def pega_silabas_filtradas(palavras, cache, internal):
    list_syllabales = []
    for palavra in palavras:
        value_sucess = None
        posicao = consts.char_map_position[consts.mapping_letter[palavra[0]].upper()]
        try:  # Tente puxar a palavra da cache
            value_sucess = cache.current_cache[posicao][0][palavra]
        except KeyError:  # A palavra não está na cache
            try:  # Tente puxar a palavra da memória interna
                value_sucess = internal.get_word(palavra)
            except KeyError:  # A palavra não está na memória interna
                # A palavra deve ser inserida na memória interna
                value_sucess = internal.insert(palavra)
            finally:
                if value_sucess is None:
                    raise ValueError(f'Palavra que deu merda: {palavra}\nvalue_sucess deve ser diferente de None.')
                else:
                    cache.current_cache[posicao][0][palavra] = value_sucess
        finally:
            if type(value_sucess) == dict:
                list_syllabales.extend(value_sucess[palavra].split('-'))
            else:
                list_syllabales.extend(value_sucess.split('-'))
    return list(set(list_syllabales))


def remove_acentos(silaba):
    string = ''
    for c in silaba:
        string += consts.mapping_letter[c]
    return string


def make_output(silabas_filtradas):
    silabas_filtradas = tuple(sorted(set(map(remove_acentos, silabas_filtradas))))
    string_io = ''
    vogal_recorrente = silabas_filtradas[0][0]
    for silaba in silabas_filtradas:
        if silaba[0] != vogal_recorrente:
            vogal_recorrente = silaba[0]
            string_io += '\n'
        string_io += silaba + ' '
    qtde_silabas = len(silabas_filtradas)
    qtde_tracos = qtde_silabas // 3
    string_io += '\n'
    string_io += '-' * qtde_tracos + '\n'
    string_io += f'No total temos {qtde_silabas} sílabas.'.center(qtde_tracos) + '\n'
    string_io += '-' * qtde_tracos + '\n'
    return string_io[:-1:]
