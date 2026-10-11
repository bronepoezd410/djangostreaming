FROM python:3.11-slim

# Install system dependencies for mysqlclient and other packages
RUN apt-get update && apt-get install -y \
    pkg-config \
    libmariadb-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code
COPY . .

# Command for development
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]