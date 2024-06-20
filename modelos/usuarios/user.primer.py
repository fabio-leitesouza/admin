from usuarios.user import User

class UserPrime(User):
    
    def __init__(self, username, email, telefone, faturamento_dia, semanal, mensal, anual):

        super().__init__(username, email, telefone)
        
        self._faturamento_dia = faturamento_dia
        self._semanal = semanal
        self.mensal = mensal
        self.anual = anual
        self._relatorio = []

    def add_relatorio(self, relatorio):
        self._relatorio.append(relatorio)

    def list_relatorio(self):
        return self._relatorio