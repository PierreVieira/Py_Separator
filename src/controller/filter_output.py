def pega_silabas_filtradas(palavras):
    print(palavras)
    return ''


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
