class Company:
    companies = []
    MAX_CADASTROS = 3

    def __init__(self, company_name, function, telephone, endereco):        
        self.company_name = company_name.title()
        self.function = function
        self.telephone = telephone
        self.endereco = endereco
        if len(Company.companies) < Company.MAX_CADASTROS:
          Company.companies.append(self)
          print("\nEmpresa cadastrada com sucesso!")
        else:
           print("\nNúmero máximo de cadastros atingido.\n")

    def __str__(self):
      return f'{self.company_name} | {self.function} | {self.telephone} | {self.endereco}'

    @classmethod
    def company_list(cls):
      print(f"{'Nome da empresa':<15} | {'Função':<15} | {'Telefone':<15} | {'Endereço':<15}")
      for company in cls.companies:
        print(f'{company.company_name:<15} | {company.function:<15} | {company.telephone:<15} | {company.endereco:<15}')

    @classmethod
    def create_company(cls):
      while True:
       print()
       print("1 - Cadastrar empresa")
       print("2 - Listar empresas cadastradas")
       print("3 - Sair")

       opcao = int(input("Escolha uma opção: "))

       if opcao == 1:
           if len(Company.companies) < Company.MAX_CADASTROS:
           
            nome = input("\nDigite o nome da empresa: ")
            funcao = input("Digite a função da empresa: ")
            telefone = input("Digite o telefone da empresa: ")
            endereco = input("Digite o endereço da empresa: ")

            Company(nome, funcao, telefone, endereco)
           else:
              print("Número máximo de cadastros atigido, assine o prêmio para cadastros sem limites.")

       elif opcao == 2:  
           Company.company_list()

       elif opcao == 3:
           print("Encerrando o programa.")
           break
       else:
           print("Opção inválida. Tente novamente.")
