from modelos.usuarios.user import User
from modelos.company.company import Company
from modelos.infor import Work

# Função para criar um novo usuário
def create_user():
    username = input("Digite o nome de usuário: ")
    email = input("Digite o endereço de e-mail: ")
    telephone = input("Digite o número de telefone: ")

    # Verificar se o usuário já existe na lista de usuários da classe User
    for user in User.usuarios:
        if user._username == username:
            print("\nUsuário já cadastrado. Faça login em vez de criar um novo usuário.\n")
            return
    
    # Criar um novo usuário e adicionar à lista de usuários da classe User
    new_user = User(username, email, telephone)
    User.usuarios.append(new_user)
    print("\nUsuário criado com sucesso!\n")

# Função para fazer login
def login():
    username = input("\nDigite o nome de usuário: ")
    password = input("Digite a senha: ")
        
    for user in User.usuarios:
        if user._username == username:
            # Aqui você poderia adicionar uma verificação de senha se desejado
            print(f"\nBem-vindo, {user._username}!\n")
            return
        
    print("\nUsuário não encontrado. Verifique os dados e tente novamente.\n")

# Função para interação com empresas
def create_company():
    while True:
        print()
        print("1 - Cadastrar empresa")
        print("2 - Listar empresas cadastradas")
        print("3 - Sair")

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            # Verifica se o número de empresas cadastradas não excedeu o limite
            if len(Company.companies) < Company.MAX_CADASTROS:
                nome = input("\nDigite o nome da empresa: ")
                funcao = input("Digite a função da empresa: ")
                telefone = input("Digite o telefone da empresa: ")
                endereco = input("Digite o endereço da empresa: ")

                # Cria uma nova instância de Company com as informações fornecidas
                Company(nome, funcao, telefone, endereco)
            else:
                print("Número máximo de cadastros atingido. Assine o prêmio para cadastros sem limites.")

        elif opcao == 2:
            Company.company_list()  # Chama o método para listar empresas cadastradas

        elif opcao == 3:
            print("Encerrando o programa.")
            break

        else:
            print("Opção inválida. Tente novamente.")

# Exemplos de chamadas que estavam no seu código original
Work.infor_works()  # Método estático para adicionar informações de trabalho

def main():
    Company.company_list()  # Método para listar todas as empresas registradas
    User.user_list()  # Método para listar todos os usuários registrados
    Work.work_list()  # Método para listar todos os trabalhos registrados

if __name__ == '__main__':
    main()
