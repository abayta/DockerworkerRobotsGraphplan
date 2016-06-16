from util.mutex import Mutex


class Graphplan(object):
    def __init__(self, problema_planificacion):
        self.estado_inicial = problema_planificacion.estado_inicial
        self.acciones = problema_planificacion.acciones
        self.objetivos = problema_planificacion.objetivos
        self.accion_persistencia = [x for x in self.acciones if 'persistencia' in x.nombre]

    def graphPlan(self):
        niveles = []
        #Creamos un nivel que contendrá acciones y atomos
        nivel = GraphplanNivel(capa_acciones=None, capa_atomos=list(self.estado_inicial.variables_estados.values()))
        i = 0
        #añadimos el nivel a niveles
        niveles.append(nivel)
        while True:
            if self.objetivos in P: #sin mutex entre ellos
                print("Objetivos iguales a las precondiciones")
            else:
                i = i + 1
                #Creamos la capa de acciones
                # que tienen que cumplir las precondiciones de Pi-1
                nivel = GraphplanNivel()
                accionesAplicables = self.AccionesAplicables()

                #Calculamos mutex sobre la capa de acciones Ai

                #Creamos la capa de atomos(efectos de aplicar acciones)

                #Calculamos mutex sobre la capa de atomos

            # if la capa de atomos son las mismas en Pi-1 y Pi
            # y además tienen los mismos mutex se termina el while mediante break
        #devolver fallo porq no se ha podido encontrar una solucion



    #metodo que dado un nivel devuelve la lista de acciones aplicables a ese nivel
    def AccionesAplicables(self, nivelanterior):
        return [a for a in self.acciones if a.es_aplicable(nivelanterior.capa_atomos)]



class GraphplanNivel(object):
    def __init__(self, capa_acciones=None, capa_atomos=None):
        if capa_acciones is None:
            capa_acciones = CapaAcciones()
        if capa_atomos is None:
            capa_atomos = CapaAtomos()
        self.capa_acciones = capa_acciones
        self.capa_atomos = capa_atomos


class CapaAtomos(object):
    def __init__(self):
        self.atomos = []
        self.atomosMutex = []

    def setAtomos(self, lista_atomos):
        self.atomos=lista_atomos;

    def setAtomosMutex(self, lista_atomos_mutex):
        self.atomosMutex=lista_atomos_mutex

    def añadirAtomo(self,atomo):
        self.atomos.append(atomo)

    def añadirAtomosMutex(self,atomo1, atomo2):
        self.atomosMutex.append(Mutex(atomo1,atomo2))

class CapaAcciones(object):
    def __init__(self,):
        self.acciones = []
        self.accionesMutex = []

    def añadirAccion(self, accion):
        self.acciones.append(accion)

    def añadirAccionesMutex(self,accion1, accion2):
        self.accionesMutex.append(Mutex(accion1,accion2))
