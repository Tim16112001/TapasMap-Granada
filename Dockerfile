# 1) slim, official Python-Image
FROM python:3.12-slim

# 2) working directory
WORKDIR /app

# 3) first, just copy the requirements(Layer-Caching)
COPY requirements.txt /app/requirements.txt

# 4) install dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# 5) Copy App-Code 
COPY app /app/app
COPY pytest.ini /app/pytest.ini

# 6) Security: do not run as root
RUN useradd -m appuser
USER appuser

# 7) Port and start command
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]