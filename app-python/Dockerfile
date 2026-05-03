# Utiliza uma imagem leve do Python
FROM python:3.9-slim

# Define o diretório de trabalho
WORKDIR /app

# Instala a dependência necessária (Flask)
# Em projetos maiores, usaríamos um requirements.txt
RUN pip install --no-cache-dir flask

RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# Copia o código da aplicação
COPY app.py .

# Expõe a porta que a aplicação utiliza
EXPOSE 5001

HEALTHCHECK --interval=10s --timeout=3s CMD curl -f http://localhost:5001/texto || exit 1

# Comando para iniciar a aplicação
CMD ["python", "app.py"]