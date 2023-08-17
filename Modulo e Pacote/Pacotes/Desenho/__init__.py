def desenhar_gato():
    gato = r"""
 /\_/\  
( o.o ) 
 > ^ <
"""
    return gato

def desenhar_cachorro():
    cachorro = r"""
   / \__
  (    @\____
  /         O
 /   (_____/
/_____/   U
"""
    return cachorro

def desenhar_peixe():
    peixe = r"""
><(((º>
"""
    return peixe

def desenhar_tartaruga():
    tartaruga = r"""
  ___
 /0  \
 \___/
"""
    return tartaruga

def desenhar_leao():
    leao = r"""
   \    ____
    \  /    \
      | ^  ^ |
      |      |
       \____/
"""
    return leao

def desenhar_cavalo():
    cavalo = r"""
      ,/'  | 
     ( =   | 
      / |  |
      | ^  |
     /  -  \ 
    /  -  \ \
   ( ~    ) )
    \    / /
     |  | | 
    / ^  | \
   /_/ |_/  
"""
    return cavalo

def cor_texto(texto, cor):
    cores = {
        'vermelho': '\033[91m',
        'verde': '\033[92m',
        'amarelo': '\033[93m',
        'azul': '\033[94m',
        'roxo': '\033[95m',
        'reset': '\033[0m'
    }
    return cores.get(cor, '') + texto + cores['reset']

