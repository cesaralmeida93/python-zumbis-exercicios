import datetime

class Pessoa():
    def __init__(self, nome, nascimento):
        self.nome = nome
        self.nascimento = nascimento

    def idade(self):
        delta = datetime.date.today() - self.nascimento
        return int(delta.days/365)

    def __str__(self):
        return '%s, %d anos' %(self.nome, self.idade())

cesar = Pessoa('César Almeida', datetime.date(1993, 4, 15))
print(cesar.idade())
print(cesar)