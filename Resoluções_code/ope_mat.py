# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

# Solicita dois números do usuário
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Solicita a operação desejada
operacao = input("Escolha a operação (+, -, *, /): ")

# Realiza a operação escolhida
if operacao == "+":
    resultado = numero1 + numero2
elif operacao == "-":
    resultado = abs( numero1 - numero2)
elif operacao == "*":
    resultado = numero1 * numero2
elif operacao == "/":
    if numero2 != 0:
        resultado = numero1 / numero2
    else:
        resultado = "Erro: divisão por zero não é permitida!"
else:
    resultado = "Operação inválida!"

# Exibe o resultado
print("O resultado é:", resultado)
