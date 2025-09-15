# Analisador Sintático Preditivo LL(1) – Declarações de Variáveis

## 📚 Descrição

Este projeto implementa um **analisador sintático preditivo LL(1)** para validação de **declarações de variáveis** em uma linguagem simples. A gramática utilizada suporta tipos primitivos (`int`, `float`, `char`) e múltiplos identificadores por linha.

## 🧾 Gramática

S → D S | ε

D → T L ;

T → int | float | char

L → id L′

L′ → , id L′ | ε

- **Símbolo inicial:** `S`
- **Não-terminais (VN):** {S, D, T, L, L′}
- **Terminais (VT):** {int, float, char, id, ,, ;, $}

### ✅ Exemplos de cadeias válidas

int x;

float a, b, c;

char c1;

int x; float y; char z;

### ❌ Exemplos de cadeias inválidas

int ; // falta identificador

float , a; // vírgula no lugar errado

char a b; // falta vírgula

## Conjuntos First

First(S) = { int, float, char, ε }

First(D) = { int, float, char }

First(T) = { int, float, char }

First(L) = { id }

First(L′) = { ,, ε }

## Conjuntos Follow

Follow(S) = { $ }

Follow(D) = { int, float, char, $ }

Follow(T) = { id }

Follow(L) = { ; }

Follow(L′) = { ; }

## 📋 Tabela LL(1)

A tabela de análise LL(1) foi construída a partir dos conjuntos **First** e **Follow** para orientar o algoritmo na escolha das produções.

## 💻 Implementação

A implementação foi realizada em **Python**, utilizando:

- Uma **pilha** para armazenar os símbolos em análise.
- Uma **tabela LL(1)** representada como dicionário.
- Consumo de tokens até o símbolo de fim de cadeia (`$`).

## 🧪 Testes

Foram aplicados testes com cadeias **válidas** e **inválidas**:

| Cadeia               | Resultado |
| -------------------- | --------- |
| `int id ;`           | Aceita    |
| `float id , id ;`    | Aceita    |
| `int id ; char id ;` | Aceita    |
| `int ;`              | Rejeita   |

## Conclusão

A implementação permitiu compreender na prática o funcionamento de um **analisador sintático preditivo LL(1)**.  
O cálculo correto dos conjuntos **First** e **Follow** foi essencial para construir a tabela de análise, garantindo que o programa validasse corretamente as sentenças válidas e rejeitasse as inválidas.

## 👥 Autores

- Julia Gomes
- Tuliana Andrade

📍 _Universidade Federal de Mato Grosso – Instituto de Computação – 2025_
