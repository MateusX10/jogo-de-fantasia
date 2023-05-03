from strings import titulo, TextoColorido

class Heroi:
    '''
    Esta classe servirá como superclasse para as classes que represenram classes de herói, como
    cavalheiro, mago, bruxa, etc...
    
    Atributos:

        nome (str): o nome do herói.
        dano (int): o dano que esse herói causa.
        defesa (int): a defesa desse herói.
        vida (int): os pontos de vida desse herói.
        ataque_especial: golpe especial do herói ("special move").
    '''

    def __init__(self, nome: str, dano: int, defesa: int,  vida: str, ataque_especial: int):
        '''
        O construtor da classe herói

        Parâmetros:

            nome (str): nome do herói
            dano (int): o dano que esse herói causa
            defesa (int): a defesa desse herói
            vida (int): os pontos de vida desse herói
            ataque_especial (int): ataque especial desse herói

            
        '''

        self.nome = nome
        self.dano = dano
        self.defesa = defesa
        self.vida = vida
        self.especial = ataque_especial


    def ExibirInformaçõesDoHeroi(self) -> None:
        titulo(msg=f"Informações do {type(self).__name__} ", cor="azul")
        TextoColorido(f'''Nome: {self.nome}\tDano: {self.dano}\tDefesa: {self.defesa}\n
Vida: {self.vida}\t Ataque especial: {self.especial}''', "cinza")


class Cavalheiro(Heroi):
    '''
    Subclasse "cavalheiro" da superclasse "monstro"
    
    Parâmetros:

        nome (str): nome do cavalheirop
        dano (int): dano que esse cavalheiro causa
        defesa (int): defesa que esse cavalheiro possui
        vida (int): os pontos de vida desse cavalheiro
        especial (int): o ataque especial desse cavalheiro ("special move")
        
        '''
    

    def __init__(self, nome):

        super().__init__(nome, dano=20, defesa=10, vida=1200, ataque_especial=40)




# Subclasse de "herói"    
class Mago(Heroi):
    '''
    Subclasse "mago" da classe "herói"

    Atributos:

        nome (str): nome do mago
        dano (int): dano que esse mago causa
        defesa (int): defesa que esse mago possui
        vida (int): os pontos de vida desse mago
        especial (int): o ataque especial desse mago ("special move")

    '''

    def __init__(self, nome: str):
        '''
        Construtor da classe "Mago".

        Parâmetros:

            nome (str): nome do mago
            dano (int): o dano que esse mago causa
            defesa (int): defesa do mago
            vida (int): pontos de vida do mago
            especial (int): golpe especial do mago ("special move")
        '''


        super().__init__(nome, dano=50, defesa=5, vida=1000, ataque_especial=300)


    




