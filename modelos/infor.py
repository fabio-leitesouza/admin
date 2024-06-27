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