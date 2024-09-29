# Crie um programa que receba uma quantidade indefinida de números do usuário. O programa deve calcular a média desses números e parar quando o usuário digitar -1.
soma_dos_numeros = 0
quant = 0
numero = 0

while numero != -1:
    numero = int(input('Digite um numero: '))

    if numero == -1:
        break
    
    soma_dos_numeros = soma_dos_numeros + numero
    quant = quant + 1
   
print(f"A média dos numeros é : {soma_dos_numeros/quant}")

