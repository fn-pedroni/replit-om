# Use Python 3.11 slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install uv for faster dependency management
RUN pip install uv

# Copy dependency files first for better caching
COPY pyproject.toml uv.lock ./

# Install dependencies
RUN uv sync --frozen

# Copy application files
COPY . .

# Expose port 5000
EXPOSE 5000

# Set environment variable for production
ENV FLASK_ENV=production
ENV SESSION_SECRET=docker-default-secret-change-in-production

# Run the application using gunicorn
CMD ["uv", "run", "gunicorn", "--bind", "0.0.0.0:5000", "--reuse-port", "main:app"]