FROM python:3.11-slim

WORKDIR /app

# Install system dependencies including awscli
RUN apt-get update && apt-get install -y --no-install-recommends \
    awscli \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY . /app

# Install python dependencies and the project package
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir -e .

EXPOSE 8000

CMD ["python", "app.py"]