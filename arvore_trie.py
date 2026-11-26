# Trabalho de Estruturas de Dados - autocomplemento e aprendizado de palavras com árvore trie
# Autores: Lucas Keller da Silva e Matheus Soares Ouriques

import os # Importa o módulo OS da biblioteca padrão do Python

# Classe que representa cada nó da Árvore Trie
class NoTrie:
    # Construtor do nó
    def __init__(self):
        self.filhos = {}  # Dicionário que armazena os caracteres seguintes
        self.eh_fim_de_palavra = False  # Indica se o nó termina uma palavra


# Classe responsável pela Árvore Trie
class Trie:
    # Construtor da árvore
    def __init__(self):
        self.raiz = NoTrie()  # Cria o nó raiz da árvore

    # Insere uma palavra na árvore
    def inserir(self, palavra):
        # Remove espaços nas extremidades e padroniza as letras
        palavra = self.normalizar(palavra)

        # Rejeita palavras vazias ou com espaços no meio (a Trie guarda uma palavra por vez)
        if palavra == "" or len(palavra.split()) > 1:
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
        if no_atual.eh_fim_de_palavra:
            return False
        else:
            # Marca o último nó como final de uma palavra válida
            no_atual.eh_fim_de_palavra = True
            return True

    # Localiza um prefixo na árvore
    def buscar_prefixo(self, prefixo):
        # Remove espaços nas extremidades e padroniza as letras
        prefixo = self.normalizar(prefixo)

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
    
    # Retorna até 'limite' palavras que começam com o prefixo (ou lista vazia se não houver nenhuma)
    def autocompletar(self, prefixo, limite=3):
        # Padroniza o prefixo
        prefixo = self.normalizar(prefixo)

        # Localiza o nó correspondente ao último caractere do prefixo
        no_prefixo = self.buscar_prefixo(prefixo)

        # Lista que receberá as sugestões
        resultado = []

        # Se o prefixo existe, coleta as palavras da subárvore a partir dele
        if no_prefixo is not None:
            self._coletar_palavras(no_prefixo, prefixo, resultado, limite)

        return resultado
    
    # Coleta todas as palavras a partir de um nó (busca em profundidade)
    def _coletar_palavras(self, no, prefixo, resultado, limite=None):
        # Se já atingiu o limite de palavras desejado, interrompe a busca
        if limite is not None and len(resultado) >= limite:
            return

        # Se o nó atual marca o fim de uma palavra, adiciona o prefixo acumulado ao resultado
        if no.eh_fim_de_palavra:
            resultado.append(prefixo)

        # Percorre os filhos em ordem alfabética
        for caractere in sorted(no.filhos):

            # Chama a função para o filho, acrescentando o caractere ao prefixo
            self._coletar_palavras(no.filhos[caractere], prefixo + caractere, resultado, limite)

            # Interrompe o laço se o limite já foi atingido
            if limite is not None and len(resultado) >= limite:
                return
    
    # Carrega as palavras do arquivo para a Trie
    def carregar_dicionario(self, caminho="dicionario.txt"):
        # Se o arquivo não existir, não há nada a carregar
        if not os.path.exists(caminho):
            return 0

        # Contador de palavras novas inseridas
        total = 0

        # Abre o arquivo para leitura
        with open(caminho, "r", encoding="utf-8") as arquivo:

            # Lê o arquivo linha por linha
            for linha in arquivo:

                # Normaliza a palavra lida
                palavra = self.normalizar(linha)

                # Insere na árvore e conta se foi uma palavra nova
                if self.inserir(palavra):
                    total += 1

        return total
    
    # Salva todas as palavras da Trie no arquivo
    def salvar_dicionario(self, caminho="dicionario.txt"):
        # Obtém todas as palavras armazenadas na árvore
        palavras = self.listar_palavras()

        # Abre o arquivo para escrita (sobrescreve o conteúdo anterior)
        with open(caminho, "w", encoding="utf-8") as arquivo:

            # Grava uma palavra por linha
            for palavra in palavras:
                arquivo.write(palavra + "\n")

        return len(palavras)
    
    # Lista todas as palavras armazenadas na Trie
    def listar_palavras(self):
        # Lista que receberá as palavras encontradas
        resultado = []

        # Coleta as palavras a partir da raiz, com prefixo vazio
        self._coletar_palavras(self.raiz, "", resultado)

        return resultado

    # Verifica se uma palavra completa existe na Trie
    def existe_palavra(self, palavra):
        # Remove espaços nas extremidades e padroniza as letras
        palavra = self.normalizar(palavra)

        # Verifica se a palavra está vazia
        if palavra == "":
            return False

        # Começa a busca a partir da raiz
        no_atual = self.raiz

        # Percorre cada caractere da palavra
        for caractere in palavra:

            # Se o caractere não existir, a palavra não está cadastrada
            if caractere not in no_atual.filhos:
                return False
            # Avança para o próximo nó
            else:
                no_atual = no_atual.filhos[caractere]

        # Verifica se o último nó marca o fim de uma palavra
        return no_atual.eh_fim_de_palavra
    
    # Padroniza uma palavra (sem espaços nas extremidades e em minúsculas)
    def normalizar(self, palavra):
        # Remove espaços nas extremidades e converte para minúsculas
        return palavra.strip().lower()
