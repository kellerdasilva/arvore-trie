
# Classe que representa cada nó da Árvore Trie
class NoTrie:

    # Método construtor do nó
    def __init__(self):
        self.filhos = {}  # Dicionário que armazena os caracteres seguintes
        self.eh_fim_de_palavra = False  # Indica se o nó termina uma palavra

# Classe responsável pela Árvore Trie
class Trie:

    # Método construtor da árvore
    def __init__(self):
        self.raiz = NoTrie()  # Cria o nó raiz da árvore


    # Método responsável por inserir uma palavra na árvore
    def inserir(self, palavra):

        # Remove espaços nas extremidades e padroniza as letras
        palavra = palavra.strip().lower()

        # Verifica se a palavra está vazia
        if palavra == "":
            return False

        # Começa a inserção a partir da raiz
        no_atual = self.raiz

        # Percorre cada caractere da palavra
        for caractere in palavra:

            # Verifica se o caractere ainda não existe entre os filhos
            if caractere not in no_atual.filhos:
                # Cria um novo nó para o caractere
                no_atual.filhos[caractere] = NoTrie()

            # Avança para o nó correspondente ao caractere
            no_atual = no_atual.filhos[caractere]

        # Verifica se a palavra já estava cadastrada
        if no_atual.eh_fim_de_palavra == True:
            return False

        else:
            # Marca o último nó como final de uma palavra válida
            no_atual.eh_fim_de_palavra = True
            return True

    # Método responsável por localizar um prefixo na árvore
    def buscar_prefixo(self, prefixo):

        # Remove espaços nas extremidades e padroniza as letras
        prefixo = prefixo.strip().lower()

        # Verifica se o prefixo está vazio
        if prefixo == "":
            return None

        # Começa a busca a partir da raiz
        no_atual = self.raiz

        # Percorre cada caractere do prefixo
        for caractere in prefixo:

            # Verifica se o caractere não existe entre os filhos
            if caractere not in no_atual.filhos:
                return None

            else:
                # Avança para o próximo nó
                no_atual = no_atual.filhos[caractere]

        # Retorna o nó correspondente ao último caractere do prefixo
        return no_atual
