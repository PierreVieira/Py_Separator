from src.feeder_json import alimentar_json
from src.filter_input import pega_conteudo_filtrado
from src.filter_output import pega_silabas_filtradas, make_io

with open('files/text/input.txt', encoding='utf-8') as input_text:
    conteudo_filtrado = pega_conteudo_filtrado(input_text)
    alimentar_json(conteudo_filtrado)
    silabas_filtradas = pega_silabas_filtradas(conteudo_filtrado)
    with open('files/text/output.txt', 'w', encoding='utf-8') as output_text:
        saida = make_io(silabas_filtradas)
        print(saida)
        output_text.write(saida)
