# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project files
COPY . /app/

# Expose the port (optional for debugging)
EXPOSE 8000

# Default command (runserver)
CMD ["gunicorn", "taskmanager.wsgi:application", "--bind", "0.0.0.0:8000"]
