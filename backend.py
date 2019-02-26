from datetime import *
class Relogio:
    def __init__(self):
       self.atualiza()

    def atualiza(self):
        horaagora = datetime.now()
        self.hora = horaagora.hour
        self.minuto = horaagora.minute
        self.segundo = horaagora.second

    def get_hora(self):
        return self.hora
    def get_minuto(self):
        return self.minuto
    def get_segundo(self):
        return self.segundo
