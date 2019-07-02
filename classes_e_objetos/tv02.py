class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 2

    def muda_canal_para_baixo(self):
        '''
        Isto muda canal para baixo
        '''
        self.canal -= 1

    def muda_canal_para_cima(self):
        '''
        Isto muda canal para cima
        '''

        self.canal += 1

tv_cozinha = Televisao()
tv_banheiro = Televisao()

tv_cozinha.muda_canal_para_baixo()
tv_banheiro.muda_canal_para_cima()
print(tv_cozinha.canal)
print(tv_banheiro.canal)