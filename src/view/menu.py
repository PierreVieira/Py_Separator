class Menu:
    def __init__(self):
        self._counter_calls = 0

    @property
    def resposta(self):
        self._counter_calls += 1
        if self._counter_calls == 1:
            return 'S'
        while True:
            resposta = input('\033[1;30;45mDeseja continuar? Digite s para sim ou n para não: \033[m').upper()
            if (resposta == 'S' or resposta == 'N') and self._counter_calls != 0:
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