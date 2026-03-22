# 🎓 Curso Rápido de JSON: Do Zero ao Profissional

> **Bem-vindo às aulas do Professor PolyDB!** Aqui você aprendeu a base da troca de dados entre sistemas modernos.

---

## 📋 Tabela de Referência (Regras de Ouro)

| Tipo de Dado | Exemplo | Regra |
| :--- | :--- | :--- |
| **Texto (String)** | `"Venda Ativa"` | Sempre entre aspas duplas `" "`. |
| **Número (Number)** | `450.00` | Sem aspas, usa ponto `.` para decimais. |
| **Booleano (Bool)** | `true` ou `false` | Representa Verdadeiro/Falso (minúsculas). |
| **Lista (Array)** | `["A", "B"]` | Coleção de itens entre colchetes `[ ]`. |
| **Objeto (Object)** | `{ "id": 1 }` | Uma sub-ficha completa entre chaves `{ }`. |

---

## 📚 Aula 1: O Que é o JSON? (O Conceito)

**JSON** (*JavaScript Object Notation*) é o "idioma oficial" que os computadores usam para conversar entre si. Imagine que é uma **ficha de cadastro digital**.

### 📝 Estrutura Básica:
1.  **Chave e Valor:** Tudo funciona via ` "nome": "valor" `.
2.  **Aspas Duplas:** SEMPRE use `" "` para as chaves e textos.
3.  **Contêiner:** Começa e termina com chaves `{ }`.

---

## 🏗️ Aula 2: A Fábrica de JSON (Como o Programador Usa?)

Programadores não escrevem JSON na mão o tempo todo. Eles usam ferramentas que transformam **Código** em **JSON** e vice-versa.

- **`json.dumps` (Empacotar):** Transforma variáveis do código em texto JSON para enviar.
- **`json.loads` (Desempacotar):** Transforma o texto JSON recebido em dados que o código entende.

---

## 🧠 Aula 3: Símbolos e Erros Comuns

O computador é extremamente rigoroso com a pontuação.

- `{ }` (Chaves): Representam um **Objeto** (uma coisa única).
- `[ ]` (Colchetes): Representam uma **Lista** (várias coisas juntas).
- `: ` (Dois pontos): É o sinal de **Atribuição** ("Isso é aquilo").
- `, ` (Vírgula): É o **Separador** ("Acabei esse item, vamos para o próximo").

### ❌ Cuidado com:
1.  **Aspas Simples:** No JSON, usar `' '` é proibido!
2.  **Vírgulas:** Nunca esqueça entre itens e **nunca coloque no final** do último item.

---

## 🪆 Aula 4: O "Modo Boneca Russa" (Objetos Aninhados)

Na vida real, informações têm sub-detalhes. Podemos colocar um objeto **dentro** de outro para organizar melhor.

**Exemplo de Venda com Detalhes do Cliente:**
```json
{
  "id_venda": 101,
  "data": "2026-03-18",
  "cliente": {
    "nome": "Rilen T. L.",
    "email": "rilen@example.com",
    "cidade": "Rio das Ostras"
  },
  "valor": 1200.50
}
```
> No exemplo acima, o `cliente` é um objeto inteiro dentro da venda. O programador acessa o nome usando `venda.cliente.nome`. É assim que endereços e perfis são organizados!

---
*Professor PolyDB — 2026*
