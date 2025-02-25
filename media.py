numeros = []

while True:
    entrada = input("Digite um número ou '[Y]' para calcular: ").strip().lower()
    
    if entrada == 'y':
        if len(numeros) == 0:
            print("É necessário pelo menos dois valores para calcular a média.")
        elif len(numeros) == 1:
            print("Não é possível calcular a média com apenas um valor.")
        else:
            media = sum(numeros) / len(numeros)
            print(f"A média dos números digitados é: {media:.2f}")
            break
    else:
        try:
            numero = float(entrada)
            numeros.append(numero)
        except ValueError:
            print("Comando não encontrado. Digite um número ou '[Y]' para calcular.")
