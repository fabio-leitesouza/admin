# Importa a classe User do módulo usuarios.user
from usuarios.user import User

# Classe que herda da classe User e adiciona funcionalidades específicas.
class UserPrime(User):
    
    # Construtor da classe UserPrime.
    def __init__(self, username, email, telefone, faturamento_dia, semanal, mensal, anual):
        
        # Chama o construtor da classe pai (User)
        super().__init__(username, email, telefone)
        
        self._faturamento_dia = faturamento_dia
        self._semanal = semanal
        self.mensal = mensal
        self.anual = anual
        # Lista vazia para armazenar relatórios
        self._relatorio = []
        
    # Adiciona um relatório à lista de relatórios.   
    def add_relatorio(self, relatorio):
        
        # Adiciona o relatório à lista _relatorio
        self._relatorio.append(relatorio)
    
    # Retorna a lista de relatórios adicionados.
    def list_relatorio(self):
        return self._relatorio