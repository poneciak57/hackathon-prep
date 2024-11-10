# Wybieramy obraz z Pythonem
FROM python:3.11-slim

RUN pip install --upgrade pip
RUN apt-get update && apt-get install -y netcat-openbsd && rm -rf /var/lib/apt/lists/*

# Ustawiamy katalog roboczy
WORKDIR /app

# Kopiujemy pliki requirements i instalujemy wymagania
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Kopiujemy kod aplikacji do kontenera
COPY . .

RUN chmod +x /app/run_somehow.sh
RUN sed -i 's/\r$//' /app/run_somehow.sh
# Ustawiamy zmienną środowiskową dla Django
# ENV PYTHONUNBUFFERED=1

# Komenda startowa dla Django
CMD ["sh", "-c", "/app/run_somehow.sh"]