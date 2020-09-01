def filtrar_palavra(palavra):
    palavra_filtrada = ''
    for letra in palavra:
        if palavra.isalpha():
            palavra_filtrada += letra
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
