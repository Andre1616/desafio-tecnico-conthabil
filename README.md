# desafio-tecnico-conthabil

**Desafio de automação com Selenium**

*Automação de Download e Upload de DOM (Diário Oficial de Natal/RN)*

Este projeto é uma automação em Python que realiza o download automático dos arquivos do Diário Oficial do Município de Natal/RN e os envia para um servidor de upload público (0x0.st).


**Funcionalidades**

- Acessa o portal do DOM de Natal/RN.

- Seleciona automaticamente o mês anterior ao atual.

- Lista e baixa todos os arquivos PDF disponíveis.

- Salva os arquivos em um diretório organizado por mês-ano.

- Realiza o upload de cada arquivo para o serviço 0x0.st, retornando uma URL pública para compartilhamento.

- Opcional: envia alertas por email em caso de erros.

- Exibe alertas gráficos na tela usando tkinter quando erros críticos ocorrem.


**Pré-requisitos**

Antes de rodar a automação, é necessário ter instalado:

- Python 3.8+

- Firefox (navegador usado pelo Selenium)

- GeckoDriver (driver para o Firefox)

As bibliotecas Python abaixo:

- pip install selenium requests python-dateutil



**Como usar**

Clone este repositório:

git clone https://github.com/Andre1616/desafio-tecnico-conthabil.git
cd desafio-tecnico-conthabil


Execute o script:

python desafioCONTHABIL-Andre.py

Durante a execução, você será perguntado se deseja receber erros por email:
Deseja receber erros em uma conta gmail? (s/n):
Caso selecione "s", informe:

- Email remetente (Gmail)

- Senha de app do Gmail

- Email destinatário

Os arquivos serão:

Baixados na pasta DOMs-MÊS-ANO (exemplo: DOMs 07-2025)

Enviados para o 0x0.st, com links públicos exibidos no console.

Estrutura do Projeto

desafio-tecnico-conthabil
- desafioCONTHABIL-Andre.py   # Script principal
- README.md          # Documentação do projeto
- DOMs-MM-YYYY       # Diretório criado automaticamente com os arquivos baixados

**Tecnologias utilizadas**

Python 3

Selenium WebDriver

Requests

Python-dateutil

Tkinter

SMTP

Tutorial passo a passo de como ativar e gerar uma senha de app no Gmail:
----------------------------------------------------------------------------------------------------------------------------------------------------------------------

**Passo 1: Acessar sua Conta Google**

- Abra https://myaccount.google.com/

- Faça login com sua conta do Gmail que deseja usar como remetente.


**Passo 2: Ativar a Verificação em Duas Etapas**

- Para gerar senhas de app, a verificação em duas etapas precisa estar ativada:

- No menu lateral, clique em Segurança.

- Em “Acesso ao Google”, encontre Verificação em duas etapas.

- Clique em Configurar e siga os passos para ativar (pode ser via app Google Authenticator ou SMS).


**Passo 3: Gerar uma Senha de App**

- Após ativar a verificação em duas etapas, volte à seção Segurança.

- Em “Acesso ao Google”, clique em Senhas de app.

- Faça login novamente se solicitado.

- No menu suspenso Selecionar app, escolha Outro (Personalizado).

- Digite um nome para identificar o app, por exemplo: Automação Selenium.

- Clique em Gerar.

- O Google exibirá uma senha de 16 caracteres. Copie essa senha para usá-la no script.
