FROM python:3.11-slim

WORKDIR /app

# Установка системных зависимостей
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

RUN curl -o allure-2.15.0.tgz -Ls https://github.com/allure-framework/allure2/releases/download/2.15.0/allure-2.15.0.tgz \
    && tar -zxvf allure-2.15.0.tgz -C /opt/ \
    && ln -s /opt/allure-2.15.0/bin/allure /usr/bin/allure \
    && rm allure-2.15.0.tgz

RUN mkdir -p /app/allure-results

CMD ["pytest", "-v", "--alluredir=/app/allure-results"]