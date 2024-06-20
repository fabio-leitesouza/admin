class User:
# Atributo de classe para armazernar todos os usuários
    usuarios = []

# Metodo contrutor para adicionar os atributos 
    def __init__(self, username, email, telephone):
        self. _username = username
        self._email = email
        self._telephone = telephone
        User.usuarios.append(self)
        
    def __str__(self):
        return f'{self. _username} | {self._email} | {self._telephone}'
        
    @classmethod
    def user_list(cls):
        print(f"{'Nome':<15} | {'Email':<15} | {'Telefone':<15}")
        for user in cls.usuarios:
            print(f'{user._username:<15} | {user._email:<15} | {user._telephone:<15}')

# Metodo para obter as informações do usuário
    @classmethod
    def create_user(cls):
        username = input("Digite o nome de usuário: ")
        email = input("Digite o endereço de e-mail: ")
        telephone = input("Digite o número de telefone: ")

# Verificar se o usuário já existe 
        for user in cls.usuarios:
            if user._username == username:
                print("\nUsuário já cadastrado. Faça longin em vez de criar um novo usuário.\n")
                return
            new_user = cls(username, email, telephone)
        print("\nUsuário criado com sucesso! \n")

    @classmethod 
    def login(cls):
        username = input("\nDigite o nome de usuário: ")
        password = input("Digite a senha: ")
        for user in cls.usuarios:
            if user._username == username:
                print(f"Bem vindo,{user._username}")
                return
            print("\nUsuário não encontrado ou senha incorreta Verifique os dados e tente novamente.\n")
            