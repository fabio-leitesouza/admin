class User:
    # Atributo de classe para armazenar todos os usuários
    usuarios = []

    # Método construtor para inicializar os atributos do usuário
    def __init__(self, username, email, telephone):
        self._username = username
        self._email = email
        self._telephone = telephone
        User.usuarios.append(self)  # Adiciona a instância atual à lista de usuários

    # Método para retornar uma representação formatada do usuário
    def __str__(self):
        return f'{self._username} | {self._email} | {self._telephone}'

    # Método de classe para listar todos os usuários registrados
    @classmethod
    def user_list(cls):
        print(f"{'Nome':<15} | {'Email':<15} | {'Telefone':<15}")
        for user in cls.usuarios:
            print(f'{user._username:<15} | {user._email:<15} | {user._telephone:<15}')

    # Métodos adicionais da classe User podem ser definidos aqui
