# Base image for web
FROM python:3.10-slim AS web

# Install dependencies
RUN apt-get update \
    && apt-get install -y gcc \
    && apt-get install -y --no-install-recommends \
       libjpeg-dev \
       zlib1g-dev \
       python3-venv \
       python3-dev \
       python3-pip \
       procps \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app/

# Create and activate virtual environment
RUN python3 -m venv /venv \
    && /venv/bin/pip install --upgrade pip \
    && /venv/bin/pip install --no-cache-dir -r requirements.txt

# Run migrations and collect static files
RUN /venv/bin/python manage.py makemigrations \
    && /venv/bin/python manage.py migrate \
    && /venv/bin/python manage.py collectstatic --noinput

# Expose the port
EXPOSE 8000

# Start Gunicorn server with the correct path to the WSGI application
CMD ["/venv/bin/gunicorn", "--bind", "0.0.0.0:8000", "backend.wsgi:application"]