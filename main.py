# Trabalho de Estruturas de Dados - autocomplemento e aprendizado de palavras com árvore trie
# Autores: Lucas Keller da Silva e Matheus Soares Ouriques

from arvore_trie import Trie

ARQUIVO = "dicionario.txt"

# Busca por prefixo; se nada for encontrado, oferece aprender a palavra
def buscar_e_aprender(trie):
    entrada = input("Digite o prefixo: ").strip().lower()

    # Rejeita entrada vazia ou com espaços no meio
    if entrada == "" or len(entrada.split()) > 1:
        print("Entrada inválida: digite uma única palavra ou prefixo.")
        return

    sugestoes = trie.autocompletar(entrada, 3)

    if len(sugestoes) > 0:
        print("Sugestões:")
        for palavra in sugestoes:
            print("  -", palavra)
    else:
        # Termo inexistente: o sistema aprende a nova palavra
        print("Nenhuma palavra conhecida começa com '" + entrada + "'.")
        resposta = input("Deseja que o sistema aprenda esta palavra? (s/n): ").strip().lower()
        if resposta == "s":
            trie.inserir(entrada)
            print("Palavra '" + entrada + "' aprendida.")


# Insere uma palavra digitada diretamente
def inserir_palavra(trie):
    palavra = input("Digite a palavra a cadastrar: ")
    if trie.inserir(palavra):
        print("Palavra cadastrada.")
    else:
        print("Não cadastrada (vazia, com espaços ou já existente).")


# Lista todas as palavras da árvore
def listar_todas(trie):
    palavras = trie.listar_palavras()
    if len(palavras) == 0:
        print("Dicionário vazio.")
    else:
        print(str(len(palavras)) + " palavra(s):")
        for palavra in palavras:
            print("  -", palavra)


def main():
    trie = Trie()

    # Carrega o dicionário ao iniciar
    total = trie.carregar_dicionario(ARQUIVO)
    print(str(total) + " palavra(s) carregada(s) de " + ARQUIVO + ".")

    try:
        while True:
            print("\n=== AUTOCOMPLETAR (TRIE) ===")
            print("1 - Buscar / autocompletar")
            print("2 - Inserir palavra")
            print("3 - Listar todas as palavras")
            print("0 - Salvar e sair")
            opcao = input("Opção: ").strip()

            if opcao == "1":
                buscar_e_aprender(trie)
            elif opcao == "2":
                inserir_palavra(trie)
            elif opcao == "3":
                listar_todas(trie)
            elif opcao == "0":
                break
            else:
                print("Opção inválida.")
    except (KeyboardInterrupt, EOFError):
        print("\nEncerrando...")
    finally:
        # Salva o dicionário ao encerrar
        salvas = trie.salvar_dicionario(ARQUIVO)
        print(str(salvas) + " palavra(s) salva(s) em " + ARQUIVO + ".")


if __name__ == "__main__":
    main()
