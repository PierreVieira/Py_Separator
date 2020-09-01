from src.model.memoria_cache import MemoryCache
from src.controller.feeder_json import alimentar_json
from src.controller.filter_input import pega_conteudo_filtrado
from src.controller.filter_output import pega_silabas_filtradas, make_io
from src.view.menu import Menu

menu = Menu()
memoria_cache = MemoryCache()
if menu.resposta == 'S' or menu.counter_calls == 0:
    with open('../files/text/input.txt', encoding='utf-8') as input_text:
        conteudo_filtrado = pega_conteudo_filtrado(input_text)
        alimentar_json(conteudo_filtrado)
        silabas_filtradas = pega_silabas_filtradas(conteudo_filtrado)
    with open('../files/text/output.txt', 'w', encoding='utf-8') as output_text:
        memoria_cache.insert_new_words(conteudo_filtrado)
        saida = make_io(silabas_filtradas)
        print(saida)
        output_text.write(saida)
else:
    pass
