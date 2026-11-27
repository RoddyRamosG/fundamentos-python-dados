"""Conversor de temperatura.

Este programa realiza conversões entre:
- Celsius e Fahrenheit;
- Fahrenheit e Celsius.
"""

def solicitar_temperatura():
    """Solicita uma temperatura e valida a entrada."""
    while True:
        try:
            valor = input("Digite a temperatura: ").replace(",", ".")
            return float(valor)

        except ValueError:
            print("Entrada inválida. Digite somente números.")

def celsius_para_fahrenheit(celsius):
    """Converte uma temperatura de Celsius para Fahrenheit."""
    return (celsius * 9 / 5) + 32

def fahrenheit_para_celsius(fahrenheit):
    """Converte uma temperatura de Fahrenheit para Celsius."""
    return (fahrenheit - 32) * 5 / 9

def mostrar_menu():
    """Apresenta as opções de conversão."""
    print("=" * 42)
    print("        CONVERSOR DE TEMPERATURA")
    print("=" * 42)
    print("1 - Celsius para Fahrenheit")
    print("2 - Fahrenheit para Celsius")
    print("0 - Sair")

def main():
    """Executa o programa principal."""
    while True:
        mostrar_menu()

        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == "0":
            print("\nPrograma encerrado.")
            break

        if opcao not in ("1", "2"):
            print("\nOpção inválida. Escolha 1, 2 ou 0.\n")
            continue

        temperatura = solicitar_temperatura()

        if opcao == "1":
            resultado = celsius_para_fahrenheit(temperatura)

            print(
                f"\n{temperatura:.2f} °C corresponde a "
                f"{resultado:.2f} °F.\n"
            )

        else:
            resultado = fahrenheit_para_celsius(temperatura)

            print(
                f"\n{temperatura:.2f} °F corresponde a "
                f"{resultado:.2f} °C.\n"
            )

if __name__ == "__main__":
    main()
