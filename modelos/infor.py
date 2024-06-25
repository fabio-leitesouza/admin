class Work:
    # Lista para armazenar todos os trabalhos registrados
    works = []
    
    def __init__(self, entrada, saida, job_function, work_value):
        self.entrada = entrada
        self.saida = saida
        self.job_function = job_function
        self.work_value = work_value
        Work.works.append(self)  # Adiciona o trabalho à lista de trabalhos registrados
    
    # Retorna uma representação em string do objeto Work.
    def __str__(self):
        return f'{self.entrada} | {self.saida} | {self.job_function} | {self.work_value}'
    
    # Imprime uma lista formatada de todos os trabalhos registrados.
    @classmethod
    def work_list(cls):
        print(f"{'Hora de entrada':<15} | {'Hora de saída':<15} | {'Função do Trabalho':<20} | {'Valor do trabalho':<15}")
        for work in cls.works:
            print(f'{work.entrada:<15} | {work.saida:<15} | {work.job_function:<20} | {work.work_value:<15}')
    
    # Solicita ao usuário informações sobre um novo trabalho e adiciona à lista de trabalhos registrados.
    @classmethod
    def infor_works(cls):
        entrada = input("Digite o horário de entrada: ")
        saida = input("Digite o horário de saída: ")
        job_function = input("Digite a função do trabalho: ")
        work_value = input("Digite o valor do trabalho: ")

        # Cria um novo objeto Work com as informações fornecidas e imprime mensagem de sucesso
        new_info = cls(entrada, saida, job_function, work_value)
        print("\nInformações de trabalho adicionadas com sucesso!\n")