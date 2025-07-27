FROM python:3.9-slim
WORKDIR /app
# Copy all files first
COPY . /app

# Install all Python dependencies in one go for caching efficiency
RUN pip install --no-cache-dir Flask feedparser requests
EXPOSE 9999
CMD ["python", "app.py"]

