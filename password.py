import random           #sorteia a casa 
casa1 = random.randint(0,9)     
casa2 = random.randint(0,9)
casa3 = random.randint(0,9)
casa4 = random.randint(0,9)
casa5 = random.randint(0,9)
sorteada = (casa1, casa2, casa3, casa4, casa5)          # cria uma variavel para todas as casas sorteadas 
mostra=''


def teve_ganhador(mostra):       #verifica se houve ganhador
    if mostra == ' +1  +1  +1  +1  +1 ':
        return True
    else:
        return False

def mostra_ganhador(mostra):       #mostra se houve ganhador
    if mostra == ' +1  +1  +1  +1  +1 ':
        print ('voce ganhou!!!!')
        return True
    else:
        print ("voce perdeu!!")
        return False
    
def tentar():
    global mostra 
    tentativas = 0          
    while tentativas < 10 and not teve_ganhador(mostra):
        mostra=''
        senha = input('informe a senha: ')      #pede a senha
        aux1 = int (senha [0])
        aux2 = int (senha [1])
        aux3 = int (senha [2])
        aux4 = int (senha [3])
        aux5 = int (senha [4])
        
        if sorteada[0] == aux1:         #if verifica se cada caracter da senha inserida é compativel com o da senha sorteada)
            mostra += ' +1 '            # caso afirmativo printa +1 na dela
        elif aux1 in sorteada:          #elif verifica se o caracter da senha inserida esta na senha
            mostra += ' 0 '             # caso afirmativo, printa 0
        else:                           #else verifica caso o caracter nao estiver na senha 
            mostra += ' -1 '            #printa -1
            
        if sorteada[1] == aux2:
            mostra += ' +1 '   
        elif aux2 in sorteada:
            mostra += ' 0 ' 
        else:
            mostra += ' -1 '
            
        if sorteada[2] == aux3:
            mostra += ' +1 '
        elif aux3 in sorteada:
            mostra += ' 0 '
        else:
            mostra += ' -1 '
            
        if sorteada[3] == aux4 :
            mostra += ' +1 ' 
        elif aux4 in sorteada:
            mostra += ' 0 '
        else:
            mostra += ' -1 '
            
        if sorteada[4] == aux5:
            mostra += ' +1 '
        elif aux5 in sorteada:
            mostra += ' 0 '
        else :
            mostra += ' -1 '
            
        tentativas += 1             # contabiliza +1 as tentativas
        print(mostra)               # informa as tentativas da senha
    mostra_ganhador(mostra)       #verifica se teve ganhador de acordo c o parametro mostra

tentar()
print ('A SENHA SORTEADA FOI: ',sorteada)
