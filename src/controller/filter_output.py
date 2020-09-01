import src.constants as consts
from src.model.internal_memory import InternalMemory


def pega_silabas_filtradas(palavras, cache):
    list_syllabales = []
    for palavra in palavras:
        value_sucess = None
        posicao = consts.char_map_position[palavra[0]]
        try:  # Tente puxar a palavra da cache
            value_sucess = cache[posicao][palavra]
        except KeyError:  # A palavra não está na cache
            internal_memory = InternalMemory()
            try:  # Tente puxar a palavra da memória interna
                value_sucess = internal_memory.get_word(palavra)
            except KeyError:  # A palavra não está na memória interna
                # A palavra deve ser inserida na memória interna
                value_sucess = internal_memory.insert(palavra)
        finally:
            if value_sucess is None:
                raise ValueError('value_sucess deve ser diferente de None.')
            else:
                list_syllabales.append(value_sucess)


def make_io(silabas_filtradas):
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
