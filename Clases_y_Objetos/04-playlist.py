class Musica:
    def __init__(self, musica, estilo, cantante):
        self._musica =  musica
        self._estilo = estilo
        self._cantante = cantante


    def playlist(self):
        print(f"""La musica de este anio es:
Musica: {self._musica}
Estilo: {self._estilo}
Cantante: {self._cantante}""")

    @property
    def musica(self):
        return self._musica

    @musica.setter
    def musica(self,musica):
        self._musica = musica

    @property
    def estilo(self):
        return self._estilo

    @estilo.setter
    def estilo(self,estilo):
        self._estilo = estilo

    @property
    def cantante(self):
        return self._cantante

    @cantante.setter
    def cantante(self,cantante):
        self._cantante = cantante



musica = Musica('Demonia','Trap','Anuel AA')
musica.playlist()

musica.musica = 'En que pais'
musica.estilo = 'Trap Sucio'
musica.cantante = 'Bryan Myers'
print(f'\nNuevos valores: {musica.musica, musica.estilo, musica.cantante}')
musica.playlist()

