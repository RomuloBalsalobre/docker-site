# Usar uma imagem base do Python
FROM python:3.9-slim

# Definir o diretório de trabalho
WORKDIR /app

# Copiar o arquivo requirements.txt para o contêiner
COPY requirements.txt .

# Instalar as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o código da aplicação para o contêiner
COPY . .

# Expor a porta que o Flask usará
EXPOSE 5000

# Definir o comando padrão para rodar a aplicação usando gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]