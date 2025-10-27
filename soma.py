def somar_numeros():
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = num1 + num2
        print(f"A soma de {num1} + {num2} é: {resultado}")
    except ValueError:
        print("Por favor, digite apenas números válidos.")

if __name__ == "__main__":
    somar_numeros()