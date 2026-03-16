# Use a stable version that has pre-compiled wheels for all your libs
FROM python:3.10-slim

# Install minimal system dependencies for building if needed
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy and install requirements first to leverage Docker caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code
COPY . .

# Adjust 'app:app' if your Flask file is named differently (e.g., main:app)
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:10000"]