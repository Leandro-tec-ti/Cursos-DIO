class cachorro:
    def __init__(self, nome, cor, acordado=True):
        print("incializando classe...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado


    def __del__(self):      # vai aparecer sempre no final para finalizar o texto.
         print('Removendo a instancia da classe. ') 

    
    def falar(self):
        print("uaua")



c = cachorro("charpie", "amarelo")
c.falar()