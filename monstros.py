class Monstro:
    '''
    Esta classe servirá como superclasse para as classes que representam classes de monstro, como
    goblin, esqueleto, múmia etc...

    Atributos:

        dano (int): dano que o monstro causa
        defesa (int): defesa do monstro
        vida (int): pontos de vida do monstro
        ataque_especial (int): o ataque especial do monstro
    '''

    def __init__(self, dano: int, defesa: int, vida: int, ataque_especial: int):
        '''
        Construtor da classe monstro

        Parâmetros:

            dano (int): dano que o monstro causa
            defesa (int): defesa do monstro
            vida (int): pontos de vida do monstro
            ataque_especial (int): o ataque especial do monstro
        '''

        self.dano = dano
        self.defesa = defesa
        self.vida = vida
        self.especial = ataque_especial



class Goblin(Monstro):
    '''
    Subclasse "globin" da superclasse monstro

    Parâmetros:

        dano (int): dano que o monstro causa
        defesa (int): defesa que esse monstro possui
        vida (int): pontos de vida do monstro
        ataque_especial (int): ataque especial do monstro

    '''

    def __init__(self):
        '''
        Construtor da classe "goblin"

        Parâmetros:
        
            dano (int): dano que o monstro causa
            defesa (int): defesa que esse monstro possui
            vida (int): pontos de vida do monstro
            ataque_especial (int): ataque especial do monstro
        '''
        super().__init__(dano=5, defesa=1, vida=480, ataque_especial=30)



