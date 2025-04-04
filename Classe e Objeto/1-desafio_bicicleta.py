class bicicleta:
    def __init__(self, cor, molelo, ano, valor, aro=18): 
        self.cor = cor
        self.modelo = molelo
        self.ano = ano
        self.valor = valor
        self.aro = aro
    
    def buzinar(self):
        print("plim plim")

    
    def parar(self):
        print("parando bicicleta...")
        print("bicicleta parada!")

    
    def correr(self):
        print("bicicleta correndo...")
        print("vruuummmmm...")
        

    def __str__(self): # formula de busca de dados MAnual tenho que colcocar de forma manual o dado que quero. 
       return f'Bicicleta: cor= {self.cor}, modelo= {self.modelo}, ano= {self.ano}, valor= {self.valor}'    
    

    def __str__(self): # Formula de busca de dados automatizado idependente da quanitidade de atributos tem na bicicleta 
        return f'{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}'

b1 = bicicleta("vermelha", "caloi", 2022, 600)
b1.buzinar()
b1.correr()
b1.parar()

print(b1.cor, b1.modelo, b1.ano, b1.valor)

b2 = bicicleta("verde", "monark", 2000, 189)
print(b2)
