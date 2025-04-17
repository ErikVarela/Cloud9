# AWS Cloud9 + Amazon CodeWhisperer Lab

Este repositório contém os arquivos e anotações de um laboratório prático realizado utilizando o ambiente AWS Cloud9 e o Amazon CodeWhisperer. O objetivo foi explorar os recursos de geração de código assistido por IA em Python, como sugestões de função, preenchimento de blocos e linhas, além da integração com o ambiente da AWS.

---

## 🛠️ Tecnologias Utilizadas

- **AWS Cloud9** – IDE baseada na nuvem
- **Amazon CodeWhisperer** – Assistente de código com IA da AWS
- **Python 3** – Linguagem utilizada nos exercícios
- **Regex (re)** – Expressões regulares para validação de e-mails
- **Módulo `datetime`** – Para exibição da data atual

---

## 📋 Tarefas Realizadas

### ✅ Tarefa 1: Criar um ambiente no AWS Cloud9
- Criado ambiente EC2 no Cloud9 com Amazon Linux 2 e instância `t2.micro`
- Região selecionada: Norte da Virgínia (us-east-1)
- Conectado automaticamente ao Amazon CodeWhisperer

### ✅ Tarefa 2: Gerar uma função completa com CodeWhisperer
- Criado um novo arquivo Python `CodeWhispererTest.py`
- Gerada função `validate_email(email)` com expressões regulares via comentário
- Corrigido erro com importação automática do módulo `re`
- Criada função `main()` usando sugestões automáticas para:
  - Solicitar e validar e-mail via `input()`
  - Exibir mensagens baseadas na validação
  - Chamar a função principal via `if __name__ == "__main__"`

### ✅ Tarefa 3: Preenchimento de bloco com CodeWhisperer
- Substituído o código da função `main()` por um loop `while True`
- CodeWhisperer gerou automaticamente lógica para repetir solicitação de e-mail até entrada válida
- Mensagens ajustadas para feedback ao usuário

### ✅ Tarefa 4: Preenchimento de linha única
- Adicionada linha para exibir a data atual no início da função `main()`
- Utilizado o CodeWhisperer para completar automaticamente:
  ```python
  print("Today's date is: " + date.today().strftime("%B %d, %Y"))
  
### 💻 Execução do Código

Para rodar o programa:

1. Certifique-se de que o ambiente está ativo no **AWS Cloud9**.
2. No terminal bash, execute:

   ```bash
   python3 CodeWhispererTest.py
   
### 🧪 Teste com diferentes formatos de e-mails:

- **Válido:** `exemplo@email.com`  
- **Inválido:** `email@.com`

---

### ✨ Resultado Esperado

- Impressão da data atual  
- Solicitação de um e-mail ao usuário  
- Mensagem indicando se o e-mail é **válido** ou **inválido**  
- Loop até que um e-mail **válido** seja fornecido  

---

### 📚 Créditos

Este laboratório foi realizado por meio do **AWS Academy Learner Lab**, utilizando conteúdos de treinamento oficiais da AWS.

_____________________________________________________________________

         ___        ______     ____ _                 _  ___  
        / \ \      / / ___|   / ___| | ___  _   _  __| |/ _ \ 
       / _ \ \ /\ / /\___ \  | |   | |/ _ \| | | |/ _` | (_) |
      / ___ \ V  V /  ___) | | |___| | (_) | |_| | (_| |\__, |
     /_/   \_\_/\_/  |____/   \____|_|\___/ \__,_|\__,_|  /_/ 
 ----------------------------------------------------------------- 


Hi there! Welcome to AWS Cloud9!

To get started, create some files, play with the terminal,
or visit https://docs.aws.amazon.com/console/cloud9/ for our documentation.

Happy coding!
