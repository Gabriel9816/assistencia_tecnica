# Usar uma imagem base Python
FROM python:3.9-slim

# Definir o diretório de trabalho dentro do container
WORKDIR /app

# Copiar o requirements.txt e instalar dependências
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copiar o restante do código para o container
COPY . .

# Expor a porta que o Flask vai rodar
EXPOSE 5000

# Definir o comando para rodar sua aplicação
CMD ["python", "app.py"]
