FROM python:3.9-slim
WORKDIR /app
COPY . /app
COPY index.html /var/www/html/index.html
RUN apt update -y
RUN pip install Flask
RUN pip install requests
EXPOSE 9999
CMD ["python", "app.py"]

