from src.controller.filter_input import pega_conteudo_filtrado
from src.controller.filter_output import pega_silabas_filtradas, make_output
from src.model.cache import MemoryCache
from src.model.internal_memory import InternalMemory
from src.view.menu import Menu

menu = Menu()
cache = MemoryCache('../files/json/cache_memory/')
internal_memory = InternalMemory('../files/json/internal_memory/')
filtred_content = None
while menu.resposta == 'S':
    print('Loading...')
    with open('../files/text/input.txt', encoding='utf-8') as input_text:
        filtred_content = pega_conteudo_filtrado(input_text)
        filtered_syllabales = pega_silabas_filtradas(filtred_content, cache, internal_memory)
    with open('../files/text/output.txt', 'w', encoding='utf-8') as output_text:
        saida = make_output(filtered_syllabales)
        print(saida)
        output_text.write(saida)
if filtred_content is None:
    raise ValueError('O conteúdo filtrado não pode ser vazio')
else:
    cache.overrite_cache()
