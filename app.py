from modelos.usuarios.user import User  # Importa a classe User do módulo modelos.usuarios.user
from modelos.company.company import Company  # Importa a classe Company do módulo modelos.company.company
from modelos.infor import Work  # Importa a classe Work do módulo modelos.infor

User.create_user()  # Método estático para criar um novo usuário
User.login()  # Método estático para fazer login de usuário existente
Work.infor_works()  # Método estático para adicionar informações de trabalho
Company.create_company()  # Método estático para criar uma nova empresa

def main():
    Company.company_list()  # Método para listar todas as empresas registradas
    User.user_list()  # Método para listar todos os usuários registrados
    Work.work_list()  # Método para listar todos os trabalhos registrados

if __name__ == '__main__':
    main() 