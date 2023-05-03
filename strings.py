def ApagaCor() -> None:
    '''
    Remove a cor de um texto
    '''
    print("\033[m")


def FormataCor(cor_de_fundo: str) -> str:
    '''==> Retorna a cor em código escape ANSI normal ou em RGB (a preferência do usuário)
        :param cor: cor a ser atribuída ao texto (vermelho, verde, azul)
        :return: retorna a cor formatada em RGB
    '''
    cores = {"cinza": "\033[1;100m", "preto": "\033[1;40m",
            "vermelho": "\033[1m\033[48;2;128;0;0m",
            "verde": "\033[1m\033[48;2;0;128;0m",
            "azul": "\033[1m[\033[48;2;0;0;128m",
            "amarelo": "\033[1;43m", "azul": "\033[1;44m", 
            "magenta": "\033[1;45m", "ciano": "\033[1;46m",
            "branco": "\033[1;47m"}
    
    return cores[cor_de_fundo]


def linha(tamanho: int = 60) -> None:
    '''
    Imprime uma linha na tela
    :param tamanho int: tamanho da linha a ser imprimida
    :return: sem retorno
    '''
    print('-=' * tamanho)


def titulo(msg: str, cor: str) -> None:
    '''==> Imprime um título na tela
        :param msg: mensagem do título a ser mostrada
        :param cor: cor do texto do título emk RGB
        :return: sem retorno     
    '''
    tamanho = len(msg) + 2
    print(FormataCor(cor))
    linha(tamanho)
    print(msg.center(tamanho * 2))
    linha(tamanho)
    ApagaCor()


def TextoColorido(msg: str, cor: str) -> None:
    '''==> Imprime um texto colorido na tela
        :param msg: mensagem do título a ser mostrada
        :param cor: cor do texto do título emk RGB
        :return: sem retorno     
    '''    
    print(f"{FormataCor(cor)}{msg}{ApagaCor()}")
    


