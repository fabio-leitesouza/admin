class Company:
    companies = [] # Lista para armazenar as empresas
    MAX_CADASTROS = 3 # limitador de cadastro

    # Método construtor 
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

    # Método para imprimir as informaçãoes na tela 
    def __str__(self):
      return f'{self.company_name} | {self.function} | {self.telephone} | {self.endereco}'

    @classmethod
    def company_list(cls):
      print(f"{'Nome da empresa':<15} | {'Função':<15} | {'Telefone':<15} | {'Endereço':<15}")
      for company in cls.companies:
        print(f'{company.company_name:<15} | {company.function:<15} | {company.telephone:<15} | {company.endereco:<15}')
