class User:
    usuarios = []
    
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

    @classmethod
    def create_user(cls):
        username = input("Digite o nome de usuário: ")
        email = input("Digite o endereço de e-mail: ")
        telephone = input("Digite o número de telefone: ")
        
        new_user = cls(username, email, telephone)
        print("\nUsuário criado com sucesso! \n")
            
            