from src.controller.filter_input import pega_conteudo_filtrado
from src.controller.filter_output import pega_silabas_filtradas, make_io
from src.model.cache import MemoryCache
from src.view.menu import Menu

menu = Menu()
cache = MemoryCache()
filtred_content = None
if menu.resposta == 'S' or menu.counter_calls == 0:
    with open('../files/text/input.txt', encoding='utf-8') as input_text:
        filtered_content = pega_conteudo_filtrado(input_text)
        filtered_syllabales = pega_silabas_filtradas(filtred_content, cache.current_cache)
    with open('../files/text/output.txt', 'w', encoding='utf-8') as output_text:
        saida = make_io(filtered_syllabales)
        print(saida)
        output_text.write(saida)
else:
    if filtred_content is None:
        raise ValueError('O conteúdo filtrado não pode ser vazio')
    else:
        cache.insert_new_words(filtred_content)
