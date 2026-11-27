"""Identificador de números pares e ímpares.

O programa recebe números inteiros, separa-os em duas listas e apresenta um resumo dos resultados.
"""

def solicitar_quantidade():
    """Solicita a quantidade de números que serão analisados."""
    while True:
        try:
            quantidade = int(
                input("Quantos números você deseja informar? ")
            )

            if quantidade > 0:
                return quantidade

            print("A quantidade deve ser maior que zero.")

        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

def solicitar_numero(posicao):
    """Solicita e valida um número inteiro."""
    while True:
        try:
            return int(
                input(f"Digite o {posicao}º número inteiro: ")
            )

        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

def separar_numeros(numeros):
    """Separa os números recebidos em pares e ímpares."""
    pares = []
    impares = []

    for numero in numeros:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)

    return pares, impares

def calcular_soma(numeros):
    """Calcula a soma dos valores de uma lista."""
    return sum(numeros)

def main():
    """Executa o programa principal."""
    print("=" * 42)
    print("       IDENTIFICADOR DE PARES E ÍMPARES")
    print("=" * 42)

    quantidade = solicitar_quantidade()
    numeros = []

    for posicao in range(1, quantidade + 1):
        numero = solicitar_numero(posicao)
        numeros.append(numero)

    pares, impares = separar_numeros(numeros)

    print("\nResultado")
    print("-" * 42)
    print(f"Números informados: {numeros}")
    print(f"Números pares: {pares}")
    print(f"Números ímpares: {impares}")
    print(f"Quantidade de pares: {len(pares)}")
    print(f"Quantidade de ímpares: {len(impares)}")
    print(f"Soma dos números pares: {calcular_soma(pares)}")
    print(f"Soma dos números ímpares: {calcular_soma(impares)}")

if __name__ == "__main__":
    main()
