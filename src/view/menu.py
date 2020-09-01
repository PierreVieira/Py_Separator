class Menu:
    def __init__(self):
        self._counter_calls = 0

    @property
    def resposta(self):
        while True:
            resposta = input('Deseja continuar? Digite s para sim ou n para não: ').upper()
            if resposta == 'S' or resposta == 'N':
                break
            else:
                print(f'Você digitou {resposta}. Vou tentar ser mais claro!')
                print('Para continuar o fluxo do programa digite s se não quer continuar digite n')
        return resposta

    @property
    def counter_calls(self):
        return self._counter_calls

    @counter_calls.setter
    def counter_calls(self, value):
        self._counter_calls = value