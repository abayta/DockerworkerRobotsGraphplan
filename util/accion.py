class Accion(object):
    def __init__(self, nombre, precondiciones, efectosp, efectosn):
        self.nombre = nombre
        self.precondiciones = precondiciones
        self.efectosp = efectosp
        self.efectosn = efectosn


    def get_nombre(self):
        return self.nombre

    def get_precondiciones(self):
        return self.precondiciones

    def get_efectosn(self):
        return self.efectosN

    def get_efectosp(self):
        return self.efectosP

    # def siEsPrecondicion(self, atomo):
    #     return atomo in self.precondiciones
    #
    # def siEsEfectoN(self, atomo):
    #     return atomo in self.efectosN
    #
    # def siEsEfectoP(self, atomo):
    #     return atomo in self.efectosP
    #
    # def siPrecondEnLista(self,lista):
    #
    #     return [False if pred not in lista else True for pred in self.precondiciones]
    #     # for pred in self.precondiciones:
    #     #     if pred not in lista:
    #     #         return False
    #     # return True
    def es_aplicable(self,lista):
        return all(pred in lista for pred in  self.precondiciones)