numero = int(input('Digite um numero: '))
show =  ' '

while numero != 0 :
    resto =  numero % 2 
    if resto == 0:
        show = show + '0'
    else :
        show = show + '1'
    numero = numero // 2
    
  
    
print (show[::-1])
