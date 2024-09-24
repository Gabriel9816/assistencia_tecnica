# Assistência Técnica

Este projeto é um sistema de gerenciamento de assistência técnica, que permite o cadastro de clientes, a abertura e acompanhamento de chamados, e o envio de notificações automáticas por email aos clientes sobre o status de seus chamados.

## Funcionalidades

- **Cadastro de Clientes**: Permite o registro de novos clientes no sistema.
- **Gerenciamento de Chamados**: Criação e acompanhamento de chamados técnicos para clientes.
- **Envio de Emails**: O sistema envia automaticamente notificações por email aos clientes quando um novo chamado é registrado ou o status de um chamado é atualizado.
- **Uso de Banco de Dados na Nuvem**: Utiliza MongoDB Atlas para armazenar as informações dos clientes e chamados.
- **Containerização com Docker**: A aplicação pode ser containerizada para facilitar o deploy em qualquer ambiente.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal utilizada para o backend.
- **MongoDB Atlas**: Banco de dados NoSQL hospedado na nuvem para armazenar dados de clientes e chamados.
- **SMTP (via Gmail)**: Para envio de notificações por email.
- **Docker**: Utilizado para criar containers e facilitar a execução da aplicação em diferentes ambientes.
- **GitHub Actions**: Usado para automação de CI/CD (integração contínua e deploy).

## Requisitos

Antes de rodar o projeto localmente, certifique-se de ter instalado:

- **Python 3.9+**
- **Docker** (para rodar a aplicação em containers, opcional)
- **MongoDB Atlas** (ou outro banco de dados MongoDB local)

## Configuração

### 1. Clonar o repositório

```bash
git clone https://github.com/Gabriel9816/assistencia_tecnica.git
cd assistencia_tecnica

2. Configurar as dependências
Ambiente virtual Python (opcional, mas recomendado):

bash
Copiar código
python3 -m venv venv
source venv/bin/activate
Instalar as dependências:

bash
Copiar código
pip install -r requirements.txt
3. Configurar variáveis de ambiente
No código, as credenciais de email e banco de dados estão definidas diretamente. Se preferir, crie um arquivo .env com suas credenciais de forma segura.
Exemplo de .env:

bash
Copiar código
EMAIL_USER=gabriel.oliveira6@estudante.ifms.edu.br
EMAIL_PASS=sua_senha_de_aplicativo
DB_HOST=sua_url_do_mongodb
DB_NAME=assistencia_tecnica
4. Rodar a aplicação localmente
Se você estiver rodando o banco de dados MongoDB localmente ou na nuvem, execute:

bash
Copiar código
python3 assistencia_tecnica.py
5. Usando Docker (Opcional)
Se você quiser rodar a aplicação em um container Docker, siga os passos abaixo:

Construir a imagem Docker:

bash
Copiar código
docker build -t assistencia_tecnica .
Rodar o container:

bash
Copiar código
docker run -d -p 5000:5000 --name assistencia_tecnica_container assistencia_tecnica
Testes
Se você tiver testes automatizados configurados, execute-os com o seguinte comando:

bash
Copiar código
python -m unittest discover
Contribuição
Se você quiser contribuir com o projeto:

Faça um fork do repositório.
Crie uma nova branch para suas modificações (git checkout -b minha-branch).
Faça um commit das suas mudanças (git commit -m 'Adicionar nova funcionalidade').
Faça um push para a branch (git push origin minha-branch).
Abra um Pull Request.

