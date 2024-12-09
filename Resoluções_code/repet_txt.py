# Vamos solicitar uma string e um número interio como entrada. Depois teremos que reotrnar a String repetida o número de vezes informado.

# Solicita uma string do usuário
texto = input("Digite uma string: ")

# Solicita um número inteiro do usuário
repeticoes = int(input("Digite um número inteiro: "))

# Retorna a string repetida o número de vezes informado
resultado = texto * repeticoes

# Exibe o resultado
print(f"A string repetida {repeticoes} vezes é: {resultado}")
