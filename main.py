from hyphen import Hyphenator


def filtrar_letra(letra):
    if letra == 'à' or letra == 'ã' or letra == 'á' or letra == 'â':
        return 'a'
    elif letra == 'é' or letra == 'ê':
        return 'e'
    elif letra == 'í':
        return 'i'
    elif letra == 'ó' or letra == 'õ' or letra == 'ô':
        return 'o'
    elif letra == 'ú':
        return 'u'
    return letra


def filtrar_palavra(palavra):
    palavra_filtrada = ''
    for letra in palavra:
        if palavra.isalpha():
            palavra_filtrada += filtrar_letra(letra)
    return palavra_filtrada


def filtrar_linha(linha):
    linha_sem_quebra = linha.strip()
    palavras = linha_sem_quebra.split()
    palavras_filtradas = []
    for palavra in palavras:
        palavras_filtradas.append(filtrar_palavra(palavra.lower()))
    return list(filter(lambda palavra: len(palavra) > 0, palavras_filtradas))


def pega_conteudo_filtrado(input_text):
    linhas_filtradas = []
    for linha in input_text.readlines():
        if linha == '\n':
            continue
        linha_filtrada = filtrar_linha(linha)
        linhas_filtradas.extend(linha_filtrada)
    return linhas_filtradas


def pega_silabas_filtradas(conteudo_filtrado):
    h_pt_br = Hyphenator('pt_BR')
    conjunto_silabas = set()
    for palavra in conteudo_filtrado:
        palavra_dividia = h_pt_br.syllables(palavra)
        for silaba in palavra_dividia:
            conjunto_silabas.add(silaba)
    return list(sorted(conjunto_silabas))


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


with open('text_files/input.txt', encoding='utf-8') as input_text:
    conteudo_filtrado = pega_conteudo_filtrado(input_text)
    silabas_filtradas = pega_silabas_filtradas(conteudo_filtrado)
    with open('text_files/output.txt', 'w', encoding='utf-8') as output_text:
        saida = make_io(silabas_filtradas)
        print(saida)
        output_text.write(saida)
