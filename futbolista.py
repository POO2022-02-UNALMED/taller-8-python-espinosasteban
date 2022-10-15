from persona import Persona
from deportista import Deportista

class Futbolista(Persona, Deportista):

    listaFutbolistas = []
    def __init__(self, nombre, edad, altura, sexo, añosPracticando, golesMarcados, tarjetasRojas, piernaHabil):
        Persona.__init__(self,nombre, edad, altura, sexo)
        Deportista.__init__(self,"Futbol", añosPracticando)
        self._golesMarcados = golesMarcados
        self._tarjetasRojas = tarjetasRojas
        self._piernaHabil = piernaHabil
        Futbolista.listaFutbolistas.append(self)

    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre;

    def getEdad(self):
        return self._edad

    def setEdad(self, edad):
        self._edad = edad;

    def getAltura(self):
        return self._altura

    def setAltura(self, altura):
        self._altura = altura

    def getSexo(self):
        return self._sexo

    def setSexo(self, sexo):
        self._sexo = sexo

    def getDeporte(self):
        return self._deporte

    def setDeporte(self, deporte):
        self._deporte = deporte

    def getAniosPracticando(self):
        return self._aniosPracticando

    def setAniosPracticando(self, aniosPracticando):
        self._aniosPracticando = aniosPracticando

    def getGolesMarcados(self):
        return self._golesMarcados

    def setGolesMarcados(self, golesMarcados):
        self._golesMarcados = golesMarcados

    def getTarjetasRojas(self):
        return self._tarjetasRojas

    def setTarjetasRojas(self, tarjetasRojas):
        self._tarjetasRojas = tarjetasRojas

    def getPiernaHabil(self):
        return self._piernaHabil

    def setPiernaHabil(self, piernaHabil):
        self._piernaHabil = piernaHabil

    @classmethod
    def getlistaFutbolistas(cls):
        return cls.listaFutbolistas

    @classmethod
    def setListaFutbolistas(cls, listaFutbolistas):
        cls.listaFutbolistas = listaFutbolistas

    def __str__(self):
        return f"Mi nombre es {Persona.getNombre(self)} soy profesional en el deporte {Deportista.getDeporte(self)} " \
               f"Tengo {Persona.getEdad(self)} años de edad y llevo {Deportista.getAñosPracticando(self)} años en el deporte"



