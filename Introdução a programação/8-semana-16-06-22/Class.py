# ===================================================================================================================
# EX_1:

class Bola:

    def __init__(self, cor, circunferencia, material):
        self.cor = cor 
        self.circunferencia = circunferencia  
        self.material = material 

    def troca_cor(self, cor):
        self.cor = cor
    
    def mostra_cor(self):
        print(self.cor)

# ===================================================================================================================
# EX_2:
class Retangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def mudar_valor(self, base, altura):
        self.base = base
        self. alturta = altura
    
    def lados(self):
        return self.base, self.altura
    
    def calculo_area(self):
        return self.base * self.altura
    
    def perimetro(self):
        return (self.base + self.altura) * 2

# ===================================================================================================================
# EX_3:
class Conta_corrente:

    def __init__(self, numero, nome, saldo = 0):
        self.numero = numero
        self.nome = nome
        self.saldo = saldo

    def alterar_nome(self, nome):
        self.nome = nome
    
    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f'Seu novo saldo é: R$ {self.saldo}')
        else:
            print(f'Não é possivel depositar R$ {valor}, pois ele é menor que R$ 0')
        
    def saque(self, valor):
        if self.saldo - valor >= 0 and valor > 0:
            self.saldo -= valor
            print(f'Seu novo saldo é: R$ {self.saldo}')
        else:
            print(f'Não é possivel realizar o saque de R$ {valor}, pois seu saldo é de: R$ {self.saldo}')

# =====================================================================================================================================
# EX_4:
class Tamagochi:

    def __init__(self):
        self.nome = None
        self.fome = None
        self.saude = None
        self.idade = None

    def alterar_nome(self, nome):
        self.nome = nome

    def alterar_fome(self,fome):
        self.fome = fome

    def alterar_saude(self, saude):
        self.saude = saude

    def alterar_idade(self, idade):
        self.idade = idade

    def retornar_fome(self):
        return self.fome

    def retornar_nome(self):
        return self.nome

    def retornar_saude(self):
        return self.saude

    def retornar_idade(self):
        return self.idade
# =====================================================================================================================================
# EX_5:

class Ponto:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def exibe_valores(self):
        print(f'x = {self.x}, y = {self.y}')
    
class Ret:

    def __init__(self):
        self.ponto1 = None
        self.ponto2 = None

    def centro(self):
        ponto_central = Ponto()
        
        ponto_central.x = (self.ponto1.x + self.ponto2.x) / 2
        ponto_central.y = (self.ponto1.y + self.ponto2.y) / 2
        return ponto_central
    
# =====================================================================================================================================
# EX_6:

class BombaCombustivel:
    def __init__(self, tipo_combustivel, valor_litro, quantidade_combustivel):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quantidade_combustivel = quantidade_combustivel
    
    def alterar_quantidade_combustivel(self, litro):
        if litro <= self.quantidade_combustivel:
            self.quantidade_combustivel -= litro
        else:
            print(f'Quantidade de combustivel insuficiente na bomba, so temos {self.quantidade_combustivel} litros')

    def abastecer_por_valor(self, valor_total):
        quantidade = valor_total / self.valor_litro
        print(f'Você abasteceu para R$ {valor_total}, que equivale a {quantidade} litros.')
        self.alterar_quantidade_combustivel(quantidade)

    def abastecer_por_litro(self, litro_total):
        valor = self.valor_litro * litro_total
        print(f'Você abasteceu {litro_total} litros. O Valor a pagar é: R$ {valor}')
        self.alterar_quantidade_combustivel(litro_total)

    def alterar_valor(self, valor_litro):
        self.valor_litro = valor_litro

    def alterar_combustivel(self, tipo_combustivel):
        self.tipo_combustivel = tipo_combustivel
# =====================================================================================================================================
# EX_7:
class Carro:
    def __init__(self, consumo_combustivel, combustivel_tanque = 0):
        self.consumo_combustivel = consumo_combustivel
        self.combustivel_tanque = combustivel_tanque

    def andar(self, km):
        self.consumo_ao_andar(km)
    
    def obter_gasolina(self):
        estimativa_km = self.consumo_combustivel * self.combustivel_tanque
        print(('*')*60)
        print(f'Possui {self.combustivel_tanque:.4} litros de combustivel, pode rodar {estimativa_km:.4} km ')
        print(('*')*60)
    def adicionar_gasolina(self, quantidade):
        self.combustivel_tanque += quantidade

    def consumo_ao_andar(self,km):
        consumo = km / self.consumo_combustivel
        self.combustivel_tanque -= consumo
# =====================================================================================================================================
