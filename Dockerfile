FROM python:3.9-slim
WORKDIR /app
COPY . /app
RUN pip install Flask
RUN pip install requests
EXPOSE 9999
CMD ["python", "app.py"]

