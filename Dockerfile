FROM python:3.9-slim
WORKDIR /News_Project
RUN apt update -y
RUN pip install Flask
RUN pip install requests
EXPOSE 9999
CMD ["python", "app.py"]

