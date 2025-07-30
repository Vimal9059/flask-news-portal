FROM python:3.9-slim

WORKDIR /app

# Copy project files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir Flask feedparser requests

# Ensure script is executable
RUN chmod +x update-noip.sh

EXPOSE 9999

# First run the DNS update script, then start the Flask app
ENTRYPOINT ["./update-noip.sh"]
CMD ["python", "app.py"]


