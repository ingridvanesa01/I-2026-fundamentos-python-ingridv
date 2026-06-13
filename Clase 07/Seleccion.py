class Seleccion:
    def __init__(self, pais, confederacion):
        self.pais = pais
        self.confederacion = confederacion
        self.jugadores = []
    
    def agregar_jugador(self, jugador):
        self.jugadores.append(jugador)
    def mostrar_jugadores(self, jugador):
        for jugador_en_lista in self.jugadores:
            if jugador_en_lista == jugador:
                self.jugadores.remove(jugador_en_lista)
                break


argentina = Seleccion("Argentina", "Conmebol")
brasil = Seleccion("Brasil", "Conmebol")
espana = Seleccion("España", "UEFA")

argentina.agregar_jugador(" LionelMessi")
espana.agregar_jugador("Angel Di Maria")
brasil.agregar_jugador("Neymar")
argentina.agregar_jugador("Lamine yamal")
print(argentina.jugadores)
print(espana.jugadores)
print(brasil.jugadores)
argentina.eliminar_jugador("Angel Di Maria")
print(argentina.jugadores)




