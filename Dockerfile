# Wybieramy obraz z Pythonem
FROM python:3.11-slim

RUN pip install --upgrade pip

# Ustawiamy katalog roboczy
WORKDIR /app

# Kopiujemy pliki requirements i instalujemy wymagania
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Kopiujemy kod aplikacji do kontenera
COPY . .

# Ustawiamy zmienną środowiskową dla Django
# ENV PYTHONUNBUFFERED=1

# Komenda startowa dla Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]