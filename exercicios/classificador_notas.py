"""Classificador de notas.

O programa solicita a nota e a frequência de um estudante
e determina sua situação acadêmica.
"""

def solicitar_nota():
    """Solicita e valida uma nota entre 0 e 10."""
    while True:
        try:
            nota = float(
                input("Digite a nota final, entre 0 e 10: ")
                .replace(",", ".")
            )

            if 0 <= nota <= 10:
                return nota

            print("A nota deve estar entre 0 e 10.")

        except ValueError:
            print("Entrada inválida. Digite somente números.")

def solicitar_frequencia():
    """Solicita e valida uma frequência entre 0% e 100%."""
    while True:
        try:
            frequencia = float(
                input("Digite a frequência do estudante, em %: ")
                .replace(",", ".")
            )

            if 0 <= frequencia <= 100:
                return frequencia

            print("A frequência deve estar entre 0% e 100%.")

        except ValueError:
            print("Entrada inválida. Digite somente números.")

def classificar_desempenho(nota):
    """Classifica o desempenho com base na nota."""
    if nota >= 9:
        return "Excelente"

    if nota >= 7:
        return "Bom"

    if nota >= 5:
        return "Regular"

    return "Insuficiente"

def determinar_situacao(nota, frequencia):
    """Determina a situação acadêmica do estudante."""
    frequencia_minima = 75

    if frequencia < frequencia_minima:
        return "Reprovado por frequência"

    if nota >= 7:
        return "Aprovado"

    if nota >= 5:
        return "Recuperação"

    return "Reprovado por nota"

def main():
    """Executa o programa principal."""
    print("=" * 42)
    print("         CLASSIFICADOR DE NOTAS")
    print("=" * 42)

    nome = input("Digite o nome do estudante: ").strip()

    if not nome:
        nome = "Estudante"

    nota = solicitar_nota()
    frequencia = solicitar_frequencia()

    desempenho = classificar_desempenho(nota)
    situacao = determinar_situacao(nota, frequencia)

    print("\nResultado")
    print("-" * 42)
    print(f"Estudante: {nome}")
    print(f"Nota final: {nota:.2f}")
    print(f"Frequência: {frequencia:.1f}%")
    print(f"Desempenho: {desempenho}")
    print(f"Situação: {situacao}")

if __name__ == "__main__":
    main()
