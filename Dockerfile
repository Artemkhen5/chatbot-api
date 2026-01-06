FROM python:3.12-alpine

WORKDIR /app

# Устанавливаем системные зависимости для psycopg2 и компилятор
RUN apk add --no-cache \
    postgresql-dev \
    gcc \
    musl-dev \
    linux-headers

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Удаляем компилятор, чтобы уменьшить размер образа
RUN apk del gcc musl-dev linux-headers

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]