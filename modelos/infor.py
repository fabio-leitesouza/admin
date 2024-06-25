class Work:
    works = []  # Lista para armazenar todos os trabalhos registrados
    
    def __init__(self, entrada, saida, job_function, work_value):
        self.entrada = entrada 
        self.saida = saida 
        self.job_function = job_function  
        self.work_value = work_value  
        Work.works.append(self) 
    
    # método para imprimir em formato de string para representação do trabalho
    def __str__(self):
        return f'{self.entrada} | {self.saida} | {self.job_function} | {self.work_value}'  
    
    # Método para imprimir a lista de todos os trabalhos registrados
    @classmethod
    def work_list(cls):
        print(f"{'Hora de entrada':<15} | {'Hora de saída':<15} | {'Função do Trabalho':<20} | {'Valor do trabalho':<15}")
        for work in cls.works:
            print(f'{work.entrada:<15} | {work.saida:<15} | {work.job_function:<20} | {work.work_value:<15}')
        
    # Método para obter as informações do usuário
    @classmethod
    def infor_works(cls):
        entrada = input("Digite o horário de entrada: ")
        saida = input("Digite o horário de saída: ")
        job_function = input("Digite a função do trabalho: ")
        work_value = input("Digite o valor do trabalho: ")

        # Cria um novo objeto Work com as informações fornecidas
        new_info = cls(entrada, saida, job_function, work_value)
        print("\nInformações de trabalho adicionadas com sucesso!\n")
