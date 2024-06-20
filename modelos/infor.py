class Work:
    works = []
    
    def __init__(self, entrada, saida, job_function, work_value):
        self.entrada = entrada
        self.saida = saida
        self.job_function = job_function
        self.work_value = work_value
        Work.works.append(self)
    
    def __str__(self):
        return f'{self.entrada} | {self.saida} | {self.job_function} | {self.work_value}'
            
    @classmethod
    def work_list(cls):
        print(f"{'Hora de entrada':<15} | {'Hora de saída':<15} | {'Função do Trabalho':<15} | {'Valor do trabalho':<15}")
        for work in cls.works:
            print(f'{work.entrada:<15} | {work.saida:<15} | {work.job_function:<15} | {work.work_value:<15}')

    @classmethod
    def infor_works(cls):
        entrada = input("Digite o horário de entrada: ")
        saida = input("Digite o horário de saída: ")
        job_funtion = input("Digite a função do trabalho: ")
        work_value = input("Digite o valor do trabalho: ")

        new_infor = cls(entrada, saida, job_funtion, work_value)
        print("\n Digite um número para prosseguir \n")