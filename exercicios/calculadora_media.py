"""Calculadora de média de notas.

Este programa solicita três notas, calcula a média aritmética e apresenta a situação do estudante.
"""

def solicitar_nota(numero):
    """Solicita e valida uma nota entre 0 e 10."""
    while True:
        try:
            nota = float(
                input(f"Digite a {numero}ª nota, entre 0 e 10: ")
                .replace(",", ".")
            )

            if 0 <= nota <= 10:
                return nota

            print("A nota deve estar entre 0 e 10.")

        except ValueError:
            print("Entrada inválida. Digite somente números.")


def calcular_media(notas):
    """Calcula a média aritmética de uma lista de notas."""
    return sum(notas) / len(notas)


def classificar_resultado(media):
    """Classifica o resultado com base na média."""
    if media >= 7:
        return "Aprovado"

    if media >= 5:
        return "Recuperação"

    return "Reprovado"


def main():
    """Executa o programa principal."""
    print("=" * 35)
    print("      CALCULADORA DE MÉDIA")
    print("=" * 35)

    notas = [
        solicitar_nota(1),
        solicitar_nota(2),
        solicitar_nota(3),
    ]

    media = calcular_media(notas)
    resultado = classificar_resultado(media)

    print("\nResultado")
    print("-" * 35)
    print(f"Notas informadas: {notas}")
    print(f"Média final: {media:.2f}")
    print(f"Situação: {resultado}")

if __name__ == "__main__":
    main()
