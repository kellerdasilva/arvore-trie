# Autocomplemento e aprendizado de palavras com árvore trie

Trabalho de Estrutura de Dados – Árvore trie

**Autores:** Lucas Keller da Silva e Matheus Soares Ouriques

## Descrição

Programa interativo de terminal que mantém um dicionário de palavras em memória usando uma **trie N-ária** (árvore de prefixos) e oferece:

- **Autocomplemento por prefixo:** dado um prefixo, lista até 3 palavras conhecidas que começam com ele.
- **Aprendizado de palavras:** se nenhuma palavra conhecida começa com o termo pesquisado, o sistema oferece inseri-lo na árvore em tempo de execução.
- **Persistência:** o dicionário é carregado de `dicionario.txt` ao iniciar e salvo no mesmo arquivo ao encerrar.

## Estrutura do repositório

| Arquivo | Conteúdo |
|---|---|
| `trie.py` | Classes `NoTrie` e `Trie` (estrutura de dados e algoritmos) |
| `main.py` | Interface de terminal (menu, busca, aprendizado, persistência) |
| `dicionario.txt` | Dicionário de palavras (uma por linha) |
| `README.md` | Esta documentação |

## Como executar

Requer Python 3. Na pasta do projeto:

```
python main.py
```

O arquivo `dicionario.txt` deve estar na mesma pasta de onde o programa é executado. Se ele não existir, o programa inicia com a árvore vazia e o cria ao encerrar.

### Menu

```
1 - Buscar / autocompletar
2 - Inserir palavra
3 - Listar todas as palavras
0 - Salvar e sair
```

### Exemplo de uso

Com o `dicionario.txt` inicial (`amor`, `amarelo`, `casa`, `carro`, `cachorro`):

```
5 palavra(s) carregada(s) de dicionario.txt.
Opção: 1
Digite o prefixo: ca
Sugestões:
  - cachorro
  - carro
  - casa

Opção: 1
Digite o prefixo: zebra
Nenhuma palavra conhecida começa com 'zebra'.
Deseja que o sistema aprenda esta palavra? (s/n): s
Palavra 'zebra' aprendida.

Opção: 0
6 palavra(s) salva(s) em dicionario.txt.
```

## Como a Trie funciona

Cada nó guarda **um caractere** (a chave no dicionário do nó pai) e uma coleção de filhos. Palavras com o mesmo prefixo compartilham o caminho inicial. Exemplo com `amor`, `amarelo`, `casa`, `carro` e `cachorro`:

```
raiz
├── a
│   └── m
│       ├── o ── r*            (amor)
│       └── a ── r ── e ── l ── o*   (amarelo)
└── c
    ├── a
    │   ├── s ── a*            (casa)
    │   ├── r ── r ── o*       (carro)
    │   └── c ── h ── o ── r ── r ── o*   (cachorro)
```

`*` marca um nó de **fim de palavra**.

A árvore é **N-ária**: em vez de um array de 26 ponteiros, cada nó usa um dicionário Python (`self.filhos`), que cria apenas os ponteiros para os caracteres que realmente existem.

## Classes e métodos

### `NoTrie`

| Atributo | Descrição |
|---|---|
| `filhos` | Dicionário `{caractere: NoTrie}` com os nós seguintes |
| `eh_fim_de_palavra` | `True` se o caminho até este nó forma uma palavra válida |

### `Trie`

| Método | Descrição |
|---|---|
| `inserir(palavra)` | Insere a palavra criando os nós necessários. Retorna `True` se a palavra era nova; `False` se já existia, se é vazia ou se contém espaços |
| `buscar_prefixo(prefixo)` | Percorre a árvore pelo prefixo e retorna o nó do último caractere, ou `None` se o prefixo não existe (ou é vazio) |
| `autocompletar(prefixo, limite=3)` | Combina `buscar_prefixo` e a coleta de palavras; retorna uma lista com até `limite` palavras que começam com o prefixo |
| `_coletar_palavras(no, prefixo, resultado, limite)` | Busca em profundidade a partir de um nó, visitando os filhos em ordem alfabética e parando ao atingir o `limite` |
| `listar_palavras()` | Retorna todas as palavras da árvore, em ordem alfabética |
| `existe_palavra(palavra)` | Verifica se a palavra completa está cadastrada (e não apenas como prefixo de outra) |
| `carregar_dicionario(caminho)` | Lê o arquivo (uma palavra por linha) e insere na árvore; retorna quantas palavras novas foram inseridas |
| `salvar_dicionario(caminho)` | Grava todas as palavras da árvore no arquivo, uma por linha; retorna quantas foram gravadas |
| `normalizar(palavra)` | Remove espaços das extremidades e converte para minúsculas |

## Decisões de projeto

- **Normalização:** todas as palavras e prefixos são convertidos para minúsculas e têm espaços das extremidades removidos, então `Casa`, `CASA` e ` casa ` são a mesma palavra.
- **Uma palavra por entrada:** entradas vazias ou com espaços no meio são rejeitadas.
- **Ordem das sugestões:** os filhos são percorridos em ordem alfabética, então as sugestões saem sempre ordenadas.
- **Limite de sugestões:** a coleta para assim que atinge 3 palavras, sem percorrer o resto da subárvore.
- **Aprendizado com confirmação:** quando o prefixo não tem nenhuma palavra associada, o programa pergunta antes de inserir, para evitar cadastrar erros de digitação.
- **Salvamento garantido:** o dicionário é salvo em um bloco `finally`, inclusive se o programa for interrompido com Ctrl+C.
- **Separação de responsabilidades:** `trie.py` não faz nenhuma entrada/saída de terminal; toda a interação fica em `main.py`.

## Complexidade

Sendo `L` o tamanho da palavra ou prefixo:

| Operação | Custo |
|---|---|
| `inserir` | O(L) |
| `buscar_prefixo` | O(L) |
| `existe_palavra` | O(L) |
| `autocompletar` | O(L) para localizar o prefixo, mais o percurso da subárvore até encontrar `limite` palavras |
| `listar_palavras` / `salvar_dicionario` | Proporcional ao número de nós da árvore |

O custo de busca e inserção depende só do tamanho da palavra, e não da quantidade de palavras cadastradas.

## Persistência

- **Formato:** texto simples, uma palavra por linha, em UTF-8.
- **Ao iniciar:** cada linha é normalizada e inserida na árvore; linhas vazias, duplicadas ou com espaços são ignoradas.
- **Ao encerrar:** o arquivo é sobrescrito com todas as palavras da árvore em ordem alfabética.

## Funcionalidades extras

_(a atualizar)_
