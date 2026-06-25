class Homem:
    def __init__(self):
        self.telescopio = Telescopio()
    def ver_com_telescopio(self, alguem):
        self.telescopio.ver(alguem)

class Mulher:
    pass

class Telescopio:
    def ver(self, alguem):
        pass

h = Homem()
m = Mulher()

h.ver_com_telescopio(m)