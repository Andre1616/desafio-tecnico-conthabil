# desafio-tecnico-conthabil

**Desafio de automação com Selenium
**
Automação de Download e Upload de DOM (Diário Oficial de Natal/RN)

Este projeto é uma automação em Python que realiza o download automático dos arquivos do Diário Oficial do Município de Natal/RN e os envia para um servidor de upload público (0x0.st).

**Funcionalidades**

- Acessa o portal do DOM de Natal/RN.

- Seleciona automaticamente o mês anterior ao atual.

- Lista e baixa todos os arquivos PDF disponíveis.

- Salva os arquivos em um diretório organizado por mês-ano.

- Realiza o upload de cada arquivo para o serviço 0x0.st, retornando uma URL pública para compartilhamento.

**Pré-requisitos**

Antes de rodar a automação, é necessário ter instalado:

- Python 3.8+

- Firefox (navegador usado pelo Selenium)

- GeckoDriver (driver para o Firefox)

As bibliotecas Python abaixo:

- pip install selenium requests

**Como usar**

Clone este repositório:

git clone https://github.com/Andre1616/desafio-tecnico-conthabil.git
cd desafio-tecnico-conthabil


Execute o script:

python desafioCONTHABIL-Andre.py


Os arquivos serão:

Baixados na pasta DOMs-MÊS-ANO (exemplo: DOMs 07-2025)

Enviados para o 0x0.st, com links públicos exibidos no console.

📂 Estrutura do Projeto
📁 desafio-tecnico-conthabil
 ┣ 📜 desafioCONTHABIL-Andre.py   # Script principal
 ┣ 📜 README.md          # Documentação do projeto
 ┗ 📂 DOMs-MM-YYYY       # Diretório criado automaticamente com os arquivos baixados

**Tecnologias utilizadas**

Python 3

Selenium WebDriver

Requests
