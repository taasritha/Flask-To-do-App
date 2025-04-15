FROM python:3.9-slim
WORKDIR /flask-to-do-app
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
