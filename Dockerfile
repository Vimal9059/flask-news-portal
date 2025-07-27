FROM python:3.9-slim
RUN apt update -y
RUN pip install Flask
RUN pip install requests
EXPOSE 5000
CMD ["python", "app.py"]

