FROM python:3.9-slim

WORKDIR /app

# Copy all project files into the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir Flask feedparser requests

# Ensure update-noip.sh has execute permission
RUN chmod +x update-noip.sh

EXPOSE 9999

# Run DNS updater and then the Flask app
CMD ./update-noip.sh && python app.py


