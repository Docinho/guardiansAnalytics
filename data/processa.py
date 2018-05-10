#08/02/2018;22:10:34;lcc2-32;-6480568611700929889,7995863693106437687

class Dia:

    def __init__(self, dia):
        self.dia = dia
        self.horas = dict([(x, set()) for x in range(0, 24)])

    def marca_hora(self, hora, usuarios):
        self.horas[hora].update(set(usuarios))

    def processa(self):
        for hora in reversed(sorted(self.horas.keys())):
            if hora < 20:
                break
            else:
                for users in self.horas.values():
                    users.difference_update(self.horas[hora])

    def usuarios(self):
        r = set()
        for h, u in self.horas.items():
            r.update(set(u))
        return r

    def __eq__(self, x):
        return self.dia == x.dia

    def __hash__(self):
        return hash(self.dia)

    def __repr__(self):
        return str(self)

    def __str__(self):
        return self.dia

    def lista(self):
        r = ""
        for hora in sorted(self.horas.keys()):
            r += self.dia + ' ' + str(hora) + ' ' + ','.join(self.horas[hora]) + '\n'
        return r

dias = {}
import sys

for linha in open(sys.argv[1]).readlines():
    data, hor, maq, users = linha.split(';')
    data = data.split('/')[2] + '-' + data.split('/')[1] + '-' + data.split('/')[0]
    hor, minutes = hor.split(':')[0:2]
    d = dias.get(data, Dia(data))
    dias[data] = d
    d.marca_hora(int(hor), [users.strip().split(',')[-1]])

for data, dia in dias.items():
    dia.processa()
    print(dia.lista())
